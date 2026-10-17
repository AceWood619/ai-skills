#!/usr/bin/env python3
"""Classify a proposed smart-home action; never executes it."""
from __future__ import annotations

import argparse
import json
import re

# Normalize underscores/hyphens to spaces for matching
def norm(text: str) -> str:
    return re.sub(r'[\s_\-]+', ' ', text.lower()).strip()

DESTRUCTIVE = (
    'factory reset', 'delete', 'wipe', 'disable safety', 'remove device',
    'reset', 'purge', 'format',
)
SECURITY = (
    'unlock', 'lock', 'disarm', 'arm', 'alarm', 'garage', 'door open',
    'access', 'disable alarm', 'open lock',
)
PRIVACY = (
    'camera', 'stream', 'snapshot', 'recording', 'microphone', 'listen',
)
SENSITIVE = SECURITY + PRIVACY + (
    'spend', 'payment', 'notify all', 'announce',
)
# State-changing but typically low physical risk
REVERSIBLE = (
    'turn on', 'turn off', 'toggle', 'set ', 'adjust ', 'open ', 'close ',
    'brighten', 'dim', 'volume', 'play', 'pause', 'stop', 'scene',
    'activate', 'deactivate', 'increase', 'decrease',
)
READ_HINTS = (
    'state', 'status', 'get ', 'read ', 'list ', 'history', 'log',
)


def classify(action: str) -> str:
    text = norm(action)
    if any(x in text for x in DESTRUCTIVE):
        return 'destructive'
    if any(x in text for x in SENSITIVE):
        return 'sensitive'
    if any(x in text for x in REVERSIBLE):
        return 'reversible-low-impact'
    if any(x in text for x in READ_HINTS):
        return 'read-only'
    # Domain heuristics when only entity is given
    if re.search(r'\b(lock|alarm|camera|cover|garage)\b', text):
        return 'sensitive'
    if re.search(r'\b(light|switch|fan|climate|media_player|input_boolean)\b', text):
        return 'reversible-low-impact'
    if re.search(r'\b(sensor|binary_sensor|weather|sun)\b', text):
        return 'read-only'
    return 'read-only'


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action')
    p.add_argument('--confirmed', action='store_true')
    args = p.parse_args()
    level = classify(args.action)
    requires = level in {'sensitive', 'destructive'}
    authorized = False  # never authorizes device control
    if requires:
        next_step = 'request exact confirmation and use an explicit device-control tool'
    elif level == 'reversible-low-impact':
        next_step = 'confirm intent if ambiguous, then use an explicit authorized device-control tool'
    else:
        next_step = 'inspect state or use an explicit authorized read-only tool'
    result = {
        'action': args.action,
        'classification': level,
        'confirmation_required': requires,
        'authorized_to_execute': authorized,
        'confirmed_flag_seen': bool(args.confirmed),
        'next_step': next_step,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
