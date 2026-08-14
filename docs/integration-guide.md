# Integration Guide

How to use PM Cortex commands together effectively — building workflows where each output feeds the next.

## The Core Pattern

```
Generate (command) → Store (/ingest) → Use context (next command)
```

Commands generate structured output. `/ingest` stores it in the brain. Future commands draw on accumulated context. This creates a flywheel where the brain gets sharper over time.

## Workflow Patterns

### Pattern 1: Discovery → Documentation

**Goal:** Run discovery, store findings, write PRD with context

```bash
# Step 1: Discovery
/discover AI meeting summarizer for remote teams

# Output: Ideas, assumptions, experiment candidates
# ↓

# Step 2: Store in brain
/ingest [paste discovery output]

# Brain updates:
# - brain/hypotheses/meeting-summarizer.md (assumptions)
# - brain/knowledge/users/insights.md (user signals)
# ↓

# Step 3: Write PRD with accumulated context
/prd-draft AI meeting summarizer

# Claude automatically loads:
# - brain/knowledge/strategy.md (your priorities)
# - brain/hypotheses/meeting-summarizer.md (assumptions)
# - Generates PRD with your context baked in
```

**Why this works:**
- Discovery establishes assumptions
- Brain tracks them with evidence
- PRD references existing hypotheses instead of inventing new ones

---

### Pattern 2: Interview → Synthesis → Planning

**Goal:** Customer interviews inform planning

```bash
# Step 1: Ingest interview transcript
/ingest
[paste interview transcript]

# Brain:
# - Copies to brain/source/interviews/
# - Synthesizes to brain/ingestion/interviews/
# - Promotes patterns to brain/knowledge/users/insights.md
# - Strengthens hypothesis evidence
# ↓

# Step 2: Review synthesis
# Check: brain/ingestion/interviews/[file].md
# Check: brain/hypotheses/[feature].md (evidence updated?)
# ↓

# Step 3: Plan next quarter
/plan-okrs

# Claude loads:
# - brain/knowledge/strategy.md
# - brain/knowledge/users/insights.md
# - Recent brain/decisions/
# - Active brain/hypotheses/
# Generates OKRs aligned to evidence
```

**Why this works:**
- Raw interviews are synthesized once
- Patterns accumulate in knowledge/
- Planning draws on accumulated evidence, not scattered notes

---

### Pattern 3: Hypothesis Tracking Loop

**Goal:** Track feature hypotheses from ideation through launch

```bash
# Step 1: Risk scan
/risk Mobile app feature

# Shows hypothesis gaps across 5 risk areas
# ↓

# Step 2: Open hypotheses
/hypothesize Mobile app feature

# Brain creates: brain/hypotheses/mobile-app.md
# ↓

# Step 3: Design experiments
/discover experiments existing

# Designs tests for top-risk hypotheses
# ↓

# Step 4: Track results
/ingest [experiment results]

# Updates hypothesis evidence:
# - Evidence for: 0.4 → 0.7
# - Decision trigger: if confidence > 0.8...
# ↓

# Step 5: Make decision when trigger fires
/decide

# Logs to brain/decisions/ with evidence trail
# ↓

# Step 6: Weekly check
/review

# Flags:
# - Hypotheses with no evidence in 30+ days
# - Decisions whose reversal condition triggered
```

---

### Pattern 4: Stakeholder Cadence

**Goal:** Maintain stakeholder relationships with context

```bash
# Monday: Prep for 1:1s
/prep john-cto

# Shows:
# - Last touchpoint: 3 weeks ago
# - Open ask: "When will enterprise auth ship?"
# - Last concern: "Performance regression in Q1"
# - Suggested questions
# ↓

# After meeting: Capture and ingest notes
/meeting-notes
[paste meeting transcript]

/ingest [meeting-notes output]

# Updates:
# - brain/stakeholders/john-cto.md (touchpoint logged)
# - brain/decisions/ (if commitments made)
# - brain/hypotheses/ (if new concerns raised)
# ↓

# Friday: Review cadence
/review

# Flags:
# - High-influence stakeholders not touched in 3+ weeks
# - Suggests who to reach out to
```

---

### Pattern 5: Weekly Habit Loop

**Goal:** Sustainable practice

```
Monday:
├── /prep [stakeholder-1]
├── /prep [stakeholder-2]
└── /daily-plan

Tuesday–Thursday:
├── /ingest (as artifacts arrive)
│   ├── Interview transcripts
│   ├── Meeting notes
│   └── Market signals
└── /discover, /prd-draft, /decide (as needed)

Friday:
└── /review (20-minute sweep)
    ├── Flags stale content
    ├── Suggests updates
    └── Archives resolved items
```

---

### Pattern 6: Feature Lifecycle

**Goal:** Track a feature from idea to ship

