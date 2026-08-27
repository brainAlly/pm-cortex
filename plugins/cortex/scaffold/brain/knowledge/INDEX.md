# Knowledge Index

Durable product state. Load from here before any execution task.

Evidence-bearing files (strategy, users, market) carry a `Tier:` marker:
- **`Tier: stated`** — operator-asserted or single-source; not yet verified. Everything seeded at setup starts here. Ranks *below* direct customer evidence.
- **`Tier: confirmed`** — backed by 3+ independent external sources. What the system trusts by default.

`/review` promotes `stated → confirmed` as evidence accumulates. Descriptive/state files (`product/metrics.md`, `product/roadmap.md`, `org/*`, `product/features/*`) hold data or plans, not competing claims, and carry no tier. See `../../CLAUDE.md § Evidence Hierarchy` and `§ Memory Promotion`.

For working memory (not yet durable), see `../ingestion/`. For raw source artifacts, see `../source/`.

---

## Strategy

| File | What it contains |
|---|---|
| [`strategy.md`](./strategy.md) | North Star metric, quarter priorities, non-goals, strategic tensions, OKRs |

Load for: every prioritization, planning, strategy-check, or ideation task.

---

## Product

| File | What it contains |
|---|---|
| [`product/roadmap.md`](./product/roadmap.md) | Now / Next / Later feature plan with outcomes and owners |
| [`product/metrics.md`](./product/metrics.md) | Current metric values, baselines, and targets |
| [`product/features/`](./product/features/) | One file per feature — status, hypothesis link, open decisions |

Load for: PRD drafts, sprint planning, launch checklists, impact sizing.

---

## Users

| File | What it contains |
|---|---|
| [`users/insights.md`](./users/insights.md) | Promoted user patterns — confirmed themes with evidence rows and provenance |
| [`users/personas.md`](./users/personas.md) | Durable persona definitions with JTBD, pain points, and behavioral markers |
| [`users/segments.md`](./users/segments.md) | Segment breakdown — size, characteristics, and strategic priority |

Load for: user-facing decisions, research synthesis, discovery, GTM.

---

## Market

| File | What it contains |
|---|---|
| [`market/landscape.md`](./market/landscape.md) | Competitive landscape — key players, positioning map, and differentiation |
| [`market/trends.md`](./market/trends.md) | Macro trends relevant to the product space |

Load for: competitive analysis, GTM strategy, expansion planning.

---

## Org

| File | What it contains |
|---|---|
| [`org/team.md`](./org/team.md) | Team roster — roles, ownership areas, and working styles |
| [`org/rituals.md`](./org/rituals.md) | Recurring ceremonies — cadence, purpose, and participants |
| [`org/tools.md`](./org/tools.md) | Tools and integrations the team uses |

Load for: sprint planning, retros, stakeholder prep, org-related decisions.
