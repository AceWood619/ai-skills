---
name: metacognitive-monitoring
description: Monitor reasoning and execution quality through explicit goals, assumptions, predictions, confidence, checkpoints, error signals, and course correction. Use for complex or uncertain tasks, multi-step work, tool-heavy execution, decisions with meaningful downside, or when the user asks to reflect, calibrate, self-check, or improve the approach.
---

# Metacognitive Monitoring

Use this skill to manage the quality of thinking and execution while work is in progress. It complements domain skills; it does not replace evidence checks, causal analysis, adversarial critique, or explicit permissions.

## Guardrails

- Monitor the work, not private chain-of-thought. Report concise reasons, observable evidence, assumptions, and decisions rather than hidden deliberation.
- Separate **goal**, **plan**, **evidence**, **inference**, **uncertainty**, and **next action**.
- Never use confidence as permission. High confidence does not authorize a protected, external, irreversible, financial, medical, legal, or device action.
- Do not manufacture progress. Mark unknown, blocked, stale, or unverified states explicitly.
- Escalate when a missing fact could materially change the outcome, when evidence conflicts, or when the next step is hard to reverse.

## Core loop

1. **Frame.** State the desired outcome, constraints, non-goals, success test, and deadline or stopping point.
2. **Pre-mortem.** List the two or three assumptions most likely to fail. For each, state what observable signal would falsify it.
3. **Plan.** Choose the smallest reversible next action. Predict its expected result and what result would count as surprising.
4. **Execute and observe.** Record the actual result, evidence source, and deviations. Do not silently update the plan.
5. **Checkpoint.** Compare prediction with observation. Classify the state as on-track, uncertain, blocked, failed, or complete.
6. **Calibrate.** Reduce confidence when predictions fail, evidence is weak, or alternatives remain plausible. Increase it only when independent evidence converges.
7. **Course-correct.** Continue, revise one variable, seek missing information, pause, escalate, or stop. Prefer the smallest change that tests the suspected cause.
8. **Close.** Verify the success test, name residual uncertainty, capture the reusable lesson, and state what would trigger a later review.

## Checkpoint contract

At each meaningful boundary, maintain:

- **Goal and success test**
- **Current state**: on-track, uncertain, blocked, failed, or complete
- **Prediction vs observation**
- **Evidence and source quality**
- **Assumptions at risk**
- **Confidence**: high, medium, or low, with a short reason
- **Next reversible action**
- **Stop or escalation condition**

Use `scripts/checkpoint.py` to validate a JSON checkpoint and surface missing fields or risk flags. Read its `--help` output when using it.

## Decision rules

- **Prediction error:** inspect the assumption that produced the prediction before adding more steps.
- **Repeated failure:** after two materially similar failed attempts, stop repeating the same approach; change the hypothesis, tool, or scope.
- **Scope drift:** compare new work with the original success test; drop attractive work that does not serve it.
- **Uncertainty bottleneck:** identify the single fact or experiment with the highest value for reducing uncertainty.
- **Conflicting evidence:** preserve the disagreement, rank sources, and avoid a forced conclusion; use `multi-source-synthesis` or `epistemic-hygiene` when appropriate.
- **High downside:** pause before the consequential step and verify assumptions or request the required confirmation.
- **Completion:** stop when the success test is met or when the remaining work has lower value than its cost; state the reason.

## Interaction with other skills

- Use `epistemic-hygiene` for claim strength and confidence calibration.
- Use `causal-reasoning` for intervention, diagnosis, or troubleshooting questions.
- Use `adversarial-self-critique` when stakes or contested claims warrant an explicit challenge.
- Use `long-horizon-planner` when monitoring spans milestones or months.
- Use `skill-evolution` when the checkpoint reveals a recurring capability gap rather than a one-off mistake.

## Skip when

- The task is trivial, deterministic, and completed in one reversible step.
- The user explicitly wants a fast answer and no monitoring overhead is useful.
- There is no meaningful uncertainty, decision, execution sequence, or quality risk to monitor.

## Output contract

Keep checkpoints concise. For a live task, report only the current state, material deviation, confidence with reason, next action, and stop/escalation condition. For a completed task, add the success-test result, residual uncertainty, and one reusable lesson.
