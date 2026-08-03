---
description: Classify tasks using the LNO Framework and build a focused weekly plan with calendar blocking
argument-hint: "<paste task list or calendar>"
---

# /prioritize -- Prioritize Tasks

Classify every task as Leverage (10x), Neutral (1x), or Overhead (<1x). Calculate your L/N/O distribution, eliminate the overhead, and build a calendar-blocked weekly plan.

## Invocation

```
/prioritize   → Paste your task list or calendar; I'll classify and plan
```

## Brain Context

Load if available:
- `brain/knowledge/strategy.md` — quarter priorities and OKRs to validate which tasks are actually Leverage vs. perceived Leverage
- `brain/style/frameworks.md` — preferred prioritization formats
- `rules/prioritization.md` — team-specific prioritization norms (if present)

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/strategy.md` to cross-reference each task against declared strategic priorities. A task that feels important but doesn't connect to a quarter goal is probably Neutral or Overhead, not Leverage.

Load `rules/prioritization.md` for team-specific norms — it may define custom LNO thresholds or override default classification rules for this PM's context.

### Step 2: Apply the Skill

Apply the **prioritize** skill.

Use strategy context to validate Leverage classifications. Flag tasks that are consuming time but not advancing any declared goal. Surface the L/N/O percentage distribution and compare against the 40/35/20 target.

### Step 3: Output

Display the classified task list and weekly plan inline. Offer to save to `outputs/<YYYY-MM-DD>-prioritized-tasks.md` if the user wants a reference copy.

### Step 4: Offer Follow-ups

- "Ready to formalize this into a weekly plan? Run `/weekly-plan`."
- "Want to execute day by day? Run `/daily-plan` each morning."
- "Overhead tasks that can become tickets? Run `/create-tickets` to hand them off."
