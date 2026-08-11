# Quickstart Guide

Get PM Cortex running in under 10 minutes.

## Prerequisites

- [Claude Desktop](https://claude.ai/download) installed
- Git installed (for brain version control)

## Step 1: Install PM Cortex

**Add the marketplace and install the plugin:**

```
claude plugin marketplace add brainAlly/pm-cortex
claude plugin install cortex@pm-cortex
```

That's it. You now have:
- 45 slash commands available
- 8 domain skills loaded automatically
- 7 sub-agent reviewers ready
- The `/pm-brain` init command to set up your brain

## Step 2: Initialize Your Brain

Create a directory for your brain (this is where all your product context lives):

```bash
mkdir ~/my-product-brain
cd ~/my-product-brain
claude
```

Then run:

```
/pm-brain
```

The system will run a **6-batch interview** to capture your full product context:

- **Batch A:** Company, product, north-star metric
- **Batch B:** Stakeholders and team
- **Batch C:** Current features and roadmap
- **Batch D:** Data sources and processes
- **Batch E:** Operating preferences and autonomy mode
- **Batch F:** Writing style, preferred frameworks, communication patterns

Answer the questions — the system scaffolds your workspace automatically after Batch F and runs a self-test to verify the structure.

## Step 3: Understand What You Have

After initialization, your project directory contains:

```
my-product-brain/
├── brain/          ← three-tier memory (source / ingestion / knowledge)
├── templates/      ← output templates
├── outputs/        ← generated deliverables
├── docs/           ← reference docs
└── .claude/
    ├── commands/   ← 45 slash commands
    ├── skills/     ← 8 auto-invoked domain skills
    └── sub-agents/ ← 7 reviewer personas
```

## Step 4: Try Your First Commands

**Feed your first artifact:**
```
/ingest
[paste a meeting transcript or customer interview]
```

**Prep before a 1:1:**
```
/prep [stakeholder-name]
```

**Draft a PRD:**
```
/prd-draft [feature description]
```

**Run a weekly sweep:**
```
/review
```

**Discover a new feature:**
```
/discover [product idea or problem]
```

## Step 5: Build the Habit

The system compounds over time. The more you ingest, the better every command gets.

**Daily (5 min each):**
- `/daily-plan` — Start the day with context
- `/ingest` — After every meeting or interview
- `/prep` — Before every stakeholder conversation

**Weekly (20 min):**
- `/review` — Every Friday, sweep the entire brain

**As needed:**
- `/prd-draft`, `/decide`, `/discover`, `/risk`, `/ideate` — When the work calls for them

## Common Issues

**"Plugin not found"**
- Verify marketplace is added: `claude plugin marketplace list`
- Retry: `claude plugin install cortex@pm-cortex`

**"Brain dirs missing after init"**
- Verify `brain/` subdirectory exists: `ls brain/`
- If missing, re-run `/pm-brain` — it detects incomplete scaffolds

**"Commands not showing up"**
- Check `.claude/commands/` exists: `ls .claude/commands/`
- Restart Claude Desktop and re-open the project directory

## Getting Help

- 📖 [Setup Guide](https://100x-pm.vercel.app/)
- 🐛 [Report Issues](https://github.com/brainAlly/pm-cortex/issues)
- 📧 [Contact](mailto:engg@brainally.io)
