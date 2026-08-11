# PM Cortex Documentation

Welcome to the PM Cortex documentation. This guide covers the unified PM operating system — one plugin, one brain, 58 items working together.

## Quick Navigation

### Getting Started
- [⚡ Quickstart Guide](quickstart.md) — Get up and running in 10 minutes
- [🏗️ Architecture Overview](architecture.md) — Understand how everything fits together

### Core Reference
- [🧠 PM Brain Guide](pm-brain-guide.md) — Memory layer, commands, and file structure
- [🔗 Integration Guide](integration-guide.md) — Workflow patterns and advanced usage

## What is PM Cortex?

PM Cortex is a unified product management operating system installed as a single Claude Desktop plugin. It combines a three-tier memory brain, 45 orchestrated commands, 8 domain-specific skills, and 7 specialist sub-agents into one cohesive system.

**Contextual Memory (Brain)**
A three-tier memory system that persists across every session. Raw artifacts are preserved verbatim, synthesized into structured working memory, and promoted to durable knowledge once a pattern has been confirmed across three or more independent sources.

**Domain-Specific Skills**
Eight modules the agent invokes automatically based on the task at hand — market sizing, sentiment analysis, OKR frameworks, and more. They operate transparently without PM intervention.

**Orchestrated Commands**
Forty-five slash commands invoked directly by the PM. Each executes a structured multi-step workflow, loads brain context before running, and updates the memory layer after. Organized by frequency: daily, weekly, sprint, occasional, and strategic.

**Sub-Agent Reviewers**
Seven independent agents — senior engineer, product designer, executive, legal advisor, customer voice, devil's advocate, and UX researcher — suggested by the system after significant outputs and confirmed by the PM before running.

## What's Inside

| Layer | Count | Invoked by |
|---|---|---|
| Commands | 45 | PM (slash command) |
| Skills | 8 | Agent (auto) |
| Sub-agents | 7 | Agent suggests, PM confirms |
| **Total** | **58** | |

## Common Tasks

| Task | Documentation |
|---|---|
| First-time setup | [Quickstart Guide](quickstart.md) |
| Initialize your brain | [Quickstart Guide](quickstart.md#step-2-initialize-your-brain) |
| Understand the memory system | [PM Brain Guide](pm-brain-guide.md) |
| Run daily workflows | [PM Brain Guide](pm-brain-guide.md#the-core-commands) |
| Integrate commands together | [Integration Guide](integration-guide.md) |
| Understand the architecture | [Architecture Overview](architecture.md) |

## Installation

```
claude plugin marketplace add brainAlly/pm-cortex
claude plugin install pm-brain@pm-cortex
```

See [Quickstart Guide](quickstart.md) for full setup including brain initialization.

## Support

- 🐛 [Report Issues](https://github.com/brainAlly/pm-cortex/issues)
- 📖 [Setup Guide](https://100x-pm.vercel.app/)
- 📧 [Contact](mailto:engg@brainally.io)
