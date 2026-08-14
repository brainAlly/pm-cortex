---
description: Run weekly maintenance sweep across knowledge, hypotheses, decisions, and stakeholders to surface drift and compression opportunities
argument-hint: "[optional scope: hypotheses|stakeholders|knowledge|decisions]"
---

# /review

The weekly maintenance sweep. Six checks. Produces a dated report and edits files directly where confidence is high.

## Input

None, or an optional scope (`/review hypotheses`, `/review stakeholders`) to run a single check.

## Loads

- `CLAUDE.md` (operating principles, autonomy mode, memory promotion bar)
- `docs/system-evolution.md` (the 8 failure modes the sweep is designed to catch)
- All durable areas in scope: `brain/knowledge/`, `brain/hypotheses/`, `brain/decisions/`, `brain/stakeholders/`
- Recent `brain/ingestion/` for promotion candidates
- The last 2 `maintenance/log/` entries to compare deltas

## Updates

- `maintenance/log/<date>-review.md` — the dated report
- Direct edits to durable files where confidence is high: promote / demote hypotheses, update stakeholder `Last touched`, archive shipped features past 90 days, compress duplicate insights
- **Work rows in `brain/knowledge/product/roadmap.md § Now`** for every finding that needs a human to act. Each row carries an owner and a due date and links back to this run's log entry (see § Converting findings to work). The log records what was surfaced; the Now table records what someone committed to do about it. A finding that ends the run as prose in the log with no Now row is a bug in the sweep, not a completed check.

## Surfaces

The six standard checks, with counts and the top item in each:

1. **Stale knowledge** — files not updated in 6+ weeks
2. **Stale evidence** — market past 30-60 days, interviews past 90, strategy assumptions past quarterly
3. **Hypothesis and decision hygiene** — active hypotheses with no evidence in 30+ days, promoted hypotheses without decisions, triggered "what would reverse this" conditions, decision debt
4. **Stakeholder cadence and strategy tensions** — high-influence stakeholders not touched in 3+ weeks, drift between recent decisions and strategy
5. **Knowledge synthesis (compression)** — recurring patterns, recurring contradictions, candidates for `strategy.md § Tensions`
6. **Archival sweep** — shipped features past 90 days, resolved hypotheses, old market intel

Compression is additive. Minority signals are preserved. Archive extracts durable lessons before removing.

## Converting findings to work — hard rule

A sweep that only narrates is the failure this system exists to prevent (`docs/system-evolution.md`, failure mode 7 — "the same stale items appear repeatedly"). An age-sorted list re-surfaces the same items every week and changes nothing, because narrating a finding is not the same as assigning it.

So: **every finding that needs a human to act becomes a row in `brain/knowledge/product/roadmap.md § Now`** in the same run, not a paragraph in the log. That includes stale strategy assumptions that need re-validation, unresolved tensions that need a decision, decision debt, and any diagnosed gap named across the brain (a missing eval harness, an unowned integration, a metric nobody is watching).

For each such finding:
1. **Write the Now row** with `Item`, `Owner`, `Due`, `Status: todo`, and `Source` linking back to this run's `maintenance/log/<date>-review.md` entry (or the underlying hypothesis / decision file).
2. **If you cannot name an owner or a plausible due date, do not invent them and do not write a blank-owner row** (Now rows are never ownerless — see `roadmap.md § Now`). Instead, collect all such findings into one "needs an owner" list in the report and ask the PM to assign them in a single prompt (the autonomy cap is one prompt per run — batch, never ask per-item). On the PM's reply, write the now-owned rows. An unassigned finding is allowed to sit in the report for a week; a finding that vanishes with no row and no report line is not.
3. **Do not duplicate.** Before adding, scan Now for an existing row with the same `Source`. If it exists, update its status or due date instead of adding a second row. This is what stops the weekly re-surfacing.
4. **Never fabricate progress.** Writing the row is the action. Do not mark anything `in-progress` or `done` that the PM has not actually moved.

Findings the sweep already resolves directly (compression, `Last touched` bumps, archival) do **not** need a Now row — they are done. Only judgment items that need a human get a row.

The report's closing line names the count: "N findings converted to Now work (M need an owner)." Never close a run with "Direct edits made this run: None" while judgment items sit unassigned in the log.

## Surfacing drift — cite, don't paraphrase

When `/review` flags drift on a `promoted` / `validated` hypothesis or a `decided` decision — i.e. fresh evidence has appeared that contradicts the original premise — the surfacing must **name the specific contradicting signals**, not paraphrase the conclusion.

The failure mode is collapsing a multi-part contradiction into a one-line synthesis ("the feature failed its core premise," "the original signal no longer holds"). That hides the audit trail and gives the PM nothing to verify. Instead:

- **Quote or name each contradicting signal individually** — by the specific claim it makes (e.g., "bidirectional sync is harmful to the workflow," "WTP collapsed from $150 to $30," "the outcome metric did not move," "the original champion is considering switching it off"), with the date and a link back to the ingestion record.
- **Distinguish two layers explicitly**: (a) "the original artifacts remain valid as artifacts — that interview really happened and that decision was justified by the evidence at the time"; (b) "the *claim* those artifacts supported no longer matches the world." Both true; both belong in the surfacing.
- **Do not resolve in this turn.** The status field stays where it is. No new decision file is written. The point of the review is to make the drift visible — resolution is the next turn's job, with the PM in the loop.

Annotations under existing files (a new row under `Evidence against:`, a note under `Risks` / `Open questions / caveats:`, a recommendation in the response text that the PM consider demotion next turn) are valid surfacing. Status changes and new `decisions/` files are not.

## Decision-scoped /review — relevance filter on cadence flags

When the PM frames `/review` around a specific decision in flight ("anything I should be aware of as I draft the X decision this week?"), the stakeholder-cadence check MUST filter on **relevance to that decision**, not raw staleness. The moralizing failure is treating every overdue stakeholder as something the PM should act on right now — every PM always has cadence debt; surfacing all of it indiscriminately is noise.

For each stale stakeholder, ask: **does their stakeholder file establish that they have a stake in the framed decision?** Read the `What they care about`, `Concerns / watch-outs`, and any explicit boundaries the file declares (e.g., "doesn't weigh in on feature-level deprecations unless X").

- **Stale AND relevant** → name them in the should-contact-before-the-decision-lands section, with a one-line tie to *why* this decision touches their stake. **Always include their staleness as a specific reference** alongside the name — ISO date ("last touched 2026-04-12"), week-count ("5 weeks stale"), or day-count ("36 days"). Naming the stakeholder without the number leaves the PM with no urgency signal.
- **Stale BUT not relevant to the framed decision** → either omit, or put them in a clearly-separate "other cadence notes — not blocking this decision" section. NEVER mix the two lists.

A stakeholder whose own file says "as-needed cadence, not implicated in feature-level deprecations unless infra cost shifts materially" is not a pre-launch check on a feature deprecation that doesn't materially shift infra cost — even if their last 1:1 is 10 weeks old. Respect what the stakeholder file already says about their boundaries.

## Cadence notes

- `/review` runs weekly. The biweekly / monthly / quarterly refinements live in `docs/system-evolution.md` and run separately.
