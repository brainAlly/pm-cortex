# Upgrade Manifest — PM Brain

This file is read by `/pm-brain upgrade`. Each version section lists exactly which files to copy, replace, or create. Paths are relative to this plugin directory as source and the PM's project directory as destination.

No file contents are embedded here. All content is sourced from the plugin directory files.

The upgrade command applies all version sections above the PM's current `.pm-os-version` in order, from oldest to newest.

---

## v1.0.0 — Initial scaffold

This is the baseline version. No upgrade actions — this version is installed by `/pm-brain` scaffold, not by upgrade.

If a PM's `.pm-os-version` is missing or unreadable, treat as v0.0.0 and apply all versions.

---

<!-- Future versions added here when released. Format:

## v1.1.0

### NEW COMMANDS
- Copy scaffold/.claude/commands/[name].md → .claude/commands/[name].md

### UPDATED COMMANDS
- Replace .claude/commands/[name].md with scaffold/.claude/commands/[name].md

### NEW SKILLS
- Copy scaffold/.claude/skills/[name].md → .claude/skills/[name].md

### NEW SUB-AGENTS
- Copy scaffold/.claude/agents/[name].md → .claude/agents/[name].md

### SCAFFOLD CHANGES
- Create [directory]/ if not exists
- Copy scaffold/[path] → [destination path]

### CLAUDE.md UPDATES
- Replace content between PM-OS:START and PM-OS:END markers with scaffold/CLAUDE.md system sections

-->