```bash
# Discovery
/discover [feature idea]
/ingest [discovery output]

# Strategy alignment
/strategy-check [feature]

# Planning
/prd-draft [feature]
/ingest [PRD]

# Review panel (all 7 sub-agents)
/prd-review-panel

# Execution
/prioritize [backlog]
/sprint plan

# During development
/ingest [weekly progress updates]
/ingest [user feedback from beta]

# Pre-launch
/pre-mortem [feature]
/risk [feature]
/launch-checklist [feature]

# Post-launch
/ingest [launch metrics]
/ingest [customer reactions]

# Review
/review  # Check hypothesis confirmation
```

**Full audit trail:**
- `brain/source/` has every artifact
- `brain/ingestion/` has every synthesis
- `brain/hypotheses/` tracks evidence
- `brain/decisions/` logs commitments
- `brain/knowledge/` accumulates patterns

---

## Advanced Patterns

### Context-Aware PRDs

```bash
# Thin PRD (no context)
/prd-draft Mobile app
# → Generic structure, invented assumptions

# Context-loaded PRD
# 1. Ensure brain has context
ls brain/knowledge/strategy.md       # ✓ Strategy defined
ls brain/knowledge/users/insights.md # ✓ User insights
ls brain/hypotheses/mobile-app.md    # ✓ Assumptions tracked

# 2. Write PRD (loads all context automatically)
/prd-draft Mobile app
# → PRD with your north-star metric, user pain points,
#   testable assumptions, and past decisions baked in
```

### Cross-Feature Learning

```bash
# Feature A learnings ingested
/ingest [Feature A post-launch analysis]

# Brain updates:
# - brain/knowledge/users/insights.md ("Onboarding friction" pattern)

# Months later, planning Feature B
/risk Feature B
# Claude notices: "Feature A showed onboarding friction causes 40% drop
# (see brain/knowledge/users/insights.md). Consider testing this first."
```

### Strategy Drift Detection

Weekly `/review` catches:
- Recent decisions diverging from `brain/knowledge/strategy.md`
- Features on roadmap misaligned to north-star
- Hypotheses contradicting strategic bets

Example flag:
> "Decision 2026-04-15-defer-realtime contradicts Strategy § Priority #2: 'Enable real-time collaboration'. Intentional pivot or oversight?"

---

## Best Practices

### 1. Initialize Brain First

Before running any command:
```bash
/pm-brain  # 6-batch interview → scaffold
```

Commands load brain context. An empty brain produces generic output.

### 2. Ingest Workflow Outputs

After any command that generates insights:
```bash
/discover → /ingest [output]
/prd-draft → /ingest [PRD]
/user-research-synthesis → /ingest [synthesis]
```

### 3. Let Brain Update Automatically

When you `/ingest`, the brain routes to multiple files simultaneously — one interview can update 6 files. Don't manually edit brain files; let the system propagate.

### 4. Review → Act → Ingest

Weekly review loop:
```bash
/review            # Friday sweep — flags issues
[Fix or run commands]
/ingest [whatever you fixed]   # Store the fix
```

### 5. Trust Provenance Tags

When Claude references evidence, check the tag:
- `[ingestion/...]` → high trust, walk the link
- `(stakeholder-verbal)` → medium trust, verify if needed
- `(intuition)` → low trust, validate soon

---

## Common Anti-Patterns

### ❌ Running Commands Without Ingesting

```bash
# Bad
/discover [idea]
[read output, don't ingest]
/prd-draft [same idea]
# → PRD has no context from discovery
```

```bash
# Good
/discover [idea]
/ingest [output]
/prd-draft [idea]
# → PRD uses discovery context
```

### ❌ Skipping Weekly Review

```
Week 1: ✓ /review
Week 2: ✓ /review
Week 3: [skip]
Week 4: [skip]
# → Stale content accumulates, memory rots
```

### ❌ Over-Promoting

```bash
# Bad: One customer quote → update knowledge/
/ingest [single quote]
# → Immediately promoted (one source is not a pattern)

# Good: Wait for the promotion gate
/ingest [customer 1]
/ingest [customer 2]
/ingest [customer 3]
# → After 3 independent observations, brain promotes automatically
```

---

## Troubleshooting

**"Commands don't use brain context"**
- Check you're in brain directory: `ls CLAUDE.md`
- Verify `brain/knowledge/strategy.md` is populated
- Re-run `/pm-brain` if scaffold is missing

**"Too much duplication"**
- Run `/review` → compression pass
- Let brain synthesize recurring patterns
- Archive resolved items

**"Context overload"**
- Brain loads only relevant areas per command, not everything
- If still heavy, split large insight files by theme
- Archive shipped features 90+ days old

**"Lost track of hypotheses"**
- Check: `brain/hypotheses/INDEX.md`
- Run: `/review` → flags actives with no evidence
- Use: `/risk [feature]` → shows hypothesis coverage

## Next Steps

- [PM Brain Guide](pm-brain-guide.md) — Memory layer details
- [Architecture Overview](architecture.md) — System design
- [Quickstart Guide](quickstart.md) — Get started
