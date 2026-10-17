---
name: security-privacy-review
description: Review skills, agents, scripts, automations, APIs, and integrations for credential exposure, excessive permissions, data leakage, prompt injection, destructive behavior, and unsafe defaults. Use before installing untrusted bundles, enabling integrations, publishing software, or changing security-sensitive workflows.
---

# Security and Privacy Review

Find concrete security and privacy risks, explain impact, and recommend the least-privilege fix.

## Workflow

1. Define assets, actors, trust boundaries, data sensitivity, and intended authority.
2. Inventory files, tools, secrets, network calls, external actions, persistence, and user-controlled inputs.
3. Check authentication, authorization, least privilege, injection paths, logging, retention, encryption assumptions, and failure behavior.
4. Search for hard-coded secrets, unsafe shell commands, permission changes, hidden executables, broad data collection, and unreviewed outbound transmission.
5. Classify findings as critical, high, medium, low, or informational; include evidence, exploit or exposure path, affected asset, and mitigation.
6. Verify fixes with a focused retest and document residual risk. Block installation or release when a critical issue is unresolved.

Use `scripts/scan_text.py` for a conservative first-pass scan of local text artifacts. Review findings manually to distinguish examples from executable behavior.

## Guardrails

Do not attempt exploitation, bypass access controls, collect secrets, or make security changes without explicit authority. Redact credentials in reports and never print their values.

## Output contract

Return scope, trust boundaries, findings with evidence and severity, mitigations, residual risk, and a pass, review, or block recommendation.

## Skip when

- The task contains no code, data, integration, automation, or permission boundary.
- The user requests offensive exploitation rather than defensive review.
- A simple formatting or content edit has no security impact.
