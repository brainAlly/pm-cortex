---
description: Quantify feature value using a 4-step driver tree with confidence levels
argument-hint: "<feature name or idea>"
---

# /impact-sizing -- Impact Sizing

Systematically estimate a feature's impact using driver trees, confidence intervals, and historical precedent from your brain. Produces a defensible business case, not a guess.

## Invocation

```
/impact-sizing   → Tell me the feature; I'll pull context and estimate
```

## Brain Context

Load if available:
- `brain/knowledge/product/features/<feature-slug>.md` — feature definition, user impact, and problem severity
- `brain/knowledge/users/insights.md` and personas — addressable user base and pain severity
- `brain/knowledge/product/metrics.md` — historical baselines and comparable feature adoption rates
- `brain/knowledge/strategy.md` — strategic priority context (resource availability, quarter focus)
- `brain/style/frameworks.md` — preferred sizing format

## Workflow

### Step 1: Load Brain Context

Load the feature file if it exists. Load `brain/knowledge/product/metrics.md` for historical adoption rates to use as comparables. Load user insights for addressable segment sizing. This grounds estimates in actual product data rather than industry benchmarks.

### Step 2: Apply the Skill

Apply the **impact-sizing** skill.

Use brain baselines as the starting point for the driver tree. Label each estimate with its confidence level and provenance (from brain file vs. assumed). Flag where assumptions are weakest.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-impact-sizing-<feature-slug>.md`.

Auto-write: add the impact estimate to `brain/knowledge/product/features/<feature-slug>.md` if the feature file exists.

### Step 4: Offer Follow-ups

- "Sizing informs a build/kill decision? Run `/decide` to document it."
- "Run `/ingest` to store this estimate in the feature's brain entry."
- "Comparing options? Use this output with `/experiment-decision` to decide how to validate."
- "Define success metrics for this feature? Run `/feature-metrics`."
