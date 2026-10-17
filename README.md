# AI Skills

Reusable, privacy-safe skills for Claude (and other agents that read `SKILL.md`, e.g. OpenClaw).
Each folder in `skills/` is one skill: a `SKILL.md` with `name` + `description` frontmatter, plus optional `scripts/` and `references/`.

**Public repo rule:** nothing here contains personal data, home addresses, IPs, tokens, or household specifics. Personal/household skills live in a separate private repo.

## Install
- **Claude Code:** copy a skill folder into `~/.claude/skills/` (personal) or `.claude/skills/` (project).
- **Claude app:** zip a skill folder and upload it under Settings → Capabilities → Skills.
- **OpenClaw:** copy into `~/.openclaw/state/skills/`.

## Skills (27)
| Skill | What it's for |
|---|---|
| `adversarial-self-critique` | Attack your own reasoning on high-stakes or contested answers, then fix the answer before showing it. Use when… |
| `agent-creator` | Design custom AI agents with clear roles, tools, memory, guardrails, and evaluation criteria. Use when the use… |
| `agent-evaluation` | Evaluate custom AI agents, personas, prompts, and skills with repeatable test cases, rubrics, safety checks, a… |
| `api-contract-review` | Review OpenAPI or Swagger JSON contracts for breaking changes, compatibility risks, missing documentation, and… |
| `automation-reliability` | Design and review reliable schedules, triggers, retries, idempotency, alerts, recovery, and failure handling f… |
| `autonomous-skill-evolution` | Run a complete, controlled skill-evolution cycle — audit existing skills, discover a reusable capability gap… |
| `backup-restore-verification` | Verify backup freshness, coverage, integrity, restore procedures, recovery objectives, and restoration evidenc… |
| `capability-discovery-router` | Discover installed skills, plugins, MCP servers, tools, and connectors, match them to a task, reuse the best a… |
| `causal-reasoning` | Apply disciplined causal thinking that scales with stakes. Use when the user asks why something happened, whet… |
| `data-pipeline-validation` | Validate CSV, JSON, and tabular pipeline inputs and outputs for schema correctness, nulls, uniqueness, invaria… |
| `dependency-risk-management` | Inventory direct and transitive dependencies, assess version, provenance, lifecycle, compatibility, and upgrad… |
| `documentation-quality` | Audit operational documentation for completeness, freshness, runnable examples, ownership, review dates, and d… |
| `epistemic-hygiene` | Apply calibrated epistemic standards that scale with stakes: label guesses as guesses, state confidence and wh… |
| `esphome-flash-budget-ble` | Fit Bluetooth LE presence scanning onto a flash-limited ESP32 ESPHome node (e.g. ESP32-C6 with voice/wake word… |
| `integration-readiness` | Preflight connectors, plugins, MCP servers, and APIs for availability, authorization, scope, health, and opera… |
| `knowledge-capture` | Turn successful work, decisions, failures, and reusable procedures into reviewable references, templates, or s… |
| `long-horizon-planner` | Structure multi-step projects with milestones, risks, review points, and exit criteria. Use for anything spann… |
| `metacognitive-monitoring` | Monitor reasoning and execution quality through explicit goals, assumptions, predictions, confidence, checkpoi… |
| `multi-source-synthesis` | Turn multiple sources into a structured synthesis with confidence levels and explicit conflict handling. Use f… |
| `observability-incident-diagnosis` | Diagnose failures in agents, automations, APIs, scripts, websites, and integrations using timelines, evidence,… |
| `privacy-data-minimization` | Minimize collected data, retention, sharing, logging, uploads, exports, and redaction risk across workflows. U… |
| `project-decision-records` | Create and maintain portable project decision records containing context, assumptions, alternatives, evidence,… |
| `prompt-context-optimization` | Optimize prompts, context windows, skill triggers, and instruction conflicts without weakening safety or user … |
| `release-quality-gates` | Design and run release quality gates for skills, agents, APIs, scripts, websites, and automations. Use for pre… |
| `safe-home-assistant-operations` | Plan and review safe Home Assistant and smart-home device operations with explicit permission boundaries, acti… |
| `security-privacy-review` | Review skills, agents, scripts, automations, APIs, and integrations for credential exposure, excessive permiss… |
| `skill-evolution` | Discover missing capabilities, create or improve reusable skills, validate and smoke-test them, and iterate fr… |

## Contributing a new skill
1. `skills/<kebab-name>/SKILL.md` with frontmatter `name` and a `description` that says *when* to use it.
2. Run `for f in skills/<kebab-name>/*; do python3 skills/security-privacy-review/scripts/scan_text.py "$f"; done` to confirm no personal data.
3. Keep scripts read-only/offline unless the skill clearly says otherwise.

Origins: most skills were drafted with Grok, then deduplicated (newest version kept) and reviewed for Claude format and privacy; `esphome-flash-budget-ble` came from a real ESP32-C6 build.
