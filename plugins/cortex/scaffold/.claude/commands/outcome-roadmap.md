---
description: Build an outcome-based now/next/later roadmap anchored to measurable outcomes, not features
argument-hint: "[quarter or planning horizon]"
---

# /outcome-roadmap

Usage: `/outcome-roadmap`

Produces an outcome-based roadmap that communicates direction without committing to specific features or dates prematurely. Reframes the `## Next` / `## Later` sections of the canonical roadmap file and never touches its `## Now` open-work table.

## Execution

### Step 1 — Load context

- `brain/knowledge/strategy.md` — OKRs, North Star, and strategic priorities
- `templates/roadmap-template.md` — output structure (if present)
- `brain/knowledge/product/roadmap.md` — current roadmap state. Its `## Now` table is the canonical home for **open work** (owned rows written by `/review` and `/sprint` — see `CLAUDE.md § Canonical Ownership`). This command **reads** those rows for context but **never rewrites the `## Now` table**. It reshapes only the `## Next` and `## Later` framing.
- `brain/knowledge/product/features/` — features in progress or planned
- `brain/hypotheses/INDEX.md` — confidence levels for planned bets
- `brain/knowledge/users/insights.md` — user needs driving the roadmap
- `brain/style/frameworks.md` + `brain/style/patterns.md`

### Step 2 — Clarify the audience

Ask the PM: "Who is this roadmap for — internal team, leadership, customers, or investors? This determines how much detail and how many features to name."

Audience conventions:
- **Internal team:** can include feature-level detail, hypothesis links, confidence scores
- **Leadership:** outcome-focused, OKR-linked, a few anchor features for concreteness
- **External (customers, investors):** outcome-focused only — no feature promises, no specific dates

Produce the appropriate version or ask which to create first.

### Step 3 — Build the roadmap structure

Organize into three horizons. Do not use quarters or months as primary organizing units — use outcomes.

**Now (current quarter / sprint cycle):**
Work the team is doing right now. Specific and committed. This is a *communication* view — derive it by reading the owned rows already in `roadmap.md § Now` (each row's `Target outcome` column) plus in-progress features. It restates that work as outcomes for the shareable version; it does not replace or re-author the `§ Now` table.
- Outcome: [what we expect to be measurably different when this ships]
- Evidence: [hypothesis confidence + user evidence supporting the bet]
- Anchor features (if naming features): [1–2 named features — no more]
- Status: [In Sprint / In Review / Shipping]

**Next (next 1–2 quarters):**
Work the team is planning but hasn't started. Direction is set, details may shift.
- Outcome: [measurable target, tied to an OKR KR]
- Evidence: [hypothesis confidence — should be 0.5+ to appear in "next"]
- Approach: [problem area, not specific feature — "improve onboarding" not "add a progress bar"]
- Open questions: [what we still need to learn before execution]

**Later (3–6 months out):**
Strategic bets and problem areas the team intends to address. Intentionally vague.
- Outcome area: [the user problem or business goal — no features, no dates]
- Why it matters: [connection to North Star or OKR]
- What would unlock it: [hypothesis validation needed, strategic decision, or market signal]

### Step 4 — Explicitly list what's not on the roadmap

The "not now" list is as important as the roadmap itself. It prevents stakeholder confusion and scope creep.

"**Not this cycle** (considered and deprioritized):"
- [item]: [why it's not on the roadmap — low confidence hypothesis / not OKR-aligned / resources / market timing]

### Step 5 — Confidence and risk overlay

For each "Now" and "Next" item, add:
- Hypothesis confidence: [score from `brain/hypotheses/`]
- Biggest risk: [one-line — value / usability / feasibility / viability]
- Mitigation planned: [yes / no — what it is]

Flag any "Now" item with hypothesis confidence below 0.5: "Shipping a bet with confidence [X] — is there a faster validation we should run first?"

### Step 6 — Stakeholder alignment check

For each item in "Now" and "Next":
- Who are the key stakeholders who need to be aligned? (Reference `brain/stakeholders/INDEX.md`)
- Is there any known misalignment? Flag it: "Engineering lead has concerns about [feature] — see `stakeholders/[slug].md`."

### Step 7 — Update roadmap.md (one-line confirmation)

Ask: "Update `brain/knowledge/product/roadmap.md` with this outcome roadmap? (y/n)"

On yes, update the brain file under two hard rules:

- **Never rewrite the `## Now` table.** It is the canonical home for open work — owned rows (`Item · Owner · Due · Status · Source · Target outcome`) written by `/review` and `/sprint`. Rewriting it here would silently drop tracked, owned work (`CLAUDE.md § Canonical Ownership`). Leave it byte-for-byte intact. The outcome "Now" you built in Step 3 is a communication view — it lives in the shareable copy below, not in this table.
- **Update only the `## Next` and `## Later` sections** with the reframed outcomes, preserving those sections' existing table columns. Do not touch `## Recently Shipped` or `## Archived`, and preserve any existing sprint commitments and feature statuses.

If the reframe cannot be expressed without rewriting `## Now`, stop and surface that to the PM rather than overwriting it.

Save the full outcome roadmap — including the Step 3 "Now" communication view — as a shareable version (without hypothesis scores and brain references) to `outputs/YYYY-MM-DD-roadmap-[audience].md`.

Report: "Roadmap `## Next` / `## Later` reframed in `brain/knowledge/product/roadmap.md` (`## Now` work table left untouched). Shareable version saved to `outputs/`."
