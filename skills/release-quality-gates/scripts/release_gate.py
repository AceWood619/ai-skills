#!/usr/bin/env python3
"""Evaluate a JSON release record with required and advisory gates."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('record', type=Path)
    args = p.parse_args()
    data = json.loads(args.record.read_text())
    gates = data.get('gates')
    notes: list[str] = []

    if gates is None:
        notes.append('missing gates array')
        decision = 'review'
        failed_required: list[str] = []
        advisory: list[str] = []
    elif not isinstance(gates, list) or len(gates) == 0:
        notes.append('gates array is empty; no evidence to pass a release')
        decision = 'review'
        failed_required = []
        advisory = []
    else:
        failed_required = [
            g.get('name', 'unnamed')
            for g in gates
            if isinstance(g, dict) and g.get('required', True) and g.get('status') != 'pass'
        ]
        advisory = [
            g.get('name', 'unnamed')
            for g in gates
            if isinstance(g, dict) and not g.get('required', True) and g.get('status') != 'pass'
        ]
        if failed_required:
            decision = 'block'
        elif advisory or notes:
            decision = 'review'
        else:
            decision = 'pass'

    out = {
        'decision': decision,
        'failed_required': failed_required,
        'advisory_failures': advisory,
        'notes': notes,
    }
    print(json.dumps(out, indent=2))
    return 1 if decision == 'block' else 0


if __name__ == '__main__':
    raise SystemExit(main())
