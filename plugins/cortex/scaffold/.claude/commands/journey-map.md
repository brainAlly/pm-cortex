---
description: Map user or customer journeys to surface friction points, emotional lows, and opportunity gaps
argument-hint: "<user journey | customer journey> for <product or flow>"
---

# /journey-map -- Journey Map

Create a user journey map (product experience) or customer journey map (full lifecycle) grounded in your brain's user insights and competitive context.

## Invocation

```
/journey-map user onboarding              → User journey for onboarding flow
/journey-map customer awareness to renew  → Full customer lifecycle map
/journey-map                              → I'll ask which mode and what to map
```

## Brain Context

Load if available:
- `brain/knowledge/users/insights.md` — promoted user patterns to ground pain points in real evidence
- `brain/knowledge/users/personas.md` — persona context for who this journey belongs to
- `brain/knowledge/product/` — feature context and known friction points
- `brain/knowledge/market/` — competitive alternatives users encounter at each stage (for customer journeys)
- Recent `brain/ingestion/interviews/` — verbatim quotes to embed in emotional touchpoints

## Workflow

### Step 1: Load Brain Context

Load user insights and persona to establish who's taking this journey. Load recent interview ingestion for verbatim quotes that can annotate emotional high/low points — these make the map evidence-based rather than assumed.

### Step 2: Apply the Skill

Apply the **journey-map** skill.

Use brain insights to annotate touchpoints with real user evidence rather than generic emotions. Use competitive context (for customer journeys) to map where users evaluate alternatives. Flag each pain point against the `brain/hypotheses/` to note which ones are actively being addressed.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-journey-map-<slug>.md`.

### Step 4: Offer Follow-ups

- "Run `/ingest` to route friction points and opportunities into your brain."
- "Friction points worth building for? Run `/prd-draft` or `/ideate`."
- "Want to validate the journey with users? Run `/interview-guide` to build a research plan."
