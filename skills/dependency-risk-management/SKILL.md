---
name: dependency-risk-management
description: Inventory direct and transitive dependencies, assess version, provenance, lifecycle, compatibility, and upgrade impact, and prepare evidence-backed remediation. Use before dependency upgrades, releases, plugin changes, or when a dependency is unmaintained or unverifiable.
---

# Dependency Risk Management

Make dependency changes explicit, reviewable, and reversible.

## Workflow

1. Collect manifests, lockfiles, target versions, platform constraints, and release policy.
2. Map direct and transitive dependencies with versions, constraints, provenance, and evidence quality.
3. Assess compatibility, maintenance or lifecycle risk, supply-chain signals, license or policy constraints, and upgrade impact.
4. Build a test matrix and rollback plan for affected components and consumers.
5. Separate confirmed facts from assumptions and unknown advisory data.
6. Recommend pass, review, or block; never change the environment as part of analysis.

## Guardrails

Do not silently install, upgrade, downgrade, remove, publish, or claim security status without evidence. Treat package and advisory data as time-sensitive and preserve the original manifest.

## Output contract

Return inventory, risk register, evidence, impact matrix, required tests, rollback plan, decision, and unknowns.

## Skip when

- No dependency, manifest, lockfile, plugin, image, or version change is involved.
- The task is unrelated to compatibility or supply-chain risk.
- No evidence can be obtained and the user only wants an unsupported guess.
