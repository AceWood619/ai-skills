---
name: causal-reasoning
description: "Apply disciplined causal thinking that scales with stakes. Use when the user asks why something happened, whether X causes Y, what will happen if they change something, or why a system is failing (automations, devices, business results), and whenever correlation is being treated as causation. Skip for pure description, prediction-only questions, and casual conversation."
---

# Causal Reasoning

Never treat association as causation without justification.

## Stakes Scaling

- **Low**: One sentence distinguishing association from causation is enough.
- **Medium / High**: Use the full checklist.

## Core Checklist

1. State the causal question precisely  
   Population, time frame, intervention vs observation.

2. Mental causal graph  
   Confounders, mediators, colliders, reverse causation.

3. Evidence ladder (strongest first)  
   1. RCT or strong natural experiment  
   2. IV / RD / DiD with solid justification  
   3. Longitudinal with careful controls  
   4. Cross-sectional with extensive controls  
   5. Simple correlation

4. Required questions  
   - Mechanism?  
   - Best alternative explanations?  
   - Sensitivity to unmeasured confounding?  
   - Is the effect size practically meaningful?

5. Troubleshooting loop (for diagnosis / home systems / debugging)  
   Change only one variable at a time. Observe. Record. Then change the next. Never multi-change when seeking cause.

## High-Stakes Output Shape

**Causal question**  
**Proposed mechanism**  
**Strongest evidence** (design + result)  
**Main threats to validity**  
**Best current estimate** + uncertainty  
**What would most change this view**

## Skip When

- User only wants prediction, not explanation  
- Pure descriptive statistics  
- Creative or speculative brainstorming
