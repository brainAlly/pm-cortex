---
description: Batch process all of today's meetings into a consolidated action list with cross-meeting conflict detection
argument-hint: "<paste all transcripts>"
---

# /meeting-cleanup -- Meeting Day Cleanup

Process all of today's meeting transcripts at once — summarize each, extract all decisions and action items, deduplicate across meetings, and flag cross-meeting conflicts.

## Invocation

```
/meeting-cleanup   → Paste all transcripts; I'll process them in batch
```

## Brain Context

Load if available:
- `brain/stakeholders/<slug>.md` for each attendee across all meetings — to enrich action item owners and surface stakeholder load
- `brain/knowledge/strategy.md` — to tag decisions against strategic pillars
- `brain/decisions/` — to flag conflicts with prior committed decisions
- Recent `brain/ingestion/meetings/` — to surface carry-over items from previous meetings on the same topics

## Workflow

### Step 1: Load Brain Context

Identify all unique attendees across the pasted transcripts. Load their stakeholder profiles. Check `brain/decisions/` for any topics that had prior decisions — flag if today's meetings contradict them.

### Step 2: Apply the Skill

Apply the **meeting-cleanup** skill.

Use stakeholder profiles to enrich action item owners with context (role, capacity, communication style). Cross-reference decisions against brain knowledge to detect conflicts. Surface recurring topics with severity tags.

### Step 3: Save Output

Save to `outputs/meeting-notes/cleanup-<YYYY-MM-DD>.md`.

After saving, offer: "Route decisions and action items to brain? Run `/ingest`."

### Step 4: Offer Follow-ups

- "Want to create tickets from these action items? Run `/create-tickets`."
- "Want to send a team recap? Run `/slack-message`."
- "Run `/ingest` to route decisions and insights into your brain."
- "Run `/decide` for any significant decisions that need formal documentation."
