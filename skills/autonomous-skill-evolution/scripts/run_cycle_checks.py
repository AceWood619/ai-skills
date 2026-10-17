#!/usr/bin/env python3
"""Run acceptance gates for one candidate skill and the full skill registry."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def run(command: list[str]) -> tuple[int, str]:
    p = subprocess.run(command, capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate', type=Path, help='candidate skill directory')
    parser.add_argument('--skills', type=Path, default=Path('/home/workdir/.grok/skills'))
    args = parser.parse_args()
    failures: list[str] = []
    skill_md = args.candidate / 'SKILL.md'
    validator = Path('/root/.grok/skills/skill-creator/scripts/quick_validate.py')
    audit_script = Path('/home/workdir/.grok/skills/skill-evolution/scripts/audit_skills.py')
    if not skill_md.is_file():
        failures.append('candidate is missing SKILL.md')
    else:
        text = skill_md.read_text(encoding='utf-8')
        if not text.startswith('---\n'):
            failures.append('candidate has no YAML frontmatter')
        if 'TODO' in text:
            failures.append('candidate contains TODO placeholders')
        if len(text.splitlines()) >= 500:
            failures.append('candidate SKILL.md is 500 lines or longer')
        if 'Skip when' not in text and 'Skip When' not in text:
            failures.append('candidate has no explicit skip cases')
        name_m = re.search(r'^name:\s*(.+)$', text, re.MULTILINE)
        if not name_m or name_m.group(1).strip() != args.candidate.name:
            failures.append('frontmatter name missing or does not match directory')
        if validator.is_file():
            code, output = run(['python3', str(validator), str(args.candidate)])
            if code != 0 or 'Skill is valid!' not in output:
                failures.append('official validator failed: ' + (output.splitlines()[-1] if output else 'no output'))

    audit_code, audit_output = run([
        'python3', str(audit_script),
        '--skills', str(args.skills), '--json'
    ])
    if audit_code != 0:
        failures.append('registry audit failed')
    else:
        try:
            data = json.loads(audit_output)
            if any(not item['valid'] for item in data['skills']):
                failures.append('registry contains invalid skill packages')
            if data.get('duplicate_names'):
                failures.append('registry contains duplicate skill names')
        except json.JSONDecodeError:
            failures.append('registry audit returned non-JSON')

    if failures:
        for failure in failures:
            print('FAIL:', failure)
        print('RESULT: CYCLE CHECKS FAILED')
        return 1
    print('RESULT: CYCLE CHECKS PASSED')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
