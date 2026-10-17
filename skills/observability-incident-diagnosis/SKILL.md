---
name: observability-incident-diagnosis
description: Diagnose failures in agents, automations, APIs, scripts, websites, and integrations using timelines, evidence, causal hypotheses, one-change tests, recovery steps, and post-incident learning. Use when a system is failing, behavior changed unexpectedly, or an incident needs a structured root-cause analysis.
---

# Observability and Incident Diagnosis

Separate symptoms from causes and turn incomplete logs into the next most informative safe test.

## Workflow

1. Establish impact, scope, start time, baseline behavior, and current state.
2. Build a timeline from logs, metrics, traces, user reports, deployments, configuration changes, and external dependencies. Mark timestamps and source quality.
3. State competing hypotheses with predictions and disconfirming evidence. Do not collapse correlation into cause.
4. Choose the smallest reversible test that distinguishes hypotheses. Change one variable at a time and record the result.
5. Contain safely, recover from a known-good state when necessary, and avoid destructive cleanup before evidence is preserved.
6. Confirm the fix with a regression check, then document root cause, contributing factors, detection gap, corrective actions, owner, and follow-up date.

Use `scripts/incident_report.py` to validate a structured incident record and flag missing evidence or recovery controls.

## Guardrails

Do not expose secrets in logs, delete evidence, restart critical systems without authority, or claim root cause from a single correlation. Escalate safety, security, financial, or data-loss incidents.

## Output contract

Return impact, timeline, hypotheses, evidence, test and result, containment, recovery, root cause confidence, corrective actions, and open questions.

## Skip when

- The task is descriptive and no failure or unexpected behavior exists.
- There is no observable system, event, or evidence to diagnose.
- The user wants a prediction rather than an explanation or troubleshooting plan.
