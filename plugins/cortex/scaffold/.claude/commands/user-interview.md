---
description: Process 1-3 user interview transcripts into insight cards with validated/challenged/new theme labels
argument-hint: "<paste transcript(s)>"
---

# /user-interview -- User Interview Processing

Process raw interview transcripts into structured insight cards — pain points, JTBD moments, quotes, and hypothesis validation status. Use for 1-3 interviews from a single research session.

## Invocation

```
/user-interview   → Paste transcript(s) and research goal; I'll extract insights
```

## Schema

Load `brain/hypotheses/_SCHEMA.md` before updating any hypothesis file.

## Brain Context

Load if available:
- `brain/knowledge/users/insights.md` — existing promoted insights to label as VALIDATED, CHALLENGED, or NEW
- `brain/hypotheses/` — active hypotheses to check against interview evidence
- `brain/knowledge/users/personas.md` — existing personas to match interviewees against
- Recent `brain/ingestion/interviews/` — prior interviews on the same topic to avoid re-validating known findings
- `rules/discovery.md` — team's research norms (if present)

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/users/insights.md` to know which insights already exist. Load active hypotheses for the feature area. This lets the skill label each finding as VALIDATED (confirms existing knowledge), CHALLENGED (contradicts existing knowledge), or NEW (net new finding).

Load `rules/discovery.md` for team-specific research norms — it may define how to handle edge findings or when to escalate an interview to a full research sprint.

### Step 2: Apply the Skill

Apply the **user-interview** skill.

Use brain context to skip re-surfacing already-confirmed insights. Focus extraction on what's new or contradictory. Attach hypothesis IDs to relevant findings so evidence trails stay connected.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-interview-<participant-slug>.md`.

Append raw synthesis to `brain/ingestion/interviews/<YYYY-MM-DD>-<slug>.md`.

### Step 4: Offer Follow-ups

- "Run `/ingest` to route findings into your brain and update hypothesis confidence."
- "Have 3+ interviews now? Run `/user-research-synthesis` to find cross-interview patterns."
- "New hypotheses surfaced? Run `/hypothesize` to formally track them."
- "Ready to update the PRD with these findings? Run `/prd-draft`."
