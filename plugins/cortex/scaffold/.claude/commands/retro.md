---
description: Run a structured retrospective — Start/Stop/Continue, 4Ls, or Sailboat format with brain write-back
argument-hint: "[format] <team feedback, sprint data, or retrospective notes>"
---

# /retro -- Retrospective Facilitator

Run a structured retrospective that produces actionable improvements. Use for any period — sprint, quarter, project, or initiative. For sprint-lifecycle retrospectives chained with planning and release notes, use `/sprint retro`.

## Invocation

```
/retro [paste team feedback or sprint data]
/retro start-stop-continue [feedback]
/retro 4ls [feedback]
/retro sailboat [feedback]
```

## Brain Context

Load if available:
- `brain/knowledge/product/roadmap.md` — what was committed this period
- `brain/knowledge/org/rituals.md` — prior retro commitments to check follow-through on
- `brain/hypotheses/INDEX.md` — hypotheses in progress this period
- `brain/ingestion/adhoc/` — most recent retro file, for prior commitment tracking
- `templates/retrospective-template.md` — output structure (if present)

## Workflow

### Step 1: Accept Input

Load `templates/retrospective-template.md` for the output structure before generating the retro summary.

Accept:
- Team feedback (pasted from survey, Slack, or collaborative doc)
- Sprint or period metrics (velocity, bugs, incidents)
- The user's own observations

Ask: "Which retro format do you prefer?"
- **Start/Stop/Continue** (simple, fast)
- **4Ls** (Liked, Learned, Lacked, Longed for)
- **Sailboat** (Wind = helps, Anchor = slows, Rocks = risks, Island = goals)

### Step 2: Check Prior Commitments

Load the most recent retro file from `brain/ingestion/adhoc/`. For each prior commitment:
- Followed through / not followed through / partially done

Do not carry forward a commitment for a third sprint without explicitly discussing it.

### Step 3: Analyze and Structure

Apply the **retro** skill:

- Categorize feedback into the chosen framework
- Identify themes and patterns
- Separate symptoms from root causes — push past symptoms to root causes for "didn't go well" items
- Highlight wins worth celebrating

### Step 4: Generate Retro Summary

```
## Retrospective: [Period/Sprint/Initiative]

**Date**: [today]
**Format**: [Start/Stop/Continue | 4Ls | Sailboat]
**Participants**: [if known]

### Prior Commitment Review
| Commitment | Status | Notes |
|-----------|--------|-------|

### What Went Well
[Grouped themes with supporting evidence]

### What Didn't Go Well
[Grouped themes with root cause — not symptom]

### Key Insights
[2-3 patterns that emerged]

### Action Items
| Action | Owner | Signal of Success |
|--------|-------|-----------------|

### Metrics This Period
| Metric | This Period | Last Period | Trend |
|--------|-----------|------------|-------|
```

Save to `outputs/<date>-retro-<slug>.md`.

### Step 5: Write to Brain

Auto-write a synthesis to `brain/ingestion/adhoc/<date>-retro-<slug>.md` containing:
- Period goal: hit / partial / missed + one-line explanation
- Top 3 process learnings
- Committed action items with owners

If any learning suggests a change to how the team works, flag: "This learning may warrant updating `brain/knowledge/org/rituals.md`. Update? (y/n)"

### Step 6: Offer Next Steps

- "Want me to **compare this to the last retro** for recurring patterns?"
- "Want me to **route recurring process problems to `/hypothesize`** as systemic hypotheses?"

## Notes

- Focus on 2-3 high-impact action items — not 10 things nobody will do
- Wins deserve as much time as problems — teams that only surface issues burn out
- If the same action item recurs across retros, that is a systemic issue worth `/hypothesize`-ing
