#!/usr/bin/env python3
"""Audit skills for package shape, metadata, references, and validator status."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
NAME = re.compile(r"^name:\s*([^\n]+)$", re.MULTILINE)
DESCRIPTION = re.compile(r"^description:\s*(.+)$", re.MULTILINE)


def audit(path: Path, validator: Path | None) -> dict:
    result = {
        "directory": str(path),
        "name": path.name,
        "valid": True,
        "checks": [],
        "warnings": [],
    }
    skill_md = path / "SKILL.md"
    if not skill_md.is_file():
        result["valid"] = False
        result["checks"].append("missing SKILL.md")
        return result

    text = skill_md.read_text(encoding="utf-8")
    result["lines"] = len(text.splitlines())
    if result["lines"] > 500:
        result["valid"] = False
        result["checks"].append("SKILL.md exceeds 500 lines")
    match = FRONTMATTER.match(text)
    if not match:
        result["valid"] = False
        result["checks"].append("invalid or missing YAML frontmatter")
    else:
        name = NAME.search(match.group(1))
        description = DESCRIPTION.search(match.group(1))
        if not name or not name.group(1).strip():
            result["valid"] = False
            result["checks"].append("missing name")
        elif name.group(1).strip() != path.name:
            result["warnings"].append("frontmatter name differs from directory")
        if not description or not description.group(1).strip():
            result["valid"] = False
            result["checks"].append("missing description")

    for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if link.startswith(("http://", "https://", "#", "manus-resource://", "?") ) or "{" in link:
            continue
        target = (skill_md.parent / link.split("#", 1)[0]).resolve()
        if not target.exists():
            result["warnings"].append(f"unresolved local link: {link}")

    if validator and validator.is_file():
        proc = subprocess.run(
            ["python3", str(validator), str(path)],
            capture_output=True,
            text=True,
        )
        result["validator"] = "pass" if proc.returncode == 0 and "Skill is valid!" in proc.stdout else "fail"
        if result["validator"] == "fail":
            result["valid"] = False
            result["checks"].append((proc.stdout + proc.stderr).strip().splitlines()[-1])
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills", type=Path, default=Path("/home/workdir/.grok/skills"))
    parser.add_argument("--validator", type=Path, default=Path("/root/.grok/skills/skill-creator/scripts/quick_validate.py"))
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    paths = sorted(p for p in args.skills.iterdir() if p.is_dir() and not p.name.startswith("."))
    results = [audit(path, args.validator) for path in paths]
    names = [r["name"] for r in results]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if args.json:
        print(json.dumps({"skills": results, "duplicate_names": duplicates}, indent=2))
    else:
        print("skill\tstatus\tlines\tvalidator\tissues")
        for result in results:
            issues = "; ".join(result["checks"] + result["warnings"]) or "-"
            print(f"{result['name']}\t{'PASS' if result['valid'] else 'FAIL'}\t{result.get('lines', '-')}	{result.get('validator', '-')}\t{issues}")
        print(f"\nAudited: {len(results)} skills; duplicate names: {', '.join(duplicates) or 'none'}")
    return 1 if any(not r["valid"] for r in results) or duplicates else 0


if __name__ == "__main__":
    raise SystemExit(main())
