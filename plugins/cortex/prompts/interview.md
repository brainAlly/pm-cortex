# Interview

Run before scaffolding. Ask in **batches of 3–4 questions**, not one-by-one. Tone: short, direct, no lecturing.

In migration mode, **skip batches already covered by source artifacts** and ask only the unknowns. Tell the PM what you already know before asking what you don't.

## Batch A — Context
1. Company name, product, and one-line description of what it does.
2. Stage (pre-PMF / scaling / mature) and rough scale signal (users, ARR, team size — whatever they know).
3. Their role scope: which surfaces / squads / domains do they own?
4. Top 3 strategic priorities for the next 1–2 quarters (rough is fine; we'll refine).

## Batch B — People
1. Name + role of their top 5–10 stakeholders (manager, eng lead, design lead, key execs, key customers if applicable).
2. Which 2–3 of those are **highest-friction or highest-leverage** right now?
3. Cadence — any standing 1:1s / rituals worth encoding?

## Batch C — Work in flight
1. What features / initiatives are **active** right now? (list 2–6, slug-ify them)
2. What's the next **big bet** being scoped but not started?
3. Any recent **shipped** thing they're still measuring?

## Batch D — Inputs
1. What data sources do they touch weekly? (analytics tool, interview transcripts, support tickets, sales calls, Slack channels, etc.)
2. Do they run customer interviews? If yes, roughly how often, and where do transcripts live?
3. What competitor / market signals do they track?

## Batch E — Operating preferences
1. Autonomy level: should the system **act and tell** (default), or **propose and wait**? Recommend "act and tell" for anything reversible. Stored in `CLAUDE.md § Operating preferences § Autonomy mode`.
2. Maintenance cadence preference: weekly review? on-demand only? both? Stored in `CLAUDE.md § Operating preferences § Maintenance cadence`.
3. Anything explicitly **off-limits** beyond the defaults? Defaults: avoid PII (addresses, phone numbers, financial details, government IDs, medical info). Synthetic names, work emails, and organizational context are allowed. Stored in `CLAUDE.md § Off-limits`.

## Batch F — Style & Preferences
1. Preferred output format and length — structured vs narrative, how long is "too long" for a response?
2. Preferred frameworks for prioritization, discovery, strategy, and metrics?
3. Communication style preferences — how direct, how much context, what tone with different audiences?

## After the interview

1. **Summarize back what you heard in 6–10 bullets.**
2. **Surface contradictions.** Examples: "You said pre-PMF but listed 8 active features — which is real?" "Your top stakeholder is high-friction *and* you said cadence is monthly — is that the right rhythm?"
3. **Confirm before scaffolding.** Do not move on without explicit confirmation.

## What the answers feed

| Batch | Question | Populates |
| --- | --- | --- |
| A | Q1-2 company/product/stage | `brain/knowledge/strategy.md` (top section), `README.md` (product line, optional) |
| A | Q3 role scope | `brain/knowledge/org/team.md` |
| A | Q4 priorities | `brain/knowledge/strategy.md § 1–2 quarter priorities` |
| B | Q1 stakeholders | `brain/stakeholders/<slug>.md` (one per person), `brain/stakeholders/INDEX.md` (roster) |
| B | Q2 friction/leverage | `brain/stakeholders/<slug>.md § Snapshot` (influence + friction), `brain/stakeholders/INDEX.md` |
| B | Q3 cadence | `brain/knowledge/org/rituals.md` |
| C | Q1 active features | `brain/knowledge/product/features/<slug>.md` (one per feature), `brain/knowledge/product/roadmap.md § Now` (Owner: the PM; Due: `unscheduled` — the interview collects no owners/dates, and the Now rule forbids fabricating them) |
| C | Q2 next big bet | `brain/knowledge/product/roadmap.md § Next` |
| C | Q3 recent shipped | `brain/knowledge/product/roadmap.md § Now` (with status: measuring), feature file |
| D | Q1 data sources | `brain/knowledge/org/tools.md`, `rules/data.md § Source of truth per metric` |
| D | Q2 interview cadence | `rules/discovery.md § Cadence`, `rules/discovery.md § Where transcripts live` |
| D | Q3 market signals | `brain/knowledge/market/landscape.md`, `brain/knowledge/market/trends.md` |
| E | Q1 autonomy | `CLAUDE.md § Operating preferences § Autonomy mode` |
| E | Q2 maintenance cadence | `CLAUDE.md § Operating preferences § Maintenance cadence` |
| E | Q3 off-limits | `CLAUDE.md § Off-limits` |
| F | Q1 output format/length | `brain/style/writing.md` |
| F | Q2 preferred frameworks | `brain/style/frameworks.md` |
| F | Q3 communication style | `brain/style/patterns.md` |

Keep provenance: every populated field should be traceable back to a specific Batch question or a source artifact. If a Batch answer has no clear home, flag it in the post-scaffold "immediate next moves" rather than silently dropping it.

## Provenance vocabulary, not provenance workflow

When you write claims into hypotheses, insights, or decisions, tag each row with a provenance marker from the enum in `hypotheses/_SCHEMA.md`. Claims born in this interview (no artifact behind them) are legitimate inputs — tag them `(stakeholder-verbal, <PM>, <date>)` or `(chat, no artifact)` rather than fabricating an ingestion record. The auditability promise is "every claim wears its source," not "every claim went through synthesis."
