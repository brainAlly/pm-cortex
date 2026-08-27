# PM Brain Guide

The memory layer of PM Cortex — a three-tier system that captures, organizes, and maintains product context across every session.

## What is the Brain?

The brain is a set of plain markdown files inside `brain/` in your project directory. No cloud, no vector DB — just files you can read, edit, and version control. Every PM Cortex command reads from and writes to this directory, so context accumulates automatically as you work.

## The Memory Hierarchy

```
brain/
│
├── source/              Tier 1 — Immutable
│   ├── interviews/      Raw transcripts, never edited
│   ├── meetings/
│   ├── market/
│   └── adhoc/
│
├── ingestion/           Tier 2 — Synthesized working memory
│   ├── interviews/      Provenance-tagged observations
│   ├── meetings/
│   ├── market/
│   └── adhoc/
│
├── knowledge/           Tier 3 — Durable state (tagged Tier: stated / confirmed)
│   ├── strategy.md      North-star, priorities, tensions
│   ├── product/         Features, metrics, roadmap
│   ├── users/           Personas, segments, insights
│   ├── market/          Landscape, competitors, trends
│   └── org/             Team, rituals, tools
│
├── hypotheses/          Feature-level risk tracking
├── decisions/           Append-only commitment log
├── stakeholders/        People state and touchpoints
└── style/               PM's writing and thinking patterns
```

### Tiers of Knowledge: Stated vs. Confirmed

Durable knowledge carries a `Tier:` marker so the system can weight it honestly:

- **`Tier: stated`** — asserted by you or resting on a single source, not yet verified. Everything seeded at setup starts here — it is your model of the world, not established fact.
- **`Tier: confirmed`** — the same claim after **3+ independent, external sources** back it (customer interviews, analytics, third-party data). Your own restatements don't count; three versions of your own opinion are still one source.

This matters because of the evidence hierarchy: **direct customer evidence outranks a `stated` claim.** When a customer contradicts something you stated at setup, the customer wins and the stated claim gets revised — the system will never quietly keep your assumption on top just because you wrote it down first. Only `confirmed` knowledge, which already cleared the evidence bar, outranks a fresh customer signal. `/review` promotes `stated → confirmed` as the evidence accumulates.

### Provenance System

Every claim in the brain carries a source tag:

| Tag | Trust Level |
|---|---|
| `[ingestion/<path>]` | Highest — documented and synthesized |
| `[source/<path>]` | High — raw original artifact |
| `(stakeholder-verbal, name, date)` | Medium — heard but not recorded |
| `(intuition, PM, date)` | Low — your hunch, validate soon |
| `(industry-knowledge)` | Low — background assumption |

Tag provenance honestly. The system values accuracy over false rigor.

## The Core Commands

These six commands form the daily interface with the brain. They are 6 of the 45 total PM Cortex commands.

### `/ingest` — Feed Artifacts into the Brain

Routes artifacts into the brain based on shape detection.

**Input types:**
- **Interview** — Customer calls, user research, sales conversations
- **Meeting** — 1:1s, reviews, roadmap discussions
- **Market** — Competitor articles, screenshots, analyst notes
- **Adhoc** — Quick notes, Slack threads, email insights

**Usage:**
```
/ingest
[paste transcript or drag file]
```

**What happens:**
1. Copies original → `brain/source/`
2. Synthesizes → `brain/ingestion/` with tagged observations
3. Promotes patterns → `brain/knowledge/`, `brain/hypotheses/`, `brain/decisions/`, `brain/stakeholders/`
4. Reports what was updated

**Example flow:**
```
Interview transcript
     ↓
brain/source/interviews/2026-04-22-acme.md (immutable)
     ↓
brain/ingestion/interviews/2026-04-22-acme.md (synthesis)
     ↓
brain/knowledge/users/insights.md (promoted pattern)
brain/hypotheses/feature-x.md (evidence added)
brain/stakeholders/john-ops.md (touchpoint logged)
```

---

### `/prep` — Brief Before Meetings

Generates a one-page brief before meeting a stakeholder.

**Usage:**
```
/prep john-cto
```

**Output:**
- Their last touchpoint date
- Open asks from them
- Last unresolved concern
- Suggested questions to ask

After the meeting, `/ingest` the notes to update their file.

---

### `/review` — Weekly Maintenance Sweep

Six automated checks across the entire brain.

**The Six Checks:**
1. **Stale knowledge** — Files not updated in 6+ weeks
2. **Stale evidence** — Old market intel, interviews, assumptions
3. **Hypothesis hygiene** — Actives with no evidence, pending decisions
4. **Stakeholder cadence** — High-influence people not touched in 3+ weeks
5. **Knowledge synthesis** — Recurring patterns and contradictions
6. **Archival sweep** — Shipped features, resolved hypotheses

**Usage:**
```
/review
```

**When to run:** Every Friday (20 minutes). Skip it for a month and the brain rots.

---

### `/ideate` — Evidence-Based Solution Synthesis

Surfaces 3–7 solution directions based on accumulated evidence.

