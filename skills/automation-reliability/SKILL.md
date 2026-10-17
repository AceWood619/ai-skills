---
name: automation-reliability
description: Design and review reliable schedules, triggers, retries, idempotency, alerts, recovery, and failure handling for unattended workflows. Use when an automation may duplicate work, miss runs, partially fail, or require production-grade recovery.
---

# Automation Reliability

Make unattended work observable, bounded, repeatable, and safe under retries and partial failure.

## Workflow

1. Define trigger, owner, delivery semantics, side effects, dependencies, and success signal.
2. Choose at-most-once or at-least-once behavior and define an idempotency key or deduplication strategy.
3. Bound retries, backoff, timeouts, concurrency, and terminal failure behavior.
4. Specify missed-run, partial-failure, dependency-outage, and recovery handling.
5. Add actionable alerts, escalation, runbook, audit evidence, disable control, and rollback path.
6. Test duplicate delivery, timeout, retry exhaustion, restart, and safe shutdown before release.

## Guardrails

Never claim delivery guarantees the platform does not provide. Treat retries as possible duplicate side effects. Do not create production, device-control, or external changes without the applicable authorization and confirmation.

## Output contract

Return a reliability design, failure matrix, idempotency plan, alert and runbook plan, test cases, rollback, and unresolved assumptions.

## Skip when

- The task is a one-off command with no unattended execution.
- No side effect, schedule, trigger, retry, or recovery behavior exists.
- The user only wants a simple reminder or conceptual explanation.
