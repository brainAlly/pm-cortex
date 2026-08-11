---
description: Select trustworthy experiment metrics using the STEDII framework before launching any test
argument-hint: "<feature or experiment name>"
---

# /experiment-metrics -- Experiment Metrics

Before launching an experiment, validate that your chosen metric is Sensitive, Timely, Efficient, Debuggable, Interpretable, and Isolated. Prevents wasted experiments caused by metric misselection.

## Invocation

```
/experiment-metrics   → Name the experiment or feature; I'll evaluate metric candidates
```

## Brain Context

Load if available:
- `brain/hypotheses/<feature-slug>.md` — active hypothesis to identify what the metric needs to validate
- `brain/knowledge/product/metrics.md` — current traffic and baseline data for sensitivity and detectability checks
- `brain/knowledge/product/features/<feature-slug>.md` — feature context for metric scoping
- `brain/style/frameworks.md` — preferred metrics format

## Workflow

### Step 1: Load Brain Context

Load the feature's hypothesis file to understand what belief the experiment is testing. Load `brain/knowledge/product/metrics.md` for actual traffic volumes — the sensitivity and timeliness checks require real sample size data, not estimates.

### Step 2: Apply the Skill

Apply the **experiment-metrics** skill.

Use brain traffic data to run the sensitivity check (will this metric actually move during the experiment window?). Use the hypothesis to validate that the chosen metric directly tests the stated belief. Flag any metric that fails a STEDII criterion with a specific alternative.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-experiment-metrics-<feature-slug>.md`.

### Step 4: Offer Follow-ups

- "Metric validated — now decide how to test. Run `/experiment-decision`."
- "Ready to set success criteria? Run `/feature-metrics` for the full metrics framework."
- "Run `/ingest` to store validated metric definitions in the feature's brain entry."
