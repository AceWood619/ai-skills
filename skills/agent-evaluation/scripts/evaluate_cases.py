#!/usr/bin/env python3
"""Evaluate JSON cases against supplied text outputs using simple deterministic assertions."""
import argparse, json
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument('cases', type=Path)
    p.add_argument('outputs', type=Path)
    args=p.parse_args()
    cases=json.loads(args.cases.read_text())
    outputs=json.loads(args.outputs.read_text())
    results=[]
    for case in cases:
        name=case['id']; text=outputs.get(name,'').lower()
        missing=[x for x in case.get('required_contains',[]) if x.lower() not in text]
        forbidden=[x for x in case.get('forbidden_contains',[]) if x.lower() in text]
        results.append({'id':name,'status':'pass' if not missing and not forbidden else 'fail','missing':missing,'forbidden':forbidden})
    print(json.dumps({'results':results,'passed':sum(r['status']=='pass' for r in results),'failed':sum(r['status']=='fail' for r in results)},indent=2))
    return 1 if any(r['status']=='fail' for r in results) else 0
if __name__=='__main__': raise SystemExit(main())
