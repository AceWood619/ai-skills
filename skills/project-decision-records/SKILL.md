---
name: project-decision-records
description: Create and maintain portable project decision records containing context, assumptions, alternatives, evidence, consequences, owners, review conditions, and reversal history. Use for material trade-offs, disputed assumptions, cross-team choices, or hard-to-reverse decisions.
---

# Project Decision Records

Make important decisions auditable without pretending that a record is authorization to act.

## Workflow

1. Record decision status, date, owner, context, success condition, and constraints.
2. Separate facts, assumptions, recommendations, and the final decision.
3. List alternatives considered and why they were rejected; cite evidence and confidence.
4. Record consequences, risks, dependencies, dissent, review date or trigger, and follow-up owner.
5. When assumptions change, create a supersession or reversal entry rather than erasing history.
6. Verify that no evidence, approval, date, or rationale was invented.

## Guardrails

Do not silently approve, execute, publish, reverse, or delete decisions. Require the actual decision owner for consequential changes and flag legal, safety, security, financial, or compliance matters for human review.

## Output contract

Return a concise record with status, context, decision, alternatives, evidence, assumptions, consequences, owner, review condition, and supersession links.

## Skip when

- The choice is trivial, reversible, and has no meaningful downstream impact.
- No real decision or owner exists yet.
- The user only wants brainstorming without a decision record.
