---
description: Set next week's Top 3 priorities aligned with quarter goals and active PRD pipeline
argument-hint: "[next]"
---

# /weekly-plan -- Weekly Plan

Plan the week ahead with clear priorities tied to quarterly goals, active PRDs, and meeting load.

## Invocation

```
/weekly-plan        → Plan upcoming week (or current week if Monday)
/weekly-plan next   → Explicitly plan next week (when running on Friday)
```

## Brain Context

Load if available:
- `brain/knowledge/strategy.md` — OKRs, North Star, and strategic pillars to anchor Top 3
- `brain/knowledge/product/roadmap.md` — active PRDs and pipeline stages
- `brain/style/writing.md` and `brain/style/patterns.md` — output format preferences
- Recent `outputs/weekly-reviews/` — carry-over items and learnings from last week
- `brain/decisions/` — recent committed decisions that affect this week's priorities
- `rules/prioritization.md` — team-specific prioritization norms (if present)

## Workflow

### Step 1: Load Brain Context

Check `outputs/weekly-plans/` for an existing plan for the target week. If found, offer to update or replace.

Load `brain/knowledge/strategy.md` to anchor priorities to quarter goals. Load `brain/knowledge/product/roadmap.md` to identify which PRDs need to advance this week.

Load `rules/prioritization.md` for team-specific LNO norms that govern which weekly priorities count as Leverage vs. Neutral.

### Step 2: Apply the Skill

Apply the **weekly-plan** skill.

Use brain strategy context to validate that each priority advances a declared goal. Use PRD pipeline to surface stage-blocking work. Reference last week's review to surface carry-overs.

### Step 3: Save Output

Save to `outputs/weekly-plans/<YYYY-WXX>-weekly-plan.md`.

### Step 4: Offer Follow-ups

- "Ready to start the week? Run `/daily-plan` each morning to execute."
- "Want to convert priorities into tickets? Run `/create-tickets`."
- "Want to share this plan with your team? Run `/slack-message`."
- "Run `/ingest` to log this week's priorities into your brain."
