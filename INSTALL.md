# Interactive Installation Guide

## One-Prompt Installation

Instead of following manual installation steps, you can paste this single prompt into Claude Desktop and let Claude handle everything:

---

### 🚀 Copy & Paste This Prompt:

```
Help me install PM Cortex.

Context: PM Cortex is a unified PM operating system — a self-evolving second brain with three-tier memory, 45 commands, 8 auto-selected skills, and 7 sub-agent reviewers, all in one plugin.

Your tasks:
1. Check if the brainAlly/pm-cortex marketplace is added. If not, add it with:
   claude plugin marketplace add brainAlly/pm-cortex

2. Install the plugin:
   claude plugin install pm-brain@pm-cortex

3. After installation, provide these EXACT setup steps:

   "NEXT STEPS TO SET UP YOUR PM CORTEX BRAIN:

   1. Create a directory for your product brain:
      - Use ONE directory per product (don't mix multiple products)
      - Example: mkdir ~/my-product-brain
      - Or create it through your file explorer

   2. Open that directory in Claude Desktop:
      - Click the 'Code' tab in Claude Desktop
      - Click 'Add Folder' or 'Open Folder'
      - Select your brain directory (the empty folder you just created)

   3. Initialize your brain by running: /pm-brain
      - I will ask you 6 batches of questions about:
        * Batch A: Your company, product, stage, and strategic priorities
        * Batch B: Your stakeholders, friction points, and standing rituals
        * Batch C: Active features, your next big bet, and recently shipped work
        * Batch D: Data sources, customer interviews, and competitor signals
        * Batch E: How autonomous you want the system to be and what's off-limits
        * Batch F: How you write, which frameworks you lean on, and how you think

   4. After initialization, here's what you'll have:

      YOUR FULL ARSENAL — 58 items total:

      45 COMMANDS — everything from daily planning to quarterly strategy, all wired
      to your brain. You type them, the system already knows your product.

      8 STANDALONE SKILLS — Claude invokes these automatically when the context
      calls for it. You never have to think about them.

      7 SUB-AGENT REVIEWERS — engineer, designer, executive, legal, customer,
      skeptic, and UX researcher — ready to tear apart your PRD from every angle.

      THE BRAIN — three tiers of memory that get smarter every session:
      brain/source/       → verbatim audit trail of everything you've ingested
      brain/ingestion/    → synthesized working memory (meetings, interviews, signals)
      brain/knowledge/    → promoted durable facts (confirmed across 3+ sources)
      brain/hypotheses/   → evidence-weighted bets on what's true
      brain/decisions/    → append-only log of what you've committed to and why
      brain/stakeholders/ → per-person state: asks, concerns, last touchpoint
      brain/style/        → your voice, your frameworks, your thinking patterns

   5. The 8 commands you'll reach for every single day:

      /daily-plan      → Your morning clarity ritual. Pulls your OKRs, open
                         priorities, and calendar into a focused day plan — LNO
                         classified, so you know exactly what moves the needle.

      /ingest          → The system's heartbeat. Paste any artifact — meeting notes,
                         interview transcript, competitor screenshot, Slack thread —
                         and the brain routes, synthesizes, and files it. Run this
                         after everything.

      /prep            → Before any 1:1 or stakeholder meeting, run this. You get
                         one page: their last touchpoint, open asks, unresolved
                         concerns, and the three questions you should actually ask.

      /meeting-agenda  → Never walk into a meeting without one again. Goal, time
                         blocks, attendees, pre-reads — structured and ready before
                         you even open the calendar invite.

      /meeting-notes   → After any meeting. Decisions, action items, key insights —
                         filed into brain/ingestion/meetings/ and fed into the
                         pipeline automatically.

      /slack-message   → Write it once, send it right. Calibrates tone to the
                         recipient (announcement, request, update, escalation) and
                         matches your communication style from brain/style/.

      /status-update   → BLUF-format update with a health indicator, what moved,
                         what's at risk, and what's next. Your exec team will
                         actually read this one.

      /prioritize      → When everything feels urgent and nothing is clear. Runs
                         your task list through LNO, surfaces what to focus on,
                         and gives you the language to defend it.

   6. Daily habit that keeps the system alive:
      - Morning: /daily-plan
      - After every meeting: /meeting-notes then /ingest
      - Before every 1:1: /prep [stakeholder name]
      - Every Friday: /review (maintenance sweep — this is what keeps the brain
        from going stale)

   The system compounds. Every /ingest makes the next /prep smarter. Every
   /decide makes the next /ideate sharper. Give it two weeks of honest use
   and it will know your product better than most people on your team."

Start by checking the marketplace status.
```

---

## What Happens Next

Claude will:

### Step 1: Check Marketplace
```bash
# Claude checks if marketplace exists
claude plugin marketplace list

# If not found, adds it
claude plugin marketplace add brainAlly/pm-cortex
```

### Step 2: Install
```bash
claude plugin install pm-brain@pm-cortex
```

### Step 3: Confirmation

Claude tells you:
- ✅ What got installed
- 📋 The `/pm-brain` command is now available
- 📖 Next steps to initialize your brain

### Step 4: Next Steps Guidance

Claude guides you:
1. Create a directory for your brain
2. Open it in Claude Desktop
3. Run `/pm-brain` to initialize (6-batch interview)
4. Start using the 8 daily commands

---

## Why This Approach?

**Benefits:**
- ✅ No manual terminal commands
- ✅ Claude explains each step
- ✅ Immediate help if something goes wrong
- ✅ Educational — you understand what's happening

**Traditional approach vs Interactive:**

| Traditional | Interactive Prompt |
|------------|-------------------|
| Read docs | Paste one prompt |
| Open terminal | Claude does it |
| Run commands manually | One install command |
| Check installation | Claude confirms |
| Read next steps | Claude guides you |

---

## Troubleshooting

**"Command not found: claude"**
→ Install Claude Code CLI first: [Installation guide](https://docs.anthropic.com/claude/docs/cli-installation)

**"Marketplace already exists"**
→ No problem! Claude will skip that step and proceed to installation.

**"I don't see the /pm-brain command"**
→ Make sure the plugin is installed: `claude plugin list`
→ Reinstall if needed: `claude plugin install pm-brain@pm-cortex`

**"I want to change what I installed"**
→ You can run the prompt again. Installing the plugin again won't erase your brain data.

---

## For Advanced Users

If you prefer direct CLI commands without the interactive prompt:

```bash
claude plugin marketplace add brainAlly/pm-cortex
claude plugin install pm-brain@pm-cortex
```

Then open your brain directory in Claude Desktop and run `/pm-brain`.
