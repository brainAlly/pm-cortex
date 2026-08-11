---
name: pm-brain
description: Initialize or upgrade a Unified PM Brain — a three-tier memory brain with 45 commands, 8 skills, 7 sub-agents, and a style personalization layer for a product operator (PM, product lead, founder, or anyone accountable for one product or initiative) doing judgment-heavy work with scattered inputs. Detects greenfield vs. migration mode, runs a focused interview (6 batches including style), copies the deterministic scaffold into the working directory, populates placeholders from interview answers, runs a self-test, and commits. Run `/pm-brain upgrade` to apply updates from a newer plugin version. Use when invoked via `/pm-brain` or when the user asks to set up a PM Brain.
---

# PM Brain — Skill

This skill scaffolds and initializes a PM Brain in the current working directory. The scaffold is deterministic (static files copied as-is from `scaffold/`). The reasoning is adaptive (loaded from `prompts/` per phase).

## Architectural split

| Layer | Where it lives | Why |
| --- | --- | --- |
| **Static structure** — schemas, CLAUDE.md, INDEX.md, folder tree, file templates | `scaffold/` | Deterministic. Same every time. No generation needed. |
| **Adaptive reasoning** — mode detection, migration, interview, post-scaffold self-test | `prompts/` | Probabilistic. Depends on what's in the directory and what the PM says. |
| **Orchestration** — when to do what | This file | Glue. |

Behavior evolves independently from structure. Schemas can change without touching reasoning. Reasoning can improve without rewriting schemas.

## When to invoke

- Operator runs `/pm-brain` (or pastes a setup request like "set up a PM Brain here").
- Operator asks to add a PM Brain to an existing directory of PM artifacts.

Do **not** invoke this skill for routine PM Brain operations after init (ingestion, prep, review). Those are handled by the seeded `CLAUDE.md` operating manual in the target repo.

## Workflow

### 1. Detect mode

Load `prompts/mode-detection.md`. Inspect the current working directory. Decide: **greenfield** (empty), **migration** (PM artifacts present), or **active-repo** (working repo — pause and ask).

Announce the detected mode to the operator in one line. For active-repo mode, do not proceed without confirmation.

### 2. If migration mode

Load `prompts/migration.md`. **Copy** (do not move) pre-existing PM artifacts into a `source/` folder. Bulk-ingest with epistemic caution. Record cross-document conflicts for the post-scaffold contradictions block.

### 3. Run the interview

Load `prompts/interview.md`. Ask the 6 batches (greenfield) or only the gaps not covered by source artifacts (migration). Confirm back what you heard before scaffolding.

### 4. Copy the scaffold

Copy **every file and folder** from `scaffold/` into the current working directory — including the hidden `.claude/` directory (hooks + per-brain settings) and dotfiles (`.gitignore`, `.gitkeep`). Preserve structure exactly.

Use the form of copy that picks up dotfiles by default:

