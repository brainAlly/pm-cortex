---
description: Define success metrics for a feature using the STEDII framework — Sensitive, Timely, Efficient, Debuggable, Interpretable, Isolated
argument-hint: "<feature name>"
---

# /feature-metrics -- Feature Metrics

Select trustworthy metrics that will actually tell you if the feature worked. STEDII-validated, laddered to your North Star, with guardrail metrics to catch regressions.

## Invocation

```
/feature-metrics   → Name the feature; I'll pull context and define metrics
```

## Brain Context

Load if available:
- `brain/knowledge/product/features/<feature-slug>.md` — hypothesis, problem statement, and user impact
- `brain/knowledge/strategy.md` — North Star metric and strategic pillars to ladder metrics up to
- `brain/knowledge/product/metrics.md` — current baselines and historical ranges
- `brain/hypotheses/<feature-slug>.md` — active hypotheses that suggest which leading metrics matter
- `brain/style/frameworks.md` — preferred metrics format

## Workflow

### Step 1: Load Brain Context

Load the feature's hypothesis file to understand what belief the metrics need to validate. Load `brain/knowledge/strategy.md` for the North Star — every feature metric should ladder up to it. Load `brain/knowledge/product/metrics.md` for baselines to set realistic targets.

### Step 2: Apply the Skill

Apply the **feature-metrics** skill.

Use the North Star from strategy to define the impact chain: feature metric → product metric → North Star. Use existing baselines from brain to set STEDII-valid targets rather than arbitrary numbers. Reference active hypotheses to select metrics that will actually validate or invalidate the belief.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-feature-metrics-<feature-slug>.md`.

Auto-write: add the metric definitions to `brain/knowledge/product/features/<feature-slug>.md` under a metrics section.

### Step 4: Offer Follow-ups

- "Run `/ingest` to store these metric definitions in the feature's brain entry."
- "Setting up an experiment? Run `/experiment-metrics` to validate metric trustworthiness."
- "Need to decide how to validate? Run `/experiment-decision`."
- "Update your hypotheses with these metrics? Run `/hypothesize`."
