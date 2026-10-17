---
name: release-quality-gates
description: Design and run release quality gates for skills, agents, APIs, scripts, websites, and automations. Use for pre-release checklists, smoke and regression tests, compatibility review, artifact verification, rollback planning, or pass/review/block decisions.
---

# Release Quality Gates

Turn a change into an evidence-backed release decision with explicit rollback and ownership boundaries.

## Workflow

1. Define the release unit, intended change, version, dependencies, compatibility policy, and rollback target.
2. Build gates for syntax/package validity, unit or smoke tests, regression coverage, security review, data migration, compatibility, documentation, and artifact integrity.
3. Label each gate required, advisory, or not applicable; assign an owner and evidence location.
4. Run gates in cheap-to-expensive order. Stop early on a blocking failure and preserve logs.
5. Decide `pass`, `review`, or `block`; explain every override and unresolved risk.
6. Verify the exact artifact to release, record a rollback procedure, and define post-release signals and a review window.

Use `scripts/release_gate.py` to evaluate a JSON gate record deterministically.

## Guardrails

This skill prepares decisions; it does not publish, deploy, migrate production data, change billing, or approve a protected external submission without the required authority and confirmation.

## Output contract

Return release scope, gate table, failures and evidence, decision, rollback plan, post-release checks, and residual risk.

## Skip when

- No release, deployment, versioned artifact, or quality decision is involved.
- The task is a local draft with no downstream consumer.
- The user only wants brainstorming without a release recommendation.
