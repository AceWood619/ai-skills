---
name: autonomous-skill-evolution
description: Run a complete, controlled skill-evolution cycle — audit existing skills, discover a reusable capability gap, develop a new or improved skill with skill-creator, validate and smoke-test it, install it, and report evidence. Use when the user asks to evolve skills autonomously, discover advanced capabilities, or turn a successful workflow into a reusable skill.
---

# Autonomous Skill Evolution

Run the full capability-engineering loop below. Use autonomy for reversible local work, but keep permissions, credentials, external publication, billing, device control, and protected submissions outside the skill’s authority.

## Cycle

1. **Read the authorities.** Read `/root/.grok/skills/skill-creator/SKILL.md` and `/home/workdir/.grok/skills/skill-evolution/SKILL.md` before modifying the registry.
2. **Baseline.** Run `python /home/workdir/.grok/skills/skill-evolution/scripts/audit_skills.py --json`. Record the skill count, invalid packages, duplicates, warnings, and relevant existing coverage.
3. **Discover the gap.** Search skill metadata and references for the requested capability. Prefer an existing skill, a small additive reference/script, or composition before creating a package. Create a new skill only when the gap is distinct, reusable, and has an observable acceptance test.
4. **Specify.** Write a short acceptance record — gap, trigger, skip cases, non-goals, safety boundary, expected resources, and tests. Choose a hyphen-case name that does not collide with the registry.
5. **Develop.** Use skill-creator init scripts or create `/home/workdir/.grok/skills/<name>/` with a valid `SKILL.md`. Replace placeholders with a concise body; add only necessary scripts, references, or templates; remove unused examples. Keep the body below 500 lines and link references directly.
6. **Test the candidate.** Validate frontmatter and structure, compile and execute every bundled script with safe representative inputs, verify referenced files, and test at least one negative path when the skill performs validation or mutation.
7. **Install safely.** Copy only a passing package into `/home/workdir/.grok/skills/<name>/`. Never overwrite an unrelated skill. If improving an existing skill, preserve a backup and revalidate the final directory.
8. **Smoke-test end to end.** Re-run the full registry audit, execute targeted workflow-contract checks, and confirm no invalid packages or duplicate names. Treat a failed check as a defect — make one focused change, then rerun the affected and full checks.
9. **Report evidence.** State the gap, files changed, tests and exact results, installed status, limitations, warnings, and the next signal that would justify another iteration.

## Acceptance gates

Do not call the cycle complete unless the candidate has valid frontmatter with a trigger-focused description, clear skip cases, no unfinished placeholders, no permission escalation, a concrete workflow contract, and passing validation. A script-bearing skill must also compile and pass both positive and negative-path tests. The final registry audit must report zero invalid packages and zero duplicate names.

## Safe discovery

Inspect third-party bundles before installation. Reject hidden executables, credential requests, permission-changing instructions, and destructive install steps. Use external sources only when local capabilities are insufficient, and read the relevant official guidance before implementation. Do not create a skill recursively just because this cycle skill triggered; require a distinct reusable gap.

## Output format

For each cycle, return:

| Field | Evidence |
|---|---|
| Gap and trigger | What was missing and when the new skill activates |
| Change | Package and resources added or modified |
| Tests | Commands or representative scenarios with results |
| Registry state | Count, invalid packages, duplicates, and warnings |
| Safety boundary | Actions the skill does not authorize |
| Next signal | What future failure or recurring task would justify iteration |

## Skip when

- The request is a one-off task already handled by an existing skill.
- No recurring capability gap or observable acceptance test exists.
- The proposed change would require new authority rather than reusable reasoning, documentation, or local tooling.
