# Feature File Schema

Every file in `knowledge/product/features/` follows this template. Filename: `[slug].md`

---

```markdown
# [Feature Name]

**Status:** planning | in-progress | launching | shipped | archived
**Owner:**
**Started:**
**Shipped:** (leave blank if not yet shipped)

## Problem

<!-- One paragraph: what user problem does this solve and why now? -->

## Solution

<!-- What we are building. Scope. What's explicitly out of scope. -->

## Success Metrics

<!-- Primary metric this feature moves. Guardrail metrics. -->

**Primary:**
**Guardrails:**
**Leading indicators:**

## Hypothesis

<!-- Link to the hypotheses file for this feature -->
→ `../../../hypotheses/[slug].md`

## Impact Estimate

**Sizing:**
**Confidence:**
**Methodology:**

## Decisions

<!-- Links to relevant decision files -->

## Key Learnings

<!-- Post-launch: what did we learn? Did the hypothesis hold? -->
```
