# Unified PM-OS

A complete Product Management Operating System for Claude Desktop. One install. One command. A self-evolving second brain that gets smarter every time you work.

## What's inside

- **Three-tier memory brain** — source (immutable) → ingestion (synthesized) → knowledge (promoted patterns)
- **45 local commands** — from `/daily-plan` to `/gtm-strategy`, organized by how often you use them
- **8 standalone skills** — auto-selected by Claude based on context
- **7 sub-agent personas** — engineer, designer, executive, legal, customer, skeptic, UXR reviewer
- **Style personalization** — Claude learns how you write and think from observing your edits
- **Use-to-evolve** — the brain updates automatically as byproduct of your daily PM work

## Installation

1. Open Claude Desktop
2. Go to Marketplace → search "Unified PM-OS" → Install
3. Create a new directory for your product (e.g. `~/my-product/`)
4. Open that directory in Claude Desktop
5. Run `/pm-brain` — Claude will interview you and scaffold your full brain

## After setup

All 45 commands are available immediately as local slash commands in your project directory.

```
/daily-plan          Start every morning here
/ingest              Feed any artifact into the brain
/prep [name]         Brief before any stakeholder conversation
/prd-draft           Write a context-aware PRD
/decide              Log a decision with full evidence trail
/review              Weekly brain sweep (run every Friday)
```

See your project's `CLAUDE.md` for the complete command reference and operating manual.

## Updating

When a new version is available:
1. Update the plugin in Claude Desktop Marketplace
2. Open your project directory
3. Run `/pm-brain upgrade` — new commands and skills are added automatically. Your brain data is never touched.

## Structure

```
unified-pm-os/
├── .claude-plugin/marketplace.json    Plugin registry
└── plugins/pm-brain/                  The pm-brain plugin
    ├── commands/pm-brain.md           Entry point command
    ├── skills/pm-brain.md             Skill version
    ├── prompts/                       Interview and setup prompts
    ├── scaffold/                      Templates copied to PM's project
    │   ├── brain/                     Three-tier memory system
    │   ├── .claude/commands/          45 PM commands
    │   ├── .claude/skills/            8 standalone skills
    │   ├── .claude/sub-agents/        7 reviewer personas
    │   └── CLAUDE.md                  Operating manual
    ├── CHANGELOG.md
    └── UPGRADE_MANIFEST.md
```
