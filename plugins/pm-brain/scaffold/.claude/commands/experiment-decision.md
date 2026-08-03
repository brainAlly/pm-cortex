---
description: Decide whether to A/B test, ship + monitor, or just ship using the reversibility decision tree
argument-hint: "<feature or change to evaluate>"
---

# /experiment-decision -- Experiment Decision

Walk the decision tree: reversibility → hypothesis strength → detectable impact → risk level. Get a clear recommendation: A/B test, ship + monitor, or just ship — with rationale.

## Invocation

```
/experiment-decision   → Describe the feature/change; I'll walk the decision tree
```

## Brain Context

Load if available:
- `brain/hypotheses/<feature-slug>.md` — hypothesis confidence and evidence weight to assess how strong the belief is before testing
- `brain/knowledge/strategy.md` — risk tolerance and strategic priority context
- `brain/decisions/` — prior decisions on this feature that constrain testing options
- `brain/knowledge/product/metrics.md` — traffic and sample size context for detectability

## Workflow

### Step 1: Load Brain Context

Load the feature's hypothesis file to assess current confidence level. A high-confidence hypothesis backed by strong evidence may not need an A/B test. Load `brain/knowledge/product/metrics.md` for traffic volume — detectable impact depends on actual sample sizes.

### Step 2: Apply the Skill

Apply the **experiment-decision** skill.

Use hypothesis confidence from the brain to calibrate the "hypothesis strength" question in the decision tree. Use real traffic data for the detectability assessment. Flag if the decision contradicts a prior committed decision in `brain/decisions/`.

### Step 3: Save Output

Save decision and rationale to `outputs/<YYYY-MM-DD>-experiment-decision-<feature-slug>.md`.

### Step 4: Offer Follow-ups

- "Run `/decide` to formally commit this testing decision to your brain."
- "Decided to test? Run `/feature-metrics` to define the success metric."
- "Decided to ship? Run `/launch-checklist` to prepare."
- "Run `/hypothesize` to update hypothesis confidence based on this decision."
