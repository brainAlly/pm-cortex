---

name: release-notes
description: "Generate user-facing release notes from tickets, PRDs, or changelogs. Creates clear, engaging summaries organized by category (new features, improvements, fixes). Use when writing release notes, creating changelogs, announcing product updates, or summarizing what shipped."
user-invocable: false
argument-hint: "[paste tickets, changelog, or PRD]"
---

## Release Notes Generator

Transform technical tickets, PRDs, or internal changelogs into polished, user-facing release notes. Backs the `release-notes` mode of `/sprint`.

### Brain Context

Load if available:
- `brain/style/writing.md` — the product's voice; release notes must match it (tone, reading level, banned words)
- `brain/knowledge/product/roadmap.md` — to confirm what actually shipped this cycle and link entries back to features
- `brain/knowledge/product/features/` — for the user problem each shipped feature solved (lead with that benefit)
- `brain/knowledge/users/personas.md` — to pitch each change to the segment it affects

### Context

You are writing release notes for the shipped work the PM provides.

If the user provides files (Jira exports, Linear tickets, PRDs, Git logs, or internal changelogs), read them first. Cross-reference against `brain/knowledge/product/features/` so the "why it matters" comes from the real user problem, not a guess.

### Instructions

1. **Gather raw material**: Read all provided tickets, changelogs, or descriptions. Extract:
   - What changed (feature, improvement, or fix)
   - Who it affects (which user segment)
   - Why it matters (the user benefit)

2. **Categorize changes**:
   - **New Features**: Entirely new capabilities
   - **Improvements**: Enhancements to existing features
   - **Bug Fixes**: Issues resolved
   - **Breaking Changes**: Anything that requires user action (migrations, API changes)
   - **Deprecations**: Features being sunset

3. **Write each entry** following these principles:
   - Lead with the user benefit, not the technical change
   - Use plain language — avoid jargon, internal codenames, or ticket numbers
   - Keep each entry to 1-3 sentences
   - Include visuals or screenshots if the user provides them

   **Example transformations**:
   - Technical: "Implemented Redis caching layer for dashboard API endpoints"
   - User-facing: "Dashboards now load up to 3× faster, so you spend less time waiting and more time analyzing."

   - Technical: "Fixed race condition in concurrent checkout flow"
   - User-facing: "Fixed an issue where some orders could fail during high-traffic periods."

4. **Structure the release notes**:

   ```
   # [Product Name] — [Version / Date]

   ## Highlights
   [1-2 sentence summary of the most important change]

   ## New Features
   - **[Feature name]**: [1-2 sentence description of what it does and why it matters]

   ## Improvements
   - **[Area]**: [What got better and how it helps]

   ## Bug Fixes
   - Fixed [issue description in user terms]

   ## Breaking Changes (if any)
   - **Action required**: [What users need to do]
   ```

5. **Adjust tone** to match the product's voice from `brain/style/writing.md` — professional for B2B, friendly for consumer, developer-focused for APIs. Follow the voice rules in `CLAUDE.md § Voice and Output Style` (no jargon, benefits before features, 8th-grade reading level for user-facing copy).

### Output

Save to `outputs/<YYYY-MM-DD>-release-notes-<slug>.md`. Offer to reformat for different channels (blog post, in-app, email, Slack announcement). If the user wants HTML or another format, convert accordingly.
