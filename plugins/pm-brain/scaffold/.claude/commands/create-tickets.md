---
description: Break a PRD or feature spec into scoped engineering tickets with estimates, acceptance criteria, and dependencies
argument-hint: "<prd-name or feature spec>"
---

# /create-tickets -- Create Tickets

Generate scoped engineering tickets from a PRD or feature spec. Creates via Linear/Jira MCP if connected, or outputs formatted text for manual entry.

## Invocation

```
/create-tickets                                    → Point me to the source
/create-tickets outputs/prds/checkout-redesign.md  → Create from specific PRD
/create-tickets [paste spec]                        → Create from pasted content
```

## Brain Context

Load if available:
- `brain/knowledge/product/features/<feature-slug>.md` — feature context and scope boundaries
- `brain/knowledge/org/` — team structure and ownership (for ticket assignment)
- `brain/decisions/` — scope decisions that constrain what gets ticketed
- `brain/knowledge/product/roadmap.md` — sprint/milestone context for assignment

## Workflow

### Step 1: Load Brain Context

Load the relevant feature file from `brain/knowledge/product/features/` if it exists. Load `brain/knowledge/org/` for team context so ticket assignments reflect real ownership.

### Step 2: Apply the Skill

Apply the **create-tickets** skill.

Use brain knowledge to validate ticket scope against committed decisions — don't ticket work that was explicitly descoped. Use org context to suggest realistic owners. Reference the PRD's success metrics when writing acceptance criteria.

### Step 3: Save Output

If Linear/Jira MCP connected, create tickets directly and report back created ticket IDs.

If not connected, save formatted ticket text to `outputs/<YYYY-MM-DD>-tickets-<feature-slug>.md`.

### Step 4: Offer Follow-ups

- "Ready to plan the sprint? Run `/sprint`."
- "Want to track scope decisions in your brain? Run `/ingest`."
- "Scope changed from the PRD? Run `/decide` to document the scope decision."
