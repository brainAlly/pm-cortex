# Hypothesis File Schema

Every file in `hypotheses/` follows this template. Filename: `[feature-slug].md`

Provenance tag enum (use exactly one per evidence row):
- `[ingestion/path/file.md]` — from a synthesized ingestion file
- `[source/path/file.md]` — from the raw source artifact
- `(stakeholder-verbal, Name, YYYY-MM-DD)` — heard from a person
- `(intuition, PM, YYYY-MM-DD)` — PM's own read
- `(industry-knowledge)` — accepted background
- `(chat, no artifact)` — synthesized in conversation

---

```markdown
# Hypothesis: [Feature Name]

**Status:** active | partially-validated | promoted | demoted | archived
**Feature slug:** [slug]
**Opened:** YYYY-MM-DD
**Last updated:** YYYY-MM-DD
**Decision trigger:** [What evidence threshold would move this to a decision?]

---

## H1. Value Risk — Will users want this?

**Confidence:** 0.0–1.0
**Evidence for:**
- [provenance tag] — one-line claim

**Evidence against:**
- [provenance tag] — one-line claim

**Open questions / caveats:**

---

## H2. Usability Risk — Can users use this?

**Confidence:** 0.0–1.0
**Evidence for:**
**Evidence against:**
**Open questions / caveats:**

---

## H3. Feasibility Risk — Can we build this?

**Confidence:** 0.0–1.0
**Evidence for:**
**Evidence against:**
**Open questions / caveats:**

---

## H4. Viability Risk — Should we build this?

**Confidence:** 0.0–1.0
**Evidence for:**
**Evidence against:**
**Open questions / caveats:**

---

## H5. Other Risk — Regulatory, partnership, timing

**Confidence:** 0.0–1.0
**Evidence for:**
**Evidence against:**
**Open questions / caveats:**

---

## Linked Files

- Feature: `../knowledge/product/features/[slug].md`
- Decisions: `../decisions/`
- Source artifacts: `../source/`
```
