---
name: safe-home-assistant-operations
description: Plan and review safe Home Assistant and smart-home device operations with explicit permission boundaries, action classification, confirmation gates, rollback, and auditability. Use when inspecting or changing lights, locks, alarms, climate, cameras, routines, or other connected devices.
---

# Safe Home Assistant Operations

Keep reasoning, inspection, and device control as separate layers. A diagnosis or skill never grants device permissions.

## Workflow

1. Identify the target entity, requested action, affected people or property, current state, and user’s explicit intent.
2. Classify the action as read-only, reversible low-impact, sensitive, safety-relevant, security-relevant, or destructive.
3. Check authorization, scope, timing, dependencies, current state, and failure fallback. Prefer read-only inspection first.
4. For sensitive, security, safety, access, privacy, or spending actions, present the exact action and obtain the required confirmation before execution.
5. Execute only through an explicit authorized device-control tool. Never infer control authority from a reasoning skill, conversation context, or successful diagnosis.
6. Verify the resulting state, report what changed, and retain an audit-friendly record. If verification fails, stop and escalate rather than repeating blindly.

Use `scripts/classify_action.py` to classify proposed actions and identify whether confirmation is required. It does not control devices.

## Guardrails

Never unlock doors, disarm alarms, disable safety systems, expose cameras, change access, or spend money without explicit authority and the required confirmation. Do not guess entity IDs or silently substitute a different device.

## Output contract

Return target, action class, authorization status, confirmation requirement, exact proposed operation, verification step, fallback, and result.

## Skip when

- The task is unrelated to a connected device or Home Assistant.
- The user only wants a general explanation with no proposed operation.
- The action is already completed and only a harmless summary is requested.
