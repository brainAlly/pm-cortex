---
description: Synthesize 4+ interviews into a unified research report with cross-interview patterns and strategic recommendations
argument-hint: "<topic or paste interview files>"
---

# /user-research-synthesis -- Research Synthesis

Turn 4+ user interviews into a unified research report. Applies advanced synthesis — affinity mapping, Mom Test validation, Five Whys root cause — to find cross-interview patterns and strategic recommendations.

## Invocation

```
/user-research-synthesis   → Point me to interview files or paste; I'll synthesize
```

## Brain Context

Load if available:
- `brain/knowledge/users/insights.md` — existing promoted insights to check against new findings
- `brain/knowledge/users/personas.md` — existing personas to validate or challenge
- `brain/hypotheses/` — active hypotheses to update confidence levels based on evidence
- Recent `brain/ingestion/interviews/` — individual interview files to synthesize across
- `brain/knowledge/strategy.md` — strategic context to frame recommendations

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/users/insights.md` to know what's already promoted. Load active hypotheses to weight evidence against them. This ensures the synthesis surfaces what's genuinely new or contradictory rather than re-confirming known patterns.

Check: are there 3+ independent observations of the same theme? If so, surface a knowledge promotion candidate.

### Step 2: Apply the Skill

Apply the **user-research-synthesis** skill.

Use brain knowledge to cross-reference findings against existing insights and hypotheses. Distinguish between confirming existing knowledge and generating net-new findings. Track evidence counts per theme for promotion eligibility.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-research-synthesis-<topic-slug>.md`.

### Step 4: Offer Follow-ups

- "Run `/ingest` to promote confirmed patterns to `brain/knowledge/users/insights.md`."
- "New hypotheses from this research? Run `/hypothesize` to formally track them."
- "Ready to turn insights into a feature? Run `/prd-draft`."
- "Competitor mentions surfaced? Run `/competitor-analysis` to expand."
