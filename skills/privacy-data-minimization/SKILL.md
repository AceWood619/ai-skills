---
name: privacy-data-minimization
description: Minimize collected data, retention, sharing, logging, uploads, exports, and redaction risk across workflows. Use when designing or reviewing a process that handles personal, confidential, or sensitive data.
---

# Privacy Data Minimization

Reduce data exposure while preserving the stated purpose and required audit or safety evidence.

## Workflow

1. Inventory each field, source, purpose, recipient, storage location, retention period, and sensitivity.
2. Decide what is necessary, optional, redundant, or unjustified for the purpose.
3. Minimize collection and access; define redaction, retention, deletion, sharing, and logging rules.
4. Review uploads, transcripts, backups, telemetry, generated reports, and external recipients for unnecessary exposure.
5. State residual risks, unknown system behavior, and verification steps. Do not claim legal or regulatory compliance from a checklist alone.

## Guardrails

Do not delete, export, alter, disclose, or redact user data automatically. Preserve required safety or audit records under the authorized policy. Never expose secrets or infer sensitive attributes.

## Output contract

Return data inventory, purpose and necessity decision, access and sharing boundaries, retention and deletion plan, redaction rules, residual risks, and approvals needed.

## Skip when

- No personal, confidential, sensitive, stored, logged, uploaded, or shared data is involved.
- The task is a conceptual answer with no data-handling workflow.
- No meaningful privacy decision or lifecycle change is being made.
