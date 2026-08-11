---
description: Identify and validate your North Star Metric — the single number that captures your product's core value
argument-hint: "<product or business stage>"
---

# /define-north-star -- Define North Star

Identify, validate, and document your North Star Metric using the Frequency × Core Action × Breadth formula. Produces input metrics and guardrails that ladder down from it.

## Invocation

```
/define-north-star             → Walk through the full framework
/define-north-star --validate  → Validate an existing North Star candidate
```

## Brain Context

Load if available:
- `brain/knowledge/strategy.md` — current metric direction and any existing North Star candidate
- `brain/knowledge/product/metrics.md` — current metric baselines and what's already being tracked
- `brain/knowledge/users/insights.md` — core user behavior and what drives retention (input to North Star formula)
- `brain/hypotheses/` — any active hypotheses about what drives product value
- `brain/style/frameworks.md` — preferred strategy format

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/strategy.md` first — if a North Star already exists, this becomes a validation run, not a definition run. Load `brain/knowledge/product/metrics.md` for current tracking baselines. Load user insights to ground the "core action" component in real user behavior.

### Step 2: Apply the Skill

Apply the **define-north-star** skill.

Use brain's user insights to identify what behavior correlates with retention — this is the core action in the formula. Use existing metrics to evaluate whether a North Star candidate is actually measurable with current instrumentation. Flag if the candidate is lagging (revenue) vs. leading (engagement action).

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-north-star.md`.

### Step 4: Offer Follow-ups

- "Run `/decide` to commit the North Star to your brain as a formal decision."
- "Run `/ingest` to update `brain/knowledge/strategy.md` with the new North Star."
- "Define input metrics that ladder to this? Run `/feature-metrics` for each key lever."
- "Update your OKRs to reflect this North Star? Run `/plan-okrs`."
