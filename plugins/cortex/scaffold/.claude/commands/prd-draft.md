---
description: Create a modern PRD using brain context for strategy, users, hypotheses, and active decisions
argument-hint: "<feature idea or problem statement>"
---

# /prd-draft -- PRD Draft

Write a modern, AI-era PRD grounded in your brain context — strategy alignment, user evidence, active hypotheses, and prior decisions pre-loaded so you're not starting from scratch.

## Invocation

```
/prd-draft                          → Guided questions to start from scratch
/prd-draft [paste feature idea]     → Skip questions you've already answered
/prd-draft --stage "team kickoff"   → Set PRD stage upfront
/prd-draft --ai                     → Include AI behavior specification sections
```

## Schema

Load `brain/knowledge/product/features/_SCHEMA.md` before creating the feature file.

## Brain Context

Load if available:
- `brain/knowledge/product/` — active features, roadmap, and metrics for context and cross-references
- `brain/knowledge/users/insights.md` and `brain/knowledge/users/personas.md` — user evidence to anchor the problem statement
- `brain/hypotheses/<feature-slug>.md` — active hypotheses for this feature area to populate assumptions
- `brain/knowledge/strategy.md` — strategic pillars and priorities for the "why now" and strategic fit sections
- `brain/knowledge/market/competitors/` — competitive context for positioning
- `brain/decisions/` — prior decisions that constrain or inform this feature's scope
- `brain/style/writing.md` — your PRD voice and format preferences
- `docs/examples/` — past PRDs for style reference (if present)
- `templates/prd-template.md` — output structure template (if present)
- `rules/discovery.md` — team's discovery norms (if present)

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/strategy.md` to establish strategic fit. Load relevant `brain/hypotheses/` to populate the assumptions section with evidence-weighted beliefs. Load `brain/knowledge/users/insights.md` for user evidence to anchor the problem statement.

Check `brain/decisions/` for any committed decisions that constrain this feature's scope — surface them as non-goals or constraints.

Load `templates/prd-template.md` for the output structure. Load `docs/examples/` (blinkit-group-order-prd.md, example_prd.md) for style and format reference. Load `rules/discovery.md` for any team-specific discovery norms that affect the PRD's assumptions section.

### Step 2: Apply the Skill

Apply the **prd-draft** skill.

Use brain context to pre-populate: strategic fit from `strategy.md`, user quotes from ingestion files, hypothesis confidence from `hypotheses/`, and competitive context from `knowledge/market/`. Reference specific brain files inline in the PRD so it stays connected to the broader context.

### Step 3: Save Output

Save to `outputs/prds/<feature-slug>-<stage>.md`.

Auto-write: create `brain/knowledge/product/features/<feature-slug>.md` as a lightweight feature entry linking to this PRD.

### Step 4: Offer Follow-ups

- "Want multi-perspective review? Run `/prd-review-panel` to run all 7 reviewer subagents in parallel."
- "Surface the riskiest assumptions? Run `/hypothesize` to formalize them."
- "Break this into tickets? Run `/create-tickets`."
- "Run `/ingest` on the final PRD to route decisions into your brain."
