---
name: agent-evaluation
description: Evaluate custom AI agents, personas, prompts, and skills with repeatable test cases, rubrics, safety checks, and regression comparisons. Use when testing an agent before release, comparing prompt or skill changes, red-teaming behavior, or measuring answer quality.
---

# Agent Evaluation

Evaluate behavior against explicit expectations rather than judging an agent by a few impressive examples.

## Workflow

1. Define the agent’s scope, tools, non-goals, risk level, and success metrics.
2. Build a test matrix covering normal use, ambiguity, missing data, adversarial instructions, permission boundaries, and refusal or escalation cases.
3. Specify observable assertions: required concepts, forbidden claims or actions, uncertainty behavior, tool choice, format, latency, and safety.
4. Run a baseline and the candidate under the same cases. Keep inputs, context, model settings, and scoring rules stable.
5. Score each case as pass, partial, or fail; preserve the failing output and identify the smallest likely cause.
6. Change one prompt, skill, tool rule, or test assumption at a time. Rerun affected cases and the regression suite.
7. Release only when critical safety cases pass and quality changes are understood.

Use `scripts/evaluate_cases.py` for deterministic text assertions. It is a smoke test, not a substitute for human judgment or model-quality evaluation.

## Output contract

Return the test scope, rubric, per-case results, regressions, safety failures, confidence, and release recommendation: pass, review, or block.

## Guardrails

Never treat a passing test as permission to access data, control devices, submit records, spend money, or publish externally. Keep secrets out of fixtures and redact sensitive outputs.

## Skip when

- The task is a one-off answer with no reusable agent behavior.
- No expected behavior or acceptance criterion can be stated.
- The user wants creative exploration rather than evaluation.
