---
description: Run multi-agent PRD review from 7 perspectives — Engineering, Design, Exec, Legal, UXR, Skeptic, Customer
argument-hint: "<prd-name or leave blank to pick from recent>"
---

# /prd-review-panel -- PRD Review Panel

Get comprehensive PRD feedback from 7 sub-agent perspectives in parallel. Catches gaps, challenges assumptions, and surfaces conflicts before stakeholder review.

## Invocation

```
/prd-review-panel                             → Review most recent PRD
/prd-review-panel voice-task-capture          → Review specific PRD by name
/prd-review-panel --perspectives "eng,exec"   → Run subset of reviewers
```

## Brain Context

Load if available:
- `brain/knowledge/strategy.md` — for the executive reviewer's strategic alignment check
- `brain/knowledge/users/insights.md` — for the UXR analyst's validation of user evidence
- `brain/knowledge/market/competitors/` — for competitive context the skeptic will probe
- `brain/stakeholders/` — to anticipate real stakeholder concerns in each reviewer's output
- `brain/decisions/` — so reviewers don't relitigate committed decisions

## Workflow

### Step 1: Select PRD

If a PRD name is specified, look it up in `outputs/prds/`. If none specified, list recent PRDs and ask the user to choose.

Load the selected PRD in full. Load relevant brain context for each sub-agent perspective.

### Step 2: Apply the Skill

Apply the **prd-review-panel** skill.

Invoke sub-agents from `sub-agents/`:
1. `engineer-reviewer.md` — technical feasibility, complexity, dependencies
2. `designer-reviewer.md` — UX/UI feedback, user experience gaps
3. `executive-reviewer.md` — strategic alignment, business impact
4. `legal-advisor.md` — compliance, risk, regulatory concerns
5. `uxr-analyst.md` — user research validation
6. `skeptic.md` — devil's advocate, assumption challenges
7. `customer-voice.md` — simulated user perspective

Use brain stakeholder profiles to make each reviewer's concerns realistic rather than generic.

### Step 3: Save Output

Save consolidated review to `outputs/<YYYY-MM-DD>-prd-review-<feature-slug>.md`.

### Step 4: Offer Follow-ups

- "Decisions surfaced in the review? Run `/decide` to formally document them."
- "New hypotheses identified? Run `/hypothesize` to track them."
- "Ready to update the PRD with feedback? Run `/prd-draft` to iterate."
- "Run `/ingest` on the review feedback to route insights into your brain."
