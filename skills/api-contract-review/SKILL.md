---
name: api-contract-review
description: Review OpenAPI or Swagger JSON contracts for breaking changes, compatibility risks, missing documentation, and release-gate evidence. Use when comparing API specifications, reviewing endpoint changes, planning version upgrades, or validating a contract before release.
---

# API Contract Review

Review an API contract as a compatibility boundary between producers and consumers. Prefer the smallest evidence-backed report over a vague list of possible concerns.

## Workflow

1. **Identify the contract.** Confirm the specification format and version, the baseline and proposed documents, affected consumers, compatibility policy, and whether the check is for breaking changes, quality, or both.
2. **Normalize the comparison.** Resolve `$ref` only when needed, compare paths and operations by method, and preserve whether a difference is additive, behavioral, or removal. Do not infer runtime behavior that the specification does not show.
3. **Check compatibility.** Flag removed paths or operations, removed parameters, newly required parameters, incompatible request changes, removed response status codes, and response fields that became required or changed type. Treat additive optional fields as usually compatible, subject to the consumer’s deserializer policy.
4. **Check contract quality.** Look for missing operation summaries, undocumented error responses, absent parameter descriptions, ambiguous schemas, and inconsistent version or security declarations.
5. **Classify findings.** Use `breaking`, `risky`, `quality`, or `informational`; include location, baseline value, proposed value, affected consumer assumption, and a remediation.
6. **Gate the release.** Recommend `block`, `review`, or `pass`. A release gate must be based on the stated compatibility policy, not on confidence alone.
7. **Report uncertainty.** Name unresolved `$ref`s, behavior that requires integration tests, and assumptions about generated clients or tolerant readers.

Use `scripts/review_openapi.py` for a deterministic first-pass JSON diff. It detects high-signal structural changes; it does not replace runtime integration tests, semantic versioning policy, or human review of business behavior.

## Output contract

Return:

- **Scope and policy**
- **Decision**: block, review, or pass
- **Findings**: severity, location, baseline → proposed, impact, remediation
- **Compatibility assumptions**
- **Tests still needed**

## Safety and limits

This skill only analyzes local or user-provided specifications. It does not publish a contract, change production routes, access credentials, call customer systems, or approve a release on the user’s behalf.

## Skip when

- The user needs runtime debugging rather than contract comparison.
- No baseline, proposed contract, or concrete API behavior is available.
- The task is only to format or summarize an unchanged document.
