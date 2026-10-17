#!/usr/bin/env python3
"""Detect high-signal breaking changes between two OpenAPI/Swagger JSON documents."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

METHODS = {'get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace'}


def load(path: Path) -> dict:
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or not isinstance(data.get('paths', {}), dict):
        raise ValueError(f'{path} is not an object with a paths map')
    return data


def finding(severity: str, location: str, before, after, impact: str, remediation: str) -> dict:
    return {
        'severity': severity,
        'location': location,
        'before': before,
        'after': after,
        'impact': impact,
        'remediation': remediation,
    }


def params(operation: dict) -> dict:
    return {(p.get('in'), p.get('name')): p for p in operation.get('parameters', []) if isinstance(p, dict)}


def compare(old: dict, new: dict) -> list[dict]:
    findings: list[dict] = []
    old_paths, new_paths = old.get('paths', {}), new.get('paths', {})

    for path in sorted(set(old_paths) - set(new_paths)):
        findings.append(
            finding(
                'breaking',
                path,
                'present',
                'removed',
                'Existing consumers cannot call this path.',
                'Restore it or publish a compatible version.',
            )
        )

    for path in sorted(set(old_paths) & set(new_paths)):
        old_item, new_item = old_paths[path], new_paths[path]
        old_methods = {m for m in old_item if m in METHODS and isinstance(old_item[m], dict)}
        new_methods = {m for m in new_item if m in METHODS and isinstance(new_item[m], dict)}

        for method in sorted(old_methods - new_methods):
            findings.append(
                finding(
                    'breaking',
                    f'{method.upper()} {path}',
                    'present',
                    'removed',
                    'Generated clients or callers lose an operation.',
                    'Restore the operation or version the change.',
                )
            )

        for method in sorted(old_methods & new_methods):
            old_op, new_op = old_item[method], new_item[method]
            old_params, new_params = params(old_op), params(new_op)

            for key in sorted(set(old_params) - set(new_params)):
                findings.append(
                    finding(
                        'breaking',
                        f'{method.upper()} {path} parameter {key}',
                        'present',
                        'removed',
                        'Callers may still send or depend on this parameter.',
                        'Keep it deprecated or version the operation.',
                    )
                )

            # Newly introduced required parameters (only in proposed)
            for key in sorted(set(new_params) - set(old_params)):
                if new_params[key].get('required', False):
                    findings.append(
                        finding(
                            'breaking',
                            f'{method.upper()} {path} parameter {key}',
                            'absent',
                            'required',
                            'Previously valid requests that omit this parameter become invalid.',
                            'Make it optional with a default, or introduce a new version.',
                        )
                    )

            # Required flipped from false/absent to true on shared parameters
            for key in sorted(set(old_params) & set(new_params)):
                was, is_now = old_params[key], new_params[key]
                if not was.get('required', False) and is_now.get('required', False):
                    findings.append(
                        finding(
                            'breaking',
                            f'{method.upper()} {path} parameter {key}',
                            False,
                            True,
                            'Previously valid requests can become invalid.',
                            'Keep it optional or introduce a new version.',
                        )
                    )

            # requestBody required flip (simple object form)
            old_body = old_op.get('requestBody') if isinstance(old_op.get('requestBody'), dict) else {}
            new_body = new_op.get('requestBody') if isinstance(new_op.get('requestBody'), dict) else {}
            if new_body and new_body.get('required', False) and not old_body.get('required', False):
                # only flag when baseline had no required body (including no body)
                if not old_body or not old_body.get('required', False):
                    findings.append(
                        finding(
                            'breaking',
                            f'{method.upper()} {path} requestBody',
                            old_body.get('required', False) if old_body else 'absent',
                            True,
                            'Clients that omitted a body may fail against the proposed contract.',
                            'Keep the body optional or version the operation.',
                        )
                    )

            old_resp, new_resp = old_op.get('responses', {}), new_op.get('responses', {})
            for status in sorted(set(old_resp) - set(new_resp), key=str):
                findings.append(
                    finding(
                        'breaking',
                        f'{method.upper()} {path} response {status}',
                        'documented',
                        'removed',
                        'Consumers may branch on this documented response.',
                        'Keep the response or document the compatibility impact.',
                    )
                )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('baseline', type=Path)
    parser.add_argument('proposed', type=Path)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    try:
        findings = compare(load(args.baseline), load(args.proposed))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f'ERROR: {exc}')
        return 2
    decision = 'block' if any(f['severity'] == 'breaking' for f in findings) else 'pass'
    result = {'decision': decision, 'findings': findings}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print('DECISION:', decision)
        for f in findings:
            print(f"[{f['severity']}] {f['location']}: {f['impact']} Remediation: {f['remediation']}")
        if not findings:
            print('No high-signal breaking changes detected.')
    return 1 if decision == 'block' else 0


if __name__ == '__main__':
    raise SystemExit(main())
