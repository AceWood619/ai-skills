---
name: data-pipeline-validation
description: Validate CSV, JSON, and tabular pipeline inputs and outputs for schema correctness, nulls, uniqueness, invariants, drift, and reproducibility. Use before publishing transformed data, accepting an export, or releasing a pipeline change.
---

# Data Pipeline Validation

Treat data transformations as contracts with explicit schemas, baselines, and evidence.

## Workflow

1. Identify inputs, outputs, schema or baseline, transformation, consumer, and acceptance thresholds.
2. Check types, required fields, nullability, uniqueness, row counts, ranges, aggregates, referential links, and invariants.
3. Compare distributions and schema against the declared baseline; report affected fields and measured deltas.
4. Rerun deterministic transformations and compare normalized outputs. Record inputs, parameters, versions, and timestamps.
5. Quarantine or report invalid data; do not silently coerce, drop, overwrite, or publish it.
6. Return pass, review, or block with evidence and the next remediation.

## Guardrails

Do not infer an authoritative schema from one sample, expose sensitive records in logs, or treat a successful parse as semantic correctness. Any coercion, row dropping, baseline update, or downstream release requires explicit approval.

## Output contract

Return scope, checks and thresholds, findings with affected fields, reproducibility evidence, decision, remediation, and unknowns.

## Skip when

- No structured data transformation or export is involved.
- The task is exploratory analysis without a correctness or release gate.
- No input/output or acceptance criterion is available.
