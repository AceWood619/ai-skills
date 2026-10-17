---
name: prompt-context-optimization
description: Optimize prompts, context windows, skill triggers, and instruction conflicts without weakening safety or user requirements. Use when revising agent prompts, debugging context loss, resolving instruction conflicts, or preparing prompt changes for evaluation.
---

# Prompt and Context Optimization

Preserve the constraints that matter while reducing noise, ambiguity, and trigger overlap.

## Workflow

1. Extract the goal, hard constraints, permissions, safety rules, output contract, and success test.
2. Classify context as required, useful, redundant, stale, untrusted data, or conflicting instruction.
3. Resolve conflicts by authority and scope; surface irreconcilable conflicts instead of silently choosing.
4. Compress repeated material only after preserving provenance and edge cases. Prefer direct trigger descriptions and progressive disclosure.
5. Test normal, ambiguous, adversarial, overlong-context, and missing-data cases. Compare before and after behavior.
6. Record what was removed, why it was safe to remove, and which regression test protects it.

## Guardrails

Never delete, weaken, or reinterpret safety constraints, permissions, privacy limits, or explicit user requirements. Do not expose private chain-of-thought. A shorter prompt is not automatically a better prompt.

## Output contract

Return retained constraints, removed context with rationale, conflict resolutions, trigger changes, regression results, and residual risks.

## Skip when

- The task is ordinary writing with no prompt, context, or routing design.
- The user wants a quick answer and no context failure is present.
- No observable behavior or acceptance test can be defined.
