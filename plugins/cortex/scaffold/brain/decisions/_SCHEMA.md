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
