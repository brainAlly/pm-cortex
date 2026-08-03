---
description: Synthesize the week's progress, wins, blockers, and learnings against the weekly plan
argument-hint: "[last-week]"
---

# /weekly-review -- Weekly Review

End-of-week synthesis comparing plan vs. actual, surfacing key wins, blockers, and learnings. Feeds into next week's planning and builds institutional memory.

## Invocation

```
/weekly-review            → Review current week (best run Friday afternoon)
/weekly-review last-week  → Review the previous week (if you missed Friday)
```

## Brain Context

Load if available:
- `brain/knowledge/strategy.md` — quarter goals to assess progress velocity
- `brain/knowledge/product/roadmap.md` — PRD pipeline to track stage movement
- `brain/decisions/` — decisions made this week to capture in the review
- Recent `outputs/weekly-plans/` — this week's intended priorities (plan vs. actual comparison)
- Recent `brain/ingestion/meetings/` — meeting outcomes and decisions from the week

## Workflow

### Step 1: Load Brain Context

Check `outputs/weekly-reviews/` for an existing review for this week. Load `brain/knowledge/strategy.md` to assess quarter progress velocity. Load this week's weekly plan from `outputs/weekly-plans/` for plan vs. actual comparison.

### Step 2: Apply the Skill

Apply the **weekly-review** skill.

Use strategy context to assess whether this week moved quarter goals forward. Reference the weekly plan for a direct plan vs. actual comparison on each priority. Surface PRD pipeline movement from `brain/knowledge/product/roadmap.md`.

### Step 3: Save Output

Save to `outputs/weekly-reviews/<YYYY-WXX>-weekly-review.md`.

After saving, offer: "Promote learnings and patterns to brain? Run `/ingest` on this review."

### Step 4: Offer Follow-ups

- "Ready to plan next week? Run `/weekly-plan`."
- "Want to share a summary with your team or manager? Run `/status-update`."
- "Run `/ingest` to route key learnings and decisions into your brain."
- "Run `/decide` if any decisions from this week need formal documentation."
