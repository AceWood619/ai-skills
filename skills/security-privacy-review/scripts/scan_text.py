#!/usr/bin/env python3
"""Scan text artifacts for high-signal security and privacy patterns without printing secret values."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

# Patterns intentionally avoid capturing secret values in output — only type + line.
PATTERNS: list[tuple[str, str]] = [
    (
        'credential-risk',
        r'(?i)('
        r'api[_ -]?key|secret[_ -]?access[_ -]?key|secret|password|passwd|token|'
        r'authorization|bearer|private[_ -]?key|aws[_ -]?secret|client[_ -]?secret'
        r')\s*[:=]\s*\S+'
    ),
    (
        'credential-risk',
        r'(?i)\b(sk-[A-Za-z0-9]{10,}|AKIA[0-9A-Z]{16})\b',
    ),
    (
        'destructive-command',
        r'(?i)(rm\s+-rf|drop\s+(database|table|schema)|format\s+disk|mkfs\.|dd\s+if=)',
    ),
    (
        'permission-change',
        r'(?i)(chmod\s+777|sudo\s+|grant\s+all|disable\s+authentication|setuid)',
    ),
    (
        'outbound-data-risk',
        r'(?i)(upload|send|post|exfiltrat)\s+.{0,40}(secret|password|personal|private|credential|ssn|token)',
    ),
]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('path', type=Path)
    args = p.parse_args()
    text = args.path.read_text(errors='replace')
    findings = []
    seen: set[tuple[str, int]] = set()
    for kind, pat in PATTERNS:
        for m in re.finditer(pat, text):
            line = text.count('\n', 0, m.start()) + 1
            key = (kind, line)
            if key in seen:
                continue
            seen.add(key)
            findings.append({'type': kind, 'line': line})
    decision = 'review' if findings else 'pass'
    print(json.dumps({'path': str(args.path), 'findings': findings, 'decision': decision}, indent=2))
    return 1 if findings else 0


if __name__ == '__main__':
    raise SystemExit(main())
