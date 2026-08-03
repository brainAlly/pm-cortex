# PM Cortex

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Commands](https://img.shields.io/badge/Commands-45-blue)](#available-commands)
[![Skills](https://img.shields.io/badge/Standalone%20Skills-8-green)](#standalone-skills)
[![Sub-Agents](https://img.shields.io/badge/Sub--Agents-7-purple)](#sub-agents)

**One plugin. One command. A self-evolving second brain that gets smarter every session.**

PM Cortex is a unified PM operating system for Claude Desktop — a three-tier memory brain wired directly to 45 PM commands, 8 auto-selected skills, and 7 sub-agent reviewers. Every meeting, interview, and decision feeds the brain. The brain makes every future command more context-aware. The system compounds.

---

## What's Inside — 58 Items Total

### 🧠 The Brain — Three-Tier Memory

Plain markdown files. No cloud, no vector DB, no API keys. Lives in your project directory, version-controlled, readable by you.

| Tier | Path | What it stores |
|---|---|---|
| **Source** | `brain/source/` | Verbatim copies of every artifact ingested. Immutable audit trail. |
| **Ingestion** | `brain/ingestion/` | Synthesized observations from source. Provenance-tagged working memory. |
| **Knowledge** | `brain/knowledge/` | Promoted durable patterns — confirmed across 3+ independent sources. |
| **Hypotheses** | `brain/hypotheses/` | Evidence-weighted bets on what's true, organized by risk area. |
| **Decisions** | `brain/decisions/` | Append-only log. Every decision has an evidence trail and a reversal condition. |
| **Stakeholders** | `brain/stakeholders/` | Per-person state: open asks, concerns, last touchpoint, influence level. |
| **Style** | `brain/style/` | Your voice, your frameworks, your thinking patterns — learned and updated automatically. |

### ⚡ 45 Commands — All Brain-Aware

Every command loads relevant brain context before executing and updates the brain after. The same `/prd-draft` command on day 1 and day 90 produces different outputs — because on day 90 it knows your users, your decisions, your strategy, and your writing style.

Organized by how often you'll reach for them: [Daily](#daily--8-commands) · [Weekly](#weekly--6-commands) · [Sprint Cadence](#sprint-cadence--14-commands) · [Occasional](#occasional--11-commands) · [Strategic](#strategic--6-commands)

### 🔍 8 Standalone Skills — Auto-Selected

You never type these. Claude invokes them automatically when context signals they're relevant — opportunity solution trees during discovery, market sizing when evaluating a segment, sentiment analysis when you paste qualitative data.

### 👥 7 Sub-Agent Reviewers

Seven personas that tear apart your work from every angle. Suggested automatically after significant outputs. Run all seven simultaneously with `/prd-review-panel`.

---

## Installation

### 🚀 Interactive Install (Recommended)

Paste this into Claude Desktop and let Claude handle everything:

```
Help me install PM Cortex.

Check if the brainAlly/pm-cortex marketplace is added. If not, add it with:
claude plugin marketplace add brainAlly/pm-cortex

Then install: claude plugin install pm-brain@pm-cortex

After installation, guide me through creating a brain directory, opening it in Claude Desktop, and running /pm-brain to initialize.
```

[See the full interactive guide with guided next steps →](INSTALL.md)

---

### Manual Install

```bash
# Add the marketplace
claude plugin marketplace add brainAlly/pm-cortex

# Install
claude plugin install pm-brain@pm-cortex
```

---

## Quick Start

### 1. Initialize Your Brain

```bash
# Create a directory for your product brain (one per product)
mkdir ~/my-product-brain

# Open it in Claude Desktop → Code tab → Add Folder
# Then run:
/pm-brain
```

PM Cortex will run a 6-batch interview covering your product, stakeholders, active work, data sources, operating preferences, and writing style. Then it scaffolds your complete brain, populates it from your answers, and commits.

### 2. Build the Habit Loop

The system compounds only if you feed it. The minimum viable habit:

```
Morning           → /daily-plan
After meetings    → /meeting-notes  then  /ingest
Before 1:1s       → /prep [stakeholder]
Every Friday      → /review
```

### 3. Let the Brain Do the Work

After two weeks of honest use, the brain knows your product context. Commands stop asking for it:

```bash
# Day 1: you explain context
/prd-draft  →  "tell me about the feature..."

# Day 30: it already knows
/prd-draft  →  pulls from brain/knowledge/product/ + hypotheses/ + style/
```

---

## How It Works

```
Your Daily Work                    The Brain
───────────────                    ─────────

Meeting ends                       brain/source/meetings/
  ↓ /meeting-notes           →     YYYY-MM-DD-[slug].md  (verbatim)
  ↓ /ingest                  →     brain/ingestion/meetings/  (synthesized)
                                   brain/stakeholders/[slug].md  (touchpoint logged)
                                   brain/hypotheses/[feature].md  (if a bet surfaced)

Customer interview               
  ↓ /user-interview          →     brain/ingestion/interviews/
  ↓ 3+ matching signals      →     brain/knowledge/users/insights.md  (promoted)

Decision made
  ↓ /decide                  →     brain/decisions/YYYY-MM-DD-[slug].md
                                   brain/hypotheses/[feature].md  (status updated)

Friday
  ↓ /review                  →     Stale knowledge flagged
                                   Hypothesis hygiene checked
                                   Promotion candidates surfaced

Next PRD                           
  ↓ /prd-draft               ←     Loads knowledge/ + hypotheses/ + style/
  ↓ /prd-review-panel        ←     7 sub-agents review in one pass
  ↓ /create-tickets          ←     Formatted tickets with full feature context
```

**The pattern:** daily work feeds the brain → the brain makes future commands smarter → smarter commands surface better insights → better insights feed the brain. It's a flywheel, not a tool.

---

## Available Commands

### Daily — 8 Commands

The commands you'll reach for every working day. These should feel automatic within two weeks.

| Command | When | What you get |
|---|---|---|
| `/daily-plan` | Every morning | Focused day plan from your OKRs, open priorities, and calendar. LNO-classified so you know exactly what moves the needle. |
| `/ingest` | After every meeting, interview, or signal | Source saved, synthesized, patterns checked for promotion, brain updated automatically. |
| `/prep [stakeholder]` | Before any stakeholder conversation | One-page brief: their last touchpoint, open asks, unresolved concerns, suggested questions. |
| `/meeting-agenda` | Before scheduling or running any meeting | Structured agenda with goal, attendees, time blocks, and required pre-reads. |
| `/meeting-notes` | After any meeting | Decisions, action items, key insights — filed into ingestion and fed into the brain pipeline. |
| `/slack-message` | Drafting team communication | Clear, actionable message calibrated to recipient type (announcement, request, update, escalation). |
| `/status-update` | Stakeholder reporting | BLUF-format update with health indicator, progress summary, risks, and next steps. |
| `/prioritize` | When the task list is overwhelming | Task list classified by LNO with recommended focus order and the language to defend it. |

### Weekly — 6 Commands

| Command | When | What you get |
|---|---|---|
| `/weekly-plan` | Monday morning | Next week's priorities aligned to OKRs, with capacity planning and day-by-day theme. |
| `/weekly-review` | Friday afternoon | Personal retrospective: wins, misses, key learnings, carry-forwards. |
| `/review` | Friday — after weekly-review | Brain maintenance sweep: stale knowledge flagged, hypothesis hygiene checked, promotion candidates surfaced. |
| `/meeting-cleanup` | End of any day with 3+ meetings | Batch processes all day's meeting notes into one digest with cross-meeting action items. |
| `/decide` | When a significant decision crystallizes | Decision logged with evidence trail, reversal condition, and stakeholder sign-off. Produces a shareable stakeholder document. |
| `/strategy-check` | Bi-weekly | Drift report: recent decisions and ingestion vs. current strategy. Surfaces tensions — never edits strategy silently. |

### Sprint Cadence — 14 Commands

| Command | When | What you get |
|---|---|---|
| `/prd-draft` | Starting any new feature spec | Modern PRD built from your knowledge/, users/, and style/ preferences. Auto-updates the brain on completion. |
| `/prd-review-panel` | After any PRD draft | Consolidated review from all 7 sub-agent perspectives in one pass. |
| `/discover` | Before committing to build a feature | Full discovery sequence: OST → identify assumptions → prioritize assumptions → design experiments. |
| `/risk` | Before sprint starts | 5-area risk scan (value, usability, feasibility, viability, other). Drafts hypothesis stubs for uncovered risk areas. |
| `/hypothesize` | When opening new assumptions on a feature | Evidence-weighted hypothesis file created or refreshed, organized by 5 risk areas with confidence scores. |
| `/sprint` | Sprint planning session | Sprint goal, ticket breakdown, capacity check, and definition of done — informed by open hypotheses and current roadmap. |
| `/retro` | End of sprint | Full sprint retrospective: what went well, what didn't, what to change, action items with owners. |
| `/create-tickets` | After PRD is approved | Formatted tickets with user story, acceptance criteria, and definition of done — via Linear/Jira MCP or formatted text. |
| `/user-interview` | After user research sessions | Structured interview synthesis saved to ingestion, with pattern check and hypothesis updates. |
| `/user-research-synthesis` | After a batch of 3+ interviews | Insight clusters, persona refinements, and opportunity areas extracted from multiple sessions. |
| `/impact-sizing` | Before prioritization decisions | Feature value quantified via driver trees and 4-step sizing. Returns estimate with confidence bounds. |
| `/experiment-decision` | Before setting up any experiment | Structured decision: A/B test or just ship? Outputs experiment design if test is warranted. |
| `/feature-metrics` | When defining success for a feature | STEDII-validated metric plan with primary metric, guardrail metrics, and leading/lagging indicator pairs. |
| `/launch-checklist` | 1–2 weeks before any release | Launch readiness: stakeholder comms, rollout gates, monitoring setup, go/no-go criteria, rollback plan. |

### Occasional — 11 Commands

| Command | When | What you get |
|---|---|---|
| `/ideate` | Stuck on a hard problem | 3–7 directions grounded in your users/, hypotheses/, and decisions/. Each tagged with supporting evidence and evidence gaps. |
| `/plan` | New major objective arrives | Six-block execution plan: what we know, assumptions vs. evidence, who to interview, hypotheses to open, experiments to run, decision points. |
| `/competitor-analysis` | Monthly competitive monitoring | Deep analysis updating your knowledge/market/competitors/. Includes 7 Powers moat assessment. |
| `/interview-guide` | Before planning a user research sprint | JTBD-based interview guide with opening, probe, and closing questions organized by topic. |
| `/journey-map` | Redesigning an experience | Dual-mode journey map: emotional journey + touchpoint analysis. Identifies friction and opportunity gaps. |
| `/activation-analysis` | When activation rates are a problem | Activation funnel mapped through Setup → Aha → Habit framework. Bottleneck scores and prioritized recommendations. |
| `/retention-analysis` | When retention is declining | Cohort analysis with retention curves by segment, churn factor identification, and retention driver ranking. |
| `/ab-test-analysis` | After an experiment concludes | Statistical analysis with confidence intervals, segment breakdown, and ship/iterate/kill recommendation. |
| `/experiment-metrics` | Setting up a new experiment | STEDII framework applied to candidate metrics. Returns a scorecard with recommended primary metric and guardrails. |
| `/pre-mortem` | 1–2 weeks before any major launch | Imagined post-failure analysis with structured risk mitigation plan from identified failure modes. |
| `/sql-queries` | Deep-diving into data | PM-appropriate SQL queries for your data warehouse. Includes query explanation and interpretation guidance. |

### Strategic — 6 Commands

| Command | When | What you get |
|---|---|---|
| `/plan-okrs` | Quarterly OKR planning | OKR structure: objectives with measurable key results, leading indicators, and team alignment check. |
| `/outcome-roadmap` | Quarterly roadmap refresh | Outcome-based roadmap with now/next/later structured around measurable outcomes, not features. |
| `/define-north-star` | When the team lacks metric alignment | North Star Metric validated against sub-metrics, data requirements, and strategic alignment. |
| `/expansion-strategy` | Planning revenue expansion | Upsell, cross-sell, and account growth playbook with prioritized expansion levers. |
| `/gtm-strategy` | New product launch or market entry | Full GTM strategy: ICP, positioning, channel selection, motion design (PLG/SLG/MLG), and success metrics. |
| `/growth-loops` | PLG strategy work | Growth loop design: acquisition loop, engagement loop, monetization loop. |

---

## Standalone Skills — Auto-Selected

You never invoke these directly. Claude pulls them in when context signals they're needed.

| Skill | Triggered when |
|---|---|
| `opportunity-solution-tree` | Structuring discovery work |
| `market-sizing` | Evaluating a new market or segment |
| `porters-five-forces` | Competitive strategy or industry structure analysis |
| `pricing-strategy` | Pricing decisions surface in strategy or feature discussions |
| `lean-canvas` | Early-stage product thinking or new initiative framing |
| `sentiment-analysis` | Processing large volumes of qualitative feedback |
| `user-personas` | Research synthesis requires persona framing or updating |
| `swot-analysis` | Strategic planning or competitive positioning discussions |

---

## Sub-Agents

Seven reviewer personas. Never auto-run — Claude suggests the relevant ones after producing significant outputs, and you confirm which to run. Run all seven simultaneously with `/prd-review-panel`.

| Sub-Agent | Persona | Tears apart |
|---|---|---|
| `engineer-reviewer` | Senior engineer, 8+ years | Feasibility, complexity, technical debt, edge cases, timeline accuracy |
| `designer-reviewer` | Senior product designer, 6+ years | UX flow, accessibility, mobile, empty/error states, design system consistency |
| `executive-reviewer` | VP Product / CPO, 10+ years | Strategic alignment, ROI, resource allocation, opportunity cost |
| `legal-advisor` | Product counsel | GDPR/CCPA, data collection, ToS exposure, ADA compliance |
| `customer-voice` | The actual customer | Value clarity, discoverability, ease of use, trust |
| `skeptic` | Devil's advocate | Assumption stress-testing, problem validation, scope creep |
| `uxr-analyst` | UX researcher | Research quality, validation gaps, evidence vs. assumption |

Invoke any sub-agent by reading its file:
```
Read .claude/sub-agents/engineer-reviewer.md, then review this PRD: [paste PRD]
```

---

## Architecture

```
pm-cortex/
├── .claude-plugin/
│   └── marketplace.json          # Plugin registry (brainAlly/pm-cortex)
│
└── plugins/pm-brain/
    ├── .claude-plugin/
    │   └── plugin.json           # Plugin identity
    ├── commands/
    │   └── pm-brain.md           # Entry point — orchestrates init and upgrade
    ├── skills/
    │   └── pm-brain.md           # Skill entry point
    ├── prompts/                   # Adaptive reasoning loaded per phase
    │   ├── mode-detection.md     # Greenfield vs. migration vs. active-repo
    │   ├── interview.md          # 6-batch interview + placeholder mapping
    │   ├── migration.md          # Bulk-ingest pre-existing PM artifacts
    │   └── post-scaffold.md      # Self-test, link verification, contradictions
    ├── scaffold/                  # Deterministic static structure — copied as-is
    │   ├── .claude/
    │   │   ├── commands/         # 45 slash commands (local to project)
    │   │   ├── skills/           # 54 skill files (8 standalone + methodology)
    │   │   ├── sub-agents/       # 7 reviewer personas
    │   │   └── hooks/
    │   │       └── validate_brain_file.py   # PostToolUse schema validator
    │   ├── brain/
    │   │   ├── source/           # Immutable verbatim copies
    │   │   ├── ingestion/        # Synthesized working memory
    │   │   ├── knowledge/        # Promoted durable facts
    │   │   │   ├── strategy.md
    │   │   │   ├── product/      # features/, roadmap.md, metrics.md
    │   │   │   ├── users/        # personas.md, insights.md
    │   │   │   ├── market/       # competitors/, landscape.md
    │   │   │   └── org/          # team.md, rituals.md, tools.md
    │   │   ├── hypotheses/       # Evidence-weighted bets by feature
    │   │   ├── decisions/        # Append-only decision log
    │   │   ├── stakeholders/     # Per-person state
    │   │   └── style/            # writing.md, frameworks.md, patterns.md
    │   ├── templates/            # Blank starters for PRDs, OKRs, retros, etc.
    │   ├── rules/                # PM's process rules (discovery, data, etc.)
    │   ├── docs/                 # Guidebook, examples, advanced guides
    │   ├── maintenance/          # /review run logs
    │   ├── outputs/              # Generated artifacts (PRDs, plans, analyses)
    │   └── CLAUDE.md             # Operating manual — the brain's instruction set
    ├── CHANGELOG.md
    └── UPGRADE_MANIFEST.md
```

---

## What Makes This Different

**Not a notes app.** Opinionated three-tier structure with evidence standards, schema validation, and weekly maintenance built in. Raw signals don't become knowledge until they've been confirmed independently.

**Not a chatbot with memory.** Memory lives in your repo as plain markdown — readable, diffable, portable. You own it. Claude is the engine, not the storage.

**Not a vector database.** Everything is grep-able by you. No embeddings, no similarity search, no black-box retrieval.

**Not a skill library bolted onto a brain.** Commands and brain are one system. `/prd-draft` doesn't call the brain as a side effect — it loads your knowledge, hypotheses, and style *before* it does anything, then updates them after. The brain isn't optional context; it's the input.

**Not autonomous PM.** Judgment stays with you. The system handles cross-referencing, provenance tagging, pattern detection, and link maintenance. You decide what to promote, commit, and ship.

**Local-first.** No cloud sync. No API keys beyond Claude itself. Works anywhere Claude Desktop works.

---

## Updating

When a new version is available in Claude Desktop Marketplace:

```
1. Update the plugin in Claude Desktop
2. Open your project directory
3. Run: /pm-brain upgrade
```

New commands and skills are added automatically. Your brain data — everything in `brain/` — is never touched by upgrades.

---

## Requirements

- **Claude Desktop** with plugin support
- **Git** (for version control of your brain)
- **Python 3.7+** (for the schema validation hook)

---

## Support

- 🐛 **Bug reports:** [Open an issue](https://github.com/brainAlly/pm-cortex/issues)
- 💡 **Feature requests:** [Open an issue](https://github.com/brainAlly/pm-cortex/issues)
- 📖 **Questions:** [Discussions](https://github.com/brainAlly/pm-cortex/discussions)

---

**Star this repo** ⭐ if it helps you build better products.

---

**Version:** 1.0.0 | **Maintainer:** BrainAlly
