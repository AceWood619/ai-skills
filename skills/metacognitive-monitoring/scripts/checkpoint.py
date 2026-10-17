#!/usr/bin/env python3
"""Validate a metacognitive checkpoint JSON file and report risk flags."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = {
    'goal', 'success_test', 'state', 'prediction', 'observation',
    'evidence', 'assumptions_at_risk', 'confidence', 'next_action',
    'stop_or_escalation',
}
STATES = {'on-track', 'uncertain', 'blocked', 'failed', 'complete'}
CONFIDENCE = {'high', 'medium', 'low'}


def validate(data: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    flags: list[str] = []
    missing = sorted(REQUIRED - data.keys())
    if missing:
        errors.append('missing required fields: ' + ', '.join(missing))
    if data.get('state') not in STATES:
        errors.append('state must be one of: ' + ', '.join(sorted(STATES)))
    if data.get('confidence') not in CONFIDENCE:
        errors.append('confidence must be high, medium, or low')
    if data.get('confidence') == 'high' and len(data.get('evidence', [])) < 2:
        flags.append('high confidence has fewer than two evidence items; consider lowering confidence')
    if data.get('state') in {'blocked', 'failed'} and not data.get('stop_or_escalation'):
        flags.append('blocked or failed state needs an explicit stop or escalation condition')
    if data.get('state') != 'complete' and not data.get('next_action'):
        flags.append('non-complete state has no next action')
    if data.get('prediction') == data.get('observation'):
        flags.append('prediction and observation are textually identical; verify that an actual observation was recorded')
    if not data.get('assumptions_at_risk'):
        flags.append('no assumptions at risk recorded; add a falsifiable assumption or state why none apply')
    return errors, flags


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoint', type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.checkpoint.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        print(f'ERROR: cannot read JSON checkpoint: {exc}')
        return 2
    if not isinstance(data, dict):
        print('ERROR: checkpoint root must be a JSON object')
        return 2
    errors, flags = validate(data)
    for error in errors:
        print('ERROR:', error)
    for flag in flags:
        print('FLAG:', flag)
    if errors:
        print('RESULT: INVALID')
        return 1
    print('RESULT: VALID' if not flags else 'RESULT: VALID WITH FLAGS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
