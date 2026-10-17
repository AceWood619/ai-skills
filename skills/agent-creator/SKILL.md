---
name: agent-creator
description: Design custom AI agents with clear roles, tools, memory, guardrails, and evaluation criteria. Use when the user wants a specialist agent, system prompt, multi-agent setup, or formal persona, including Home Assistant or Jarvis voice agents. Skip for ordinary Q&A.
---

# Agent Creator

Produce a complete, portable agent specification.

## Required Sections

1. **Identity**  
   Name, one-sentence purpose, communication style.

2. **Scope**  
   Responsibilities + explicit non-goals.

3. **Capabilities & Tools**  
   Allowed tools and data sources.  
   Required reasoning skills.  
   Memory strategy.

4. **Reasoning Standards**  
   Which skills are mandatory (epistemic-hygiene, causal-reasoning, etc.).  
   When to escalate or ask clarifying questions.

5. **Output Contracts**  
   Structure, evidence requirements, uncertainty rules.  
   **Voice note**: If the agent will speak (Jarvis / Home Assistant / phone), answers must be short, linear, and free of heavy formatting.

6. **Guardrails**  
   Hard constraints (safety, privacy, legal).  
   Soft preferences.  
   Failure modes and recovery.

7. **Critical Rule**  
   A reasoning skill never grants device or Home Assistant permissions.  
   Reasoning protocols and device control are separate layers.  
   An agent may use causal-reasoning to diagnose a light failure; it may not turn the light on unless it also has an explicit device-control tool.

8. **Evaluation**  
   Success metrics + red-team tests the agent must pass.

## Output Format

Ready-to-paste system prompt  
+ list of required skills  
+ short evaluation checklist  

A fill-in template lives in `references/agent-template.md`.

## Skip when

- The user only wants a quick answer or ordinary Q&A, not a formal agent specification.
- The request is a one-off prompt tweak with no role, tools, memory, or evaluation requirements.
- Device control or Home Assistant permissions are requested without a separate authorized control path — do not grant them via this skill.
