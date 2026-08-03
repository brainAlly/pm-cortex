---
description: Build an expansion playbook for upsell, cross-sell, and account growth with NRR decomposition
argument-hint: "<expansion lever: upsell | cross-sell | seat expansion>"
---

# /expansion-strategy -- Expansion Strategy

Decompose your NRR, identify the biggest expansion gap, assess pricing sensitivity, and build a prioritized expansion playbook with in-product triggers and a GTM motion.

## Invocation

```
/expansion-strategy            → Full strategy across all expansion levers
/expansion-strategy upsell     → Focus on upsell lever specifically
/expansion-strategy cross-sell → Focus on cross-sell lever
```

## Brain Context

Load if available:
- `brain/knowledge/strategy.md` — growth focus, customer segmentation, and market positioning
- `brain/knowledge/market/` — competitive pricing and expansion tactics used by competitors
- `brain/knowledge/users/insights.md` — power user behavior and expansion signals from research
- `brain/knowledge/product/metrics.md` — NRR, expansion rate, churn rate baselines
- `brain/decisions/` — committed pricing or tier decisions that constrain the strategy
- `brain/style/frameworks.md` — preferred strategy format

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/product/metrics.md` for NRR and expansion rate baselines. Load `brain/knowledge/strategy.md` for customer segmentation and growth focus. Load competitive context from `brain/knowledge/market/` for pricing benchmarks. Check `brain/decisions/` for committed pricing decisions that define the playing field.

### Step 2: Apply the Skill

Apply the **expansion-strategy** skill.

Use brain metrics to ground the NRR decomposition in real numbers. Use competitive pricing from brain market knowledge for sensitivity benchmarks. Reference user insights to identify which power user behaviors correlate with upgrade readiness — these become the in-product expansion triggers.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-expansion-strategy.md`.

### Step 4: Offer Follow-ups

- "Run `/ingest` to route expansion findings into your brain."
- "Pricing decisions surfaced? Run `/decide` to formally commit them."
- "Activation gap limiting expansion? Run `/activation-analysis`."
- "Retention issues affecting NRR? Run `/retention-analysis`."
