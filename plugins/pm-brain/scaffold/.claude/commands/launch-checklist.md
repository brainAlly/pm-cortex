---
description: Generate a comprehensive launch checklist with critical path, owners, and dependencies for a feature
argument-hint: "<feature name or prd-name> [target date]"
---

# /launch-checklist -- Launch Checklist

Generate a prioritized launch checklist covering pre-launch prep, launch execution, and post-launch monitoring. Identifies the critical path so nothing slips.

## Invocation

```
/launch-checklist                                    → I'll ask what you're launching
/launch-checklist checkout-redesign                  → Create from named PRD
/launch-checklist checkout-redesign --target Mar 15  → With target date for due dates
/launch-checklist --template small|major|regulatory  → Use specific template
```

## Brain Context

Load if available:
- `brain/knowledge/product/features/<feature-slug>.md` — feature scope, success metrics, and rollout plan
- `brain/knowledge/org/` — team structure and ownership for checklist assignment
- `brain/stakeholders/` — key stakeholders who need to be looped in at each stage
- `brain/decisions/` — committed scope decisions that constrain the checklist
- `templates/launch-checklist-template.md` — base template (if present)
- `rules/shipping.md` — team's launch norms and required gates (if present)

## Workflow

### Step 1: Load Brain Context

Load the feature's brain entry for scope and success metrics (used to define post-launch monitoring criteria). Load `brain/knowledge/org/` to assign realistic owners. Load `rules/shipping.md` for required gates specific to your team.

Load `templates/launch-checklist-template.md` as the base structure — populate it rather than generating a checklist from scratch, so no standard gate gets accidentally omitted.

### Step 2: Apply the Skill

Apply the **launch-checklist** skill.

Use brain stakeholder profiles to name real owners rather than generic roles. Use feature success metrics from the brain to define the post-launch monitoring thresholds. Reference prior launch checklists in `brain/ingestion/` to learn from past launches.

### Step 3: Save Output

Save to `outputs/launches/<YYYY-MM-DD>-launch-checklist-<feature-slug>.md`.

Auto-write: update `brain/knowledge/product/roadmap.md` to mark this feature as "launch in progress."

### Step 4: Offer Follow-ups

- "Outstanding work to track? Run `/sprint` to plan remaining work."
- "Post-launch: run `/ingest` to capture launch learnings into your brain."
- "Metrics below target post-launch? Run `/activation-analysis` or `/retention-analysis`."