**Usage:**
```
/ideate How do we reduce churn in onboarding?
```

**What it loads:**
- `brain/knowledge/strategy.md`
- `brain/knowledge/users/insights.md`
- Active `brain/hypotheses/`
- Recent `brain/decisions/`

**Output:** Directions tagged with supporting evidence, gaps identified, experiments suggested.

---

### `/risk` — Five-Area Risk Scan

Scans a feature across 5 risk areas and drafts hypothesis stubs for gaps.

**Five risk areas:**
1. **Value** — Will users want this?
2. **Usability** — Can users use this?
3. **Feasibility** — Can we build this?
4. **Viability** — Should we build this?
5. **Other** — Regulatory, partnership, etc.

**Usage:**
```
/risk Real-time collaboration feature
```

---

### `/plan` — Six-Block Execution Plan

Drafts a structured plan from objective to execution.

**Six blocks:**
1. What we know
2. Assumption vs evidence
3. Who to interview
4. Hypotheses to open
5. Experiments to run
6. Decision points

**Usage:**
```
/plan Launch enterprise tier by Q3
```

---

## Brain File Structures

### `brain/hypotheses/[feature-slug].md`

```markdown
## H1. Value risk
**Evidence for:** 0.7
- Row 1 with provenance tag [ingestion/interviews/...]
**Evidence against:** 0.3
**Decision trigger:** if confidence > 0.8, proceed

## H2. Usability risk
...
```

### `brain/decisions/YYYY-MM-DD-slug.md`

```markdown
- Status: decided
- Driver: [what prompted this]
- What we decided: [the commitment]
- Evidence: [provenance-tagged trail]
- **What would reverse this:** [explicit reversal condition]
```

### `brain/stakeholders/[person-slug].md`

```markdown
- Role & influence level
- Current asks
- Last unresolved concern
- Touchpoint log with dates
```

### `brain/style/writing.md`

Captured automatically as the PM edits outputs. Includes preferred frameworks, tone, communication style, and thinking patterns. Updated when the PM edits output in the same direction 3+ times — the agent asks to confirm before writing.

---

## Best Practices

### 1. Ingest Daily

The longer you wait, the more context you lose. Ingest within 24 hours:
- After every customer interview
- After stakeholder 1:1s
- When you see a market signal
- Quick notes from Slack or email

### 2. Run `/review` Every Friday

20 minutes. Skip it for a month and the system rots.

### 3. Tag Provenance Honestly

Don't launder intuition through fake `[ingestion/...]` tags. If it's a hunch, tag it `(intuition, PM, date)`. The system values honesty over fake rigor.

### 4. Promote Deliberately

Anything you assert directly into `brain/knowledge/` lands as `Tier: stated` — useful working context, but not confirmed. Let `/review` promote it to `Tier: confirmed` only once 3+ independent external sources back it. Don't hand-flip a claim to confirmed to make it feel settled; that reintroduces the exact bias the tiers exist to prevent.

### 5. Archive Regularly

Shipped features inactive 90+ days? Archive them. Resolved hypotheses? Archive. The brain stays sharp by letting go of the irrelevant.

---

## Common Patterns

### Pattern: Customer Interview Flow

```bash
# 1. Conduct interview, ingest transcript
/ingest
[paste transcript]

# 2. Check what was updated
# brain/ingestion/interviews/[file].md
# brain/knowledge/users/insights.md
# brain/hypotheses/[feature].md

# 3. Prep for next interview
/prep [same customer in 4 weeks]
```

### Pattern: Feature Launch Cycle

```bash
# 1. Risk scan before starting
/risk Mobile app feature

# 2. Track hypotheses during development
# (ingestion updates them automatically)

# 3. Log decision to ship
/decide

# 4. Post-launch: ingest metrics
/ingest [analytics snapshot]

# 5. Review hypothesis confirmation
# Check: brain/hypotheses/mobile-app.md
```

### Pattern: Weekly Cadence

```
Monday:   /prep for stakeholder 1:1s
Tue–Thu:  /ingest artifacts as they arrive
Friday:   /review (full sweep)
```

---

## Troubleshooting

**"Brain dirs missing after /pm-brain init"**
- Verify `brain/` exists as a subdirectory: `ls brain/`
- If missing, re-run `/pm-brain` — it will detect the incomplete scaffold

**"Too many files, context overload"**
- Run `/review` to archive stale content
- Use compression (synthesis of recurring patterns)
- Split large insight files by theme

**"Provenance tags confusing"**
- Start simple: `[ingestion/...]` for documented, `(stakeholder-verbal)` for heard, `(intuition)` for hunches
- The vocabulary becomes natural after 2 weeks

**"Not sure what to ingest"**
- Ingest everything: interviews, meetings, market signals, quick notes
- Let the brain sort it — shape detection is automatic
- Over-ingestion beats under-ingestion

## Next Steps

- [Integration Guide](integration-guide.md) — Workflow patterns combining multiple commands
- [Architecture Overview](architecture.md) — How the full system is structured
- [Quickstart Guide](quickstart.md) — Get started from scratch
