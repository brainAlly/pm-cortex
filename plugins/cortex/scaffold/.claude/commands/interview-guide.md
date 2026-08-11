---
description: Create a JTBD-based interview guide focused on gaps in your existing research
argument-hint: "<topic> with <target segment>"
---

# /interview-guide -- Interview Guide

Generate a structured interview guide using Jobs-to-be-Done methodology. Focused on what you don't yet know — gaps in existing research — rather than re-asking what's already confirmed.

## Invocation

```
/interview-guide   → Tell me the topic, interviewee, and hypothesis; I'll build the guide
```

## Brain Context

Load if available:
- `brain/knowledge/users/insights.md` — existing confirmed insights to skip re-validating
- `brain/hypotheses/<feature-slug>.md` — active hypotheses to target with specific questions
- `brain/knowledge/users/personas.md` — target segment context for tailoring questions
- Recent `brain/ingestion/interviews/` — prior interviews on related topics to avoid duplication
- `brain/knowledge/strategy.md` — strategic context so questions connect to decisions that matter
- `rules/discovery.md` — team's research norms (if present)
- `templates/interview_template.md` — output structure for the guide (if present)

## Workflow

### Step 1: Load Brain Context

Load `brain/knowledge/users/insights.md` to identify what's already confirmed — the guide should target gaps, not re-validate known findings. Load active hypotheses for this feature area so each guide section maps to a specific belief being tested.

Load `rules/discovery.md` for team-specific research norms. Load `templates/interview_template.md` for the output structure — use it as the base and populate it rather than generating a guide from scratch.

### Step 2: Apply the Skill

Apply the **interview-guide** skill.

Use the hypothesis file to structure questions that will produce VALIDATED / CHALLENGED / NEW verdicts. Use existing insights to frame warm-up questions that don't waste time on known territory. Use the persona profile to calibrate language and context-setting for the target segment.

### Step 3: Save Output

Save to `outputs/<YYYY-MM-DD>-interview-guide-<topic-slug>.md`.

### Step 4: Offer Follow-ups

- "After interviews, run `/user-interview` to process each transcript."
- "Have 4+ interviews? Run `/user-research-synthesis` for cross-interview patterns."
- "Run `/hypothesize` to update or add hypotheses before the interviews begin."
