# Decision File Schema

Every file in `decisions/` follows this template. Filename: `YYYY-MM-DD-[slug].md`

Provenance tag enum (same as hypotheses/_SCHEMA.md — use exactly one per evidence row).

---

```markdown
# Decision: [Short title]

**Status:** pending | decided | reversed
**Date decided:** YYYY-MM-DD (leave blank if pending)
**Date reversed:** YYYY-MM-DD (leave blank if not reversed)
**Driver:** [What prompted this decision? Which stakeholder or event forced the choice?]
**Blocked by:** [what must happen before this can be made — decision slug(s) and/or a named external condition, comma-separated; write `none` if it is actionable right now]
**Blocks:** [decision slug(s) that cannot proceed until this one is made; write `none` if nothing waits on it]

---

## What We Are Deciding

[One clear question. Not a paragraph — one sentence if possible.]

---

## Options Considered

**Option A:** [description]
**Option B:** [description]
**Option C (if applicable):** [description]

---

## Decision

**We chose:** [Option X]
**Because:** [2–3 sentence rationale]

---

## Evidence

<!-- Every row must have a provenance tag. No untagged claims. -->
- [provenance tag] — one-line evidence item
- [provenance tag] — one-line evidence item

---

## What We Are Not Doing

[Explicit statement of the rejected options and why.]

---

## Reversal Condition

[Observable event or data threshold that would cause us to revisit this decision. Be specific.]

---

## Stakeholders

**Consulted:**
**Signed off:**
**Informed:**

---

## Linked Files

- Hypothesis: `../hypotheses/[slug].md`
- Feature: `../knowledge/product/features/[slug].md`
```

---

## Dependencies — `Blocked by` / `Blocks`

`Reversal Condition` says what would *undo* a decision. `Blocked by` / `Blocks` say what a decision *waits on* and what *waits on it*. They are different axes — a decision needs both.

- **`Blocked by`** lists the upstream gates: other pending decisions (by slug) and/or named external conditions (`first design partner live`, `eval harness exists`). A decision whose every `Blocked by` gate is satisfied — the upstream decisions are `decided`, the external conditions have occurred — is **on the frontier: actionable now**. `Blocked by: none` means it is a frontier item from day one (an entry point).
- **`Blocks`** is the inverse edge. When you set `Blocked by: <upstream-slug>` on this decision, add this decision's slug to that upstream decision's `Blocks` field in the same turn, so the graph stays consistent in both directions.

This is what lets `/review` separate **waiting** (blocked, correctly idle) from **stuck** (on the frontier, actionable, but not being made) instead of nagging every pending decision by age. See `/review § Decision frontier`.
