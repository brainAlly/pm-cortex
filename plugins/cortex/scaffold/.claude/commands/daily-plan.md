---
description: Generate a context-aware daily plan pulled from your brain, active PRDs, and weekly priorities
argument-hint: "[full] [tomorrow]"
---

# /daily-plan -- Daily Plan

Start your day with a prioritized plan that pulls together meetings, tasks, active PRDs, and stakeholder context from your brain.

## Invocation

```
/daily-plan              → Compact plan (TL;DR + Top 3 + Schedule + Heads Up)
/daily-plan full         → Full plan with all sections
/daily-plan tomorrow     → Evening preview of tomorrow
```

## Brain Context

Load if available:
- `brain/knowledge/strategy.md` — quarter priorities and North Star to anchor Today's Three
- `brain/knowledge/product/roadmap.md` — active PRDs and their stages, **and the `§ Now` work table** (open items with an owner and due date — these are live candidates for Today's Three, especially anything due soon or overdue)
- `brain/knowledge/users/insights.md` — user context for meeting prep
- `brain/stakeholders/<slug>.md` for each person in today's meetings — open asks, communication style, last interaction
- `brain/style/writing.md` and `brain/style/patterns.md` — output format preferences
- `brain/decisions/` — recent decisions that may affect today's priorities
- Recent `brain/ingestion/meetings/` — carry-over items from yesterday
- `rules/prioritization.md` — team-specific prioritization norms (if present)

## Workflow

### Step 1: Load Brain Context

Check `outputs/daily-plans/` for an existing plan from today. If found, offer to update, replace, or keep it.

Load `brain/knowledge/strategy.md` for quarter goals and `brain/knowledge/product/roadmap.md` for active PRD stages and the `§ Now` work table. These anchor "Today's Three." Pull open `Now` rows owned by the PM — surface any that are due today or overdue before generic backlog items, so work that `/review` converted from a finding doesn't sit untouched.

Load `rules/prioritization.md` for team-specific LNO norms — it may define which task categories are always Overhead for this PM or set a different Leverage threshold.

### Step 2: Apply the Skill

Apply the **daily-plan** skill.

Use stakeholder profiles for meeting attendee context. Use brain knowledge to anchor priorities to strategic goals rather than generating generic advice.

### Step 3: Save Output

Save to `outputs/daily-plans/<YYYY-MM-DD>-daily-plan.md`.

### Step 4: Offer Follow-ups

- "Need meeting prep for a specific meeting? Run `/meeting-agenda`."
- "Want to convert action items to tickets? Run `/create-tickets`."
- "This week isn't planned yet — run `/weekly-plan` to set priorities."
- "Run `/ingest` after your meetings to capture outcomes into your brain."
