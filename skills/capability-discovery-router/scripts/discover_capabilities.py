#!/usr/bin/env python3
"""Discover local skills plus optional connector and MCP catalogs without enabling or calling them."""
from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
from pathlib import Path

DEFAULT_SKILL_DIRS = tuple(
    Path(p).expanduser()
    for p in os.environ.get('SKILLS_DIRS', '~/.claude/skills:.claude/skills').split(os.pathsep)
    if p
)


def frontmatter(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding='utf-8', errors='replace')
    block = text.split('\n---\n', 1)[0] if text.startswith('---\n') else ''
    name = re.search(r'^name:\s*["\']?([^"\'\n]+)', block, re.M)
    desc = re.search(r'^description:\s*["\']?([^"\'\n]+)', block, re.M)
    return (name.group(1).strip() if name else path.parent.name, desc.group(1).strip() if desc else '')


def discover_skills(roots: list[Path]) -> list[dict]:
    items: list[dict] = []
    seen: set[str] = set()
    for root in roots:
        if not root.is_dir():
            continue
        for skill in sorted(root.iterdir()):
            md = skill / 'SKILL.md'
            if not md.is_file():
                continue
            name, desc = frontmatter(md)
            key = name.lower()
            if key in seen:
                continue
            seen.add(key)
            items.append({
                'name': name,
                'kind': 'skill',
                'source': str(md),
                'status': 'installed',
                'capabilities': desc,
            })
    return items


def discover_connectors(command: str) -> list[dict]:
    try:
        proc = subprocess.run(shlex.split(command), capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError):
        return []
    items = []
    for line in proc.stdout.splitlines():
        m = re.match(r'^(\S+)\s+(.+?)\s+\[([^]]+)\]\s+.*\s+(enabled|disabled)\s*$', line.strip(), re.I)
        if m:
            uid, name, kind, state = m.groups()
            items.append({
                'name': name,
                'kind': 'connector',
                'source': 'connector-catalog',
                'uid': uid,
                'status': 'enabled' if state.lower() == 'enabled' else 'listed-disabled',
                'capabilities': kind,
                'authorization': 'unknown',
            })
    return items


def discover_mcp(path: Path | None) -> list[dict]:
    if not path or not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError):
        return []
    servers = data.get('servers', data) if isinstance(data, dict) else data
    if not isinstance(servers, list):
        return []
    return [
        {
            'name': x.get('name', 'unnamed'),
            'kind': 'server',
            'source': str(path),
            'status': x.get('status', 'unknown'),
            'capabilities': x.get('capabilities', []),
            'authorization': x.get('authorization', 'unknown'),
        }
        for x in servers
        if isinstance(x, dict)
    ]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--task', default='')
    p.add_argument(
        '--skills-dir',
        type=Path,
        action='append',
        dest='skills_dirs',
        help='Skills root (repeatable). Defaults to user + bundled roots.',
    )
    p.add_argument('--connector-command', default='manus-config connector list')
    p.add_argument('--mcp-manifest', type=Path)
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    roots = args.skills_dirs if args.skills_dirs else list(DEFAULT_SKILL_DIRS)
    items = discover_skills(roots) + discover_connectors(args.connector_command) + discover_mcp(args.mcp_manifest)
    tokens = {x.lower() for x in re.findall(r'[A-Za-z0-9_-]{3,}', args.task)}
    matches = []
    for item in items:
        hay = (item['name'] + ' ' + str(item.get('capabilities', ''))).lower()
        score = sum(t in hay for t in tokens)
        if score:
            matches.append({'score': score, **item})
    matches.sort(key=lambda x: (-x['score'], x['status'] not in {'installed', 'enabled', 'ready'}, x['name']))
    result = {'counts': {}, 'matches': matches[:20], 'capabilities': items, 'skills_roots': [str(r) for r in roots]}
    for item in items:
        result['counts'][item['kind']] = result['counts'].get(item['kind'], 0) + 1
    if len(matches) >= 3:
        result['route'] = (
            'decompose the prompt into subtasks, compose the highest-scoring ready or '
            'installed capabilities, and verify authorization for each'
        )
    elif matches:
        result['route'] = 'select the highest-scoring ready or installed capability, then verify authorization'
    else:
        result['route'] = 'no suitable capability found; hand off gap to skill-creator or autonomous-skill-evolution'
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print('ROOTS:', result['skills_roots'])
        print('COUNTS:', result['counts'])
        print('ROUTE:', result['route'])
        for item in matches[:10]:
            print(f"[{item['status']}] {item['kind']}: {item['name']} (score {item['score']})")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
