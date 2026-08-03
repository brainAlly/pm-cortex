---
description: Diagnose your activation funnel using the Setup → Aha → Habit framework and identify the biggest bottleneck
argument-hint: "<product or onboarding flow>"
---

# /activation-analysis -- Activation Analysis

Diagnose your activation funnel stage by stage. Find the biggest bottleneck between Setup, Aha, and Habit — and get specific, prioritized fixes grounded in your brain's user research and metrics.

## Invocation

```
/activation-analysis   → Tell me your product and I'll pull brain context and diagnose
```

## Brain Context

Load if available:
- `brain/knowledge/product/metrics.md` — current activation rates, D7 retention, and time-to-value baselines
- `brain/knowledge/users/insights.md` — user research on onboarding friction and confusion points
- `brain/knowledge/product/features/` — past onboarding improvements for context
- `brain/knowledge/strategy.md` — strategic priority context (is activation a current focus?)
- `brain/style/frameworks.md` — preferred analysis format
- Recent `brain/ingestion/` — support tickets, CS feedback, interview quotes about getting stuck

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/product/metrics.md` for current activation and retention baselines. Load user insights for qualitative signals about where users get stuck. These anchor the diagnosis in real data rather than generic activation frameworks.

### Step 2: Apply the Skill

Apply the **activation-analysis** skill.

Use brain metrics as the quantitative input for funnel stage analysis. Use user research quotes to explain the "why" behind drop-off rates. Reference past onboarding features from `brain/knowledge/product/features/` to avoid recommending things already tried.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-activation-analysis.md`.

### Step 4: Offer Follow-ups

- "Run `/ingest` to promote activation bottleneck findings into your brain."
- "Found retention issues downstream? Run `/retention-analysis`."
- "Ready to build a fix? Run `/prd-draft` or `/hypothesize`."
- "Expansion opportunity identified? Run `/expansion-strategy`."
