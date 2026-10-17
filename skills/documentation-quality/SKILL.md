---
name: documentation-quality
description: Audit operational documentation for completeness, freshness, runnable examples, ownership, review dates, and discoverability. Use when reviewing runbooks, SOPs, API or operator guides, incident procedures, onboarding instructions, or documentation before release.
---

# Documentation Quality

Evaluate whether documentation can be found, trusted, and followed safely.

## Workflow

1. Define audience, operational purpose, criticality, source set, and version or freshness expectations.
2. Check prerequisites, scope, steps, inputs, outputs, examples, failure handling, safety notes, owner, review date, and links.
3. Verify examples or commands when safe and authorized; otherwise label them unverified.
4. Check discoverability from the workflow, service, or entry point the document supports.
5. Classify findings as block, review, or informational with evidence and remediation.
6. Recheck corrected documents without silently changing or publishing source content.

## Guardrails

Do not fabricate owners, dates, working examples, or operational guarantees. Minimize quoted sensitive content and escalate safety-critical, security, legal, or compliance procedures.

## Output contract

Return scope, documentation inventory, findings with evidence, severity, remediation, verification status, owner gaps, and release recommendation.

## Skip when

- No operational or reusable documentation is involved.
- The task is only formatting an unchanged document.
- No quality, freshness, safety, or discoverability judgment is requested.
