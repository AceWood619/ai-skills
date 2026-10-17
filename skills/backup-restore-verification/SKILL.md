---
name: backup-restore-verification
description: Verify backup freshness, coverage, integrity, restore procedures, recovery objectives, and restoration evidence. Use when testing disaster recovery, validating RPO or RTO, documenting restore readiness, or investigating an unproven backup.
---

# Backup and Restore Verification

Convert backup claims into scoped, auditable evidence without risking production data.

## Workflow

1. Define backup scope, data sensitivity, RPO, RTO, target environment, authorization, and cleanup plan.
2. Check freshness, coverage, retention, integrity, encryption or access assumptions, and metadata completeness.
3. Test restoration only in an authorized isolated target; record start/end times, result, completeness, and achieved RPO/RTO.
4. Mark each check pass, fail, or unknown with evidence and missing inputs.
5. Document remediation, owner, next test date, and limitations. Do not claim recovery success without restore evidence.

## Guardrails

Default to read-only inspection and isolated reversible tests. Never delete, expire, overwrite, alter, or expose production backups. Require explicit authorization for any restore or cleanup.

## Output contract

Return scope, verification plan, evidence table, calculated objectives, failures, remediation, owner, review date, and residual uncertainty.

## Skip when

- The request is generic backup-product guidance without verification.
- No backup metadata, target, objective, or evidence is available.
- The task is an active production recovery incident rather than a readiness review.