- **Bash:** `cp -R scaffold/. <dest>/`  (the trailing `/.` is what makes dotfiles come along)
- **PowerShell:** `Copy-Item -Recurse -Force scaffold\* <dest>\` followed by `Copy-Item -Recurse -Force scaffold\.* <dest>\` (the second pass picks up `.claude/` and `.gitignore`; `Copy-Item -Recurse scaffold\*` alone *will* silently drop them)

**After copying, run this verification checklist. Every item must pass before proceeding.**

Root-level files and folders:
- [ ] `.claude/` directory exists
- [ ] `.claude/commands/` exists and contains 45 `.md` files
- [ ] `.claude/skills/` exists and contains 54 subdirectories (each with a `SKILL.md`)
- [ ] `.claude/sub-agents/` exists and contains 7 `.md` files
- [ ] `.claude/hooks/validate_brain_file.py` exists
- [ ] `.claude/settings.json` exists
- [ ] `.gitignore` exists
- [ ] `.pm-os-version` exists
- [ ] `CLAUDE.md` exists
- [ ] `brain/` exists as a **directory** (not individual brain folders at root)
- [ ] `docs/` exists with `examples/` and `advanced/` subdirectories
- [ ] `maintenance/` exists
- [ ] `outputs/` exists
- [ ] `rules/` exists
- [ ] `templates/` exists and contains 6 `.md` files

Brain subdirectories (all must be **inside `brain/`**, never at project root):
- [ ] `brain/decisions/`
- [ ] `brain/hypotheses/`
- [ ] `brain/ingestion/` (with `meetings/`, `interviews/`, `market/`, `adhoc/` subdirs)
- [ ] `brain/knowledge/` (with `product/`, `users/`, `market/`, `org/` subdirs)
- [ ] `brain/source/` (with `meetings/`, `interviews/`, `market/`, `adhoc/` subdirs)
- [ ] `brain/stakeholders/`
- [ ] `brain/style/`
- [ ] `brain/INDEX.md`

**If any item fails:**
- If `brain/` is missing and `decisions/`, `hypotheses/`, etc. appear at project root — the scaffold was not copied; Claude regenerated the old pm-brain structure from memory. Do NOT proceed. Tell the PM: "Scaffold copy failed — I could not read the plugin's scaffold/ directory and generated the wrong structure from memory. Please verify the plugin is correctly installed in Claude Desktop and retry /pm-brain."
- If `.claude/commands/` is empty or missing — same failure mode. Same message.
- If `templates/` is missing — same failure mode. Same message.
- Do not attempt to recreate missing files from memory. The scaffold is deterministic and must come from the plugin's `scaffold/` directory verbatim.

**Critical rules:**
- Copy in place. The current working directory **is** the project root. Do not create a nested subfolder.
- Brain subdirectories (`decisions/`, `hypotheses/`, `knowledge/`, etc.) live inside `brain/` — never at the project root. If you see them at root, the copy failed.
- Preserve `.gitkeep` files in empty folders.
- Preserve `.claude/hooks/validate_brain_file.py` and `.claude/settings.json` exactly as shipped — they're what makes schema enforcement happen in-loop as the agent edits brain files.
- Do not modify scaffold files at the source. If you need to change a template permanently, edit `scaffold/` and re-version the skill.
- **Never regenerate scaffold content from memory.** If a file or directory is missing after the copy, the copy failed. Fix the copy — do not synthesize replacements.

### 5. Populate placeholders from interview answers

Walk the copied files and substitute interview answers. Use the full **Batch → file mapping** in [`prompts/interview.md § What the answers feed`](./prompts/interview.md) — that table is the canonical destination map. Every Batch answer has a documented home; do not silently drop any.

Highlights:

- `brain/knowledge/strategy.md` — north-star metric, priorities (Batch A). Non-goals start empty if PM didn't volunteer them; flag in next moves.
- `brain/knowledge/product/features/<slug>.md` — one file per active feature (Batch C Q1), populated from the feature schema.
- `brain/knowledge/product/roadmap.md` — Now / Next sections from Batch C.
- `brain/stakeholders/<slug>.md` — one file per stakeholder (Batch B Q1); influence + friction tagged from Batch B Q2.
- `brain/knowledge/org/team.md`, `brain/knowledge/org/rituals.md`, `brain/knowledge/org/tools.md` — from Batch B Q3 + Batch D Q1.
- `brain/knowledge/market/landscape.md` and/or `trends.md` — from Batch D Q3.
- `rules/discovery.md`, `rules/data.md` — from Batch D Q1-2.
- `CLAUDE.md § Operating preferences` — autonomy mode + maintenance cadence (Batch E Q1-2).
- `CLAUDE.md § Off-limits` — Batch E Q3.
- `brain/style/writing.md`, `brain/style/frameworks.md`, `brain/style/patterns.md` — PM's output style, preferred frameworks, and thinking patterns (Batch F).

For schema-templated files: copy the schema structure as-is, fill in what the interview provided, leave the rest with the placeholder comments intact.

**Provenance:** every populated field should be traceable back to either a Batch question or a source artifact. When a value came from a source artifact, link to it inline.

### 6. Post-scaffold self-test

Load `prompts/post-scaffold.md`. Run:

1. Routing self-test (can you route each of the 4 ingestion modes?).
2. Link verification (walk every internal markdown link, fix broken ones).
3. Surface 3-5 immediate next moves.
4. Surface 1-3 contradictions found during scaffolding (or say explicitly "none found").
5. Print the self-test receipt.

### 7. Commit

- Run `git rev-parse --is-inside-work-tree` in the **current working directory**.
- If already a repo: stage all scaffolded files. Single commit titled `feat: initialize PM brain`.
- If not a repo: `git init` in the current working directory, then stage and commit.
- **Never push remotely.** PM controls publication.
- If any git step fails, surface the error and stop. No destructive recovery.

### 8. Hand off

Lead with the habit loop, not the scaffold. See `prompts/post-scaffold.md § 7` for the exact ordering:

1. The three habit actions (ingest today / prep next 1:1 / `/review` Friday) — specific slug + day.
2. 1-3 contradictions surfaced (or "none found").
3. 2-3 scaffold gaps worth filling.
4. One paragraph on what was built.

Do not lead with a folder map or "your scaffold is ready." Lead with what produces value in the next 24 hours.

Then stop and wait for the operator's first real task.

## /pm-brain upgrade

Run this after updating the plugin in Claude Desktop to apply new commands, skills, sub-agents, or scaffold changes to an existing brain.

### 1. Read current version

Read `.pm-os-version` from the project root. If not found, treat as `v0.0.0` and apply all manifest entries.

### 2. Read the manifest

Read `UPGRADE_MANIFEST.md` from the plugin directory. Find all version sections with version numbers greater than the current `.pm-os-version`.

### 3. Show the changelog

Before applying any changes, read `CHANGELOG.md` from the plugin directory and display the release notes for all versions being applied. Ask the PM to confirm: "Ready to apply these updates? (y/n)"

### 4. Apply manifest instructions

For each version above current, in order from oldest to newest:

- **Copy**: Copy the specified file from the plugin directory to the PM's project directory. Create parent directories if they don't exist.
- **Replace**: Overwrite the existing file in the PM's project directory with the plugin version.
- **Create directory**: Create the specified directory if it does not already exist.
- **CLAUDE.md update**: Replace only the content between `<!-- PM-OS:START -->` and `<!-- PM-OS:END -->` markers in the project's `CLAUDE.md`. Never touch content outside those markers — it is the PM's own.

**Critical rule:** Never write to `brain/source/`, `brain/ingestion/`, `brain/knowledge/`, `brain/hypotheses/`, `brain/decisions/`, `brain/stakeholders/`, or `outputs/`. These contain the PM's data and are never modified by upgrades.

### 5. Update version

Write the new version number to `.pm-os-version`.

### 6. Report

Tell the PM exactly what changed:
- New commands added (list them)
- Commands updated (list them)
- New skills or sub-agents
- Any scaffold changes
- "Your brain data was not touched."

---

## Anti-patterns

- **Regenerating scaffold content.** The whole point of `scaffold/` is that it's deterministic. If you find yourself rewriting `CLAUDE.md` or a schema from scratch during init, stop — copy from `scaffold/` instead.
- **Creating a nested `pm-brain/` subfolder.** The current working directory **is** the project root.
- **Skipping the self-test.** Broken links are memory corruption, not cosmetic.
- **Inventing contradictions.** If migration mode found no genuine conflicts, say so. Don't fabricate.
- **Pushing remotely.** PM controls when and where this gets published.

## Files in this skill

```
pm-brain/
├── .claude-plugin/
│   └── plugin.json           # Plugin identity for Claude Desktop
├── commands/
│   └── pm-brain.md           # This file. Orchestration.
├── skills/
│   └── pm-brain.md           # Delegates to commands/pm-brain.md
├── prompts/                  # Adaptive reasoning. Loaded per phase.
│   ├── mode-detection.md
│   ├── migration.md
│   ├── interview.md
│   └── post-scaffold.md
├── scaffold/                 # Deterministic static structure. Copy as-is.
│   ├── .claude/              # Per-brain Claude Code config
│   │   ├── hooks/
│   │   │   └── validate_brain_file.py   # PostToolUse schema validator
│   │   ├── commands/         # 45 slash commands (local to project)
│   │   ├── skills/           # 8 standalone skills (local to project)
│   │   ├── sub-agents/       # 7 sub-agents (local to project)
│   │   └── settings.json     # Wires the hook to Write|Edit
│   ├── .pm-os-version        # Current installed version
│   ├── CLAUDE.md             # Operating manual (PM-OS:START/END markers)
│   ├── brain/
│   │   ├── INDEX.md
│   │   ├── knowledge/        # strategy, product, users, market, org
│   │   ├── stakeholders/
│   │   ├── hypotheses/
│   │   ├── decisions/
│   │   ├── style/            # writing.md, frameworks.md, patterns.md
│   │   ├── source/           # Verbatim audit anchors
│   │   └── ingestion/        # Synthesized records
│   ├── rules/                # PM's process rules (discovery, data, etc.)
│   ├── templates/            # Blank output starters (PRD, OKR, retro, launch checklist, etc.)
│   ├── maintenance/          # /review run logs
│   ├── docs/
│   │   ├── examples/         # Example PRDs and case studies for style reference
│   │   ├── advanced/         # Guides (agents, context management, prompt testing, etc.)
│   │   └── *.md              # Overview, schemas, workflows, system-evolution
│   └── outputs/              # Generated artifacts (PRDs, decks, etc.)
├── CHANGELOG.md
└── UPGRADE_MANIFEST.md
```
