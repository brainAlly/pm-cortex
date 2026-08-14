# Commands

Operator-facing verbs. Each command is a thin spec: input, files to load, files to update, what to surface. The agent reads the spec, executes against the brain, and reports back per `CLAUDE.md § Operating loop`.

45 commands across 8 groups. Run by name — e.g. `/daily-plan`, `/prd-draft`.

---

## Daily & Weekly Rhythm

| Verb | When to run it |
| --- | --- |
| [`/daily-plan`](./daily-plan.md) | Start of day — pulls meetings, tasks, active PRDs, and stakeholder context into a prioritized plan |
| [`/weekly-plan`](./weekly-plan.md) | Monday morning — set Top 3 priorities aligned with quarter goals and active PRD pipeline |
| [`/weekly-review`](./weekly-review.md) | Friday — synthesize progress, wins, blockers, and learnings against the weekly plan |
| [`/prioritize`](./prioritize.md) | Classify tasks using the LNO framework and build a focused weekly plan with calendar blocking |

---

## Memory & Ingestion

| Verb | When to run it |
| --- | --- |
| [`/ingest`](./ingest.md) | Any new artifact lands — interview, meeting notes, market signal, ad-hoc note |
| [`/review`](./review.md) | Weekly maintenance sweep — surfaces drift, compression opportunities, stale hypotheses, and decisions |
| [`/meeting-notes`](./meeting-notes.md) | After any meeting — summarize transcript into decisions, action items, and follow-ups |
| [`/meeting-cleanup`](./meeting-cleanup.md) | End of day — batch process all of today's meetings into a consolidated action list |
| [`/user-interview`](./user-interview.md) | After 1–3 user interviews — process transcripts into insight cards with validated/challenged/new theme labels |
| [`/user-research-synthesis`](./user-research-synthesis.md) | After 4+ interviews — synthesize into a unified report with cross-interview patterns and strategic recommendations |

---

## Stakeholder & Communication

| Verb | When to run it |
| --- | --- |
| [`/prep`](./prep.md) | Before a 1:1, exec review, roadmap discussion, or any stakeholder conversation |
| [`/meeting-agenda`](./meeting-agenda.md) | Before a meeting — structured agenda with attendee context, time boxes, pre-reads, and success criteria |
| [`/slack-message`](./slack-message.md) | Draft a contextual Slack message with the right tone and framing for the recipient |
| [`/status-update`](./status-update.md) | Generate stakeholder status updates for different audiences from your brain context |

---

## Discovery & Strategy

| Verb | When to run it |
| --- | --- |
| [`/discover`](./discover.md) | Starting a new feature — full discovery cycle from ideation through assumption mapping to experiment design |
| [`/plan`](./plan.md) | A new objective lands — turn it into discovery questions, interviews, experiments, hypotheses, decision points |
| [`/strategy-check`](./strategy-check.md) | Bi-weekly — drift check between recent decisions/hypotheses/ingestion and `knowledge/strategy.md` |
| [`/define-north-star`](./define-north-star.md) | Identify and validate your North Star Metric — the single number that captures your product's core value |
| [`/plan-okrs`](./plan-okrs.md) | Quarterly — brainstorm team-level OKRs aligned with company objectives |
| [`/outcome-roadmap`](./outcome-roadmap.md) | Build an outcome-based roadmap with now/next/later structured around measurable outcomes |
| [`/ideate`](./ideate.md) | A problem needs solution directions grounded in existing evidence and hypotheses |
| [`/hypothesize`](./hypothesize.md) | Generate or refresh hypotheses for a feature — pre-ship (5 risk areas) or post-ship (data-derived) |
| [`/decide`](./decide.md) | Log a decision — draft the complete decision file from the evidence trail, surface for PM sign-off |
| [`/risk`](./risk.md) | A feature or plan needs the 5-area risk scan; drafts hypothesis stubs for uncovered gaps |
| [`/pre-mortem`](./pre-mortem.md) | Before shipping — identify what could go wrong before it does |

---

## Product & Execution

| Verb | When to run it |
| --- | --- |
| [`/prd-draft`](./prd-draft.md) | Create a modern PRD using brain context for strategy, users, hypotheses, and active decisions |
| [`/prd-review-panel`](./prd-review-panel.md) | Run multi-agent PRD review from 7 perspectives — Engineering, Design, Exec, Legal, UXR, Skeptic, Customer |
| [`/create-tickets`](./create-tickets.md) | Break a PRD or feature spec into scoped engineering tickets with estimates, acceptance criteria, and dependencies |
| [`/sprint`](./sprint.md) | Sprint lifecycle — plan a sprint, run a retrospective, or generate release notes |
| [`/retro`](./retro.md) | Structured retrospective — Start/Stop/Continue, 4Ls, or Sailboat format with brain write-back |
| [`/launch-checklist`](./launch-checklist.md) | Comprehensive launch checklist with critical path, owners, and dependencies for a feature |
| [`/impact-sizing`](./impact-sizing.md) | Quantify feature value using a 4-step driver tree with confidence levels |

---

## Research & Analysis

| Verb | When to run it |
| --- | --- |
| [`/interview-guide`](./interview-guide.md) | Create a JTBD-based interview guide focused on gaps in your existing research |
| [`/journey-map`](./journey-map.md) | Map user or customer journeys to surface friction points, emotional lows, and opportunity gaps |
| [`/activation-analysis`](./activation-analysis.md) | Diagnose your activation funnel using the Setup → Aha → Habit framework |
| [`/retention-analysis`](./retention-analysis.md) | Analyze retention curves, identify churn drivers, and recommend interventions using cohort analysis |
| [`/feature-metrics`](./feature-metrics.md) | Define success metrics for a feature using the STEDII framework |
| [`/experiment-metrics`](./experiment-metrics.md) | Select trustworthy experiment metrics using STEDII before launching any test |
| [`/experiment-decision`](./experiment-decision.md) | Decide whether to A/B test, ship + monitor, or just ship using the reversibility decision tree |
| [`/ab-test-analysis`](./ab-test-analysis.md) | Analyze A/B test results — statistical significance, sample size validation, and ship/extend/stop recommendations |
| [`/sql-queries`](./sql-queries.md) | Generate SQL queries from natural language — supports BigQuery, PostgreSQL, MySQL, and more |

---

## Market & Competitive

| Verb | When to run it |
| --- | --- |
| [`/competitor-analysis`](./competitor-analysis.md) | Analyze the competitive landscape — identify competitors, compare strengths and weaknesses, find differentiation opportunities |
| [`/gtm-strategy`](./gtm-strategy.md) | Full GTM — ICP, positioning, channel selection, motion design (PLG/SLG/MLG), and success metrics |
| [`/expansion-strategy`](./expansion-strategy.md) | Build an expansion playbook for upsell, cross-sell, and account growth with NRR decomposition |
| [`/growth-loops`](./growth-loops.md) | Design and analyze acquisition, engagement, and monetization growth loops |

---

## Setup & Maintenance

| Verb | When to run it |
| --- | --- |
| `/pm-brain upgrade` | Built-in — upgrades the PM Brain scaffold to the latest version (no command file; runs directly) |

---

## Conventions

- Every command loads before acting and updates after. No blind drafting.
- Every command ends by surfacing 2–4 bullets per `CLAUDE.md § Operating loop`.
- `/prep` is read-only at call time. Run `/ingest` after the conversation.
- Commands respect `CLAUDE.md § Operating preferences § Autonomy mode`. Under `propose and wait`, drafts are presented for approval before saving.
- All file paths in each spec are relative to the brain root.
