---
description: Analyze retention curves, identify churn drivers, and recommend interventions using cohort analysis
argument-hint: "<product or user segment>"
---

# /retention-analysis -- Retention Analysis

Analyze your retention curve shape, identify the biggest drop-off, compare retained vs. churned user behavior, and produce a prioritized list of interventions.

## Invocation

```
/retention-analysis   → Provide retention data or I'll query your analytics MCP
```

## Brain Context

Load if available:
- `brain/knowledge/product/metrics.md` — D1, D7, D14, D30 retention rates and cohort data
- `brain/knowledge/users/insights.md` — churn research, user quotes about why they stopped
- `brain/knowledge/product/features/` — features built to improve retention (avoid re-proposing)
- `brain/knowledge/strategy.md` — whether retention is a declared strategic priority this quarter
- `brain/style/frameworks.md` — preferred analysis format
- Recent `brain/ingestion/` — CS feedback, support tickets, exit survey signals

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/product/metrics.md` for retention baselines and cohort history. Load user insights for qualitative churn signals — these explain the "why" behind the retention curve shape. Check existing feature history to avoid recommending interventions already tried.

### Step 2: Apply the Skill

Apply the **retention-analysis** skill.

Use brain metrics as the quantitative input. Use churn interview quotes from ingestion to annotate each drop-off point with user-voiced reasons. Reference past retention features to calibrate which intervention types have already been explored.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-retention-analysis.md`.

### Step 4: Offer Follow-ups

- "Run `/ingest` to promote retention findings into your brain."
- "Early activation issues contributing to churn? Run `/activation-analysis`."
- "Expansion opportunity for retained power users? Run `/expansion-strategy`."
- "Ready to test a retention intervention? Run `/hypothesize` or `/prd-draft`."
