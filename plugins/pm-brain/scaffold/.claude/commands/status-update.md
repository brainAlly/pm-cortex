---
description: Generate stakeholder status updates for different audiences from your brain context
argument-hint: "<weekly|daily|exec> for <audience>"
---

# /status-update -- Status Update

Create status updates that communicate progress, surface blockers, and keep stakeholders aligned. Auto-pulls from brain context so you don't re-explain what's already captured.

## Invocation

```
/status-update weekly for my manager       → Manager 1:1 prep format
/status-update weekly for exec             → Executive summary format
/status-update daily                       → Async standup format
/status-update                             → I'll ask period and audience
```

## Brain Context

Load if available:
- `brain/knowledge/strategy.md` — to tie accomplishments to strategic pillars and OKRs
- `brain/style/writing.md` — your voice and format preferences
- Recent `brain/ingestion/meetings/` — decisions and action items completed this week
- `brain/stakeholders/<audience-slug>.md` — audience's communication preferences (BLUF for execs, detailed for manager)
- `brain/knowledge/product/roadmap.md` — feature status and milestone progress
- `brain/decisions/` — key decisions made in the period to surface

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/strategy.md` to frame accomplishments against strategic goals. Load the audience's stakeholder profile to calibrate tone and format. Scan recent `brain/ingestion/meetings/` for completed action items and decisions made.

### Step 2: Apply the Skill

Apply the **status-update** skill.

Use brain context to auto-populate completed work, in-flight items, and blockers. Tie each accomplishment to a strategic pillar or OKR. Use the audience's communication style to select the right format (exec summary, team update, or standup).

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-status-update-<audience>.md`.

### Step 4: Offer Follow-ups

- "Want to share this on Slack? Run `/slack-message` with the update as context."
- "Blocker needs escalation? Run `/slack-message` targeting the right person."
- "Run `/ingest` to log this period's decisions and progress into your brain."
