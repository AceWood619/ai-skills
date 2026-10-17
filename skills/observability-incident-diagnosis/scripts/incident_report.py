#!/usr/bin/env python3
"""Validate an incident JSON record and identify missing diagnosis controls."""
import argparse, json
from pathlib import Path
REQUIRED=['impact','start_time','timeline','hypotheses','evidence','containment','next_test']
def main():
 p=argparse.ArgumentParser(); p.add_argument('record',type=Path); args=p.parse_args()
 d=json.loads(args.record.read_text()); missing=[x for x in REQUIRED if not d.get(x)]
 flags=[]
 if len(d.get('hypotheses',[]))<2: flags.append('record at least two competing hypotheses')
 if not d.get('rollback_or_recovery'): flags.append('define a recovery or rollback path')
 if not d.get('root_cause_confidence'): flags.append('state root-cause confidence')
 print(json.dumps({'status':'invalid' if missing else ('review' if flags else 'ready'),'missing':missing,'flags':flags},indent=2))
 return 1 if missing else 0
if __name__=='__main__': raise SystemExit(main())
