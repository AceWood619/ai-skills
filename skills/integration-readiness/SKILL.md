---
name: integration-readiness
description: Preflight connectors, plugins, MCP servers, and APIs for availability, authorization, scope, health, and operation-specific readiness before use. Use before first integration use, after configuration changes, or when a tool reports unavailable or unauthorized.
---

# Integration Readiness

Treat readiness as operation-specific evidence, not a label inferred from a catalog entry.

## Workflow

1. Identify the exact integration, operation, data scope, side effects, and required read/write authority.
2. Verify the capability is listed, enabled, authorized, minimally scoped, and healthy using actual platform metadata and tool definitions.
3. Distinguish ready, listed-disabled, unauthorized, insufficient-scope, unhealthy, unavailable, and unknown.
4. For blocked states, state the exact remediation without inventing credentials, scopes, health signals, or tools.
5. Gate writes and consequential actions behind the required authorization and confirmation; test the smallest safe read when appropriate.
6. Record the evidence and recheck after setup or authorization changes.

## Guardrails

Never bypass consent, login, scope restrictions, certificate or health failures. Never print, store, or infer secrets. Unknown status means not ready.

## Output contract

Return integration, operation, status, evidence, required scope, authorization state, blocker or remediation, confirmation requirement, and next safe check.

## Skip when

- No plugin, connector, API, MCP server, or external tool is involved.
- The task is a conceptual answer with no intended integration use.
- The operation and its required scope are already explicit and verified.
