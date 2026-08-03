---
description: Create a structured meeting agenda with attendee context, time boxes, pre-reads, and success criteria
argument-hint: "<meeting topic> with <attendees>"
---

# /meeting-agenda -- Meeting Agenda

Generate a focused, time-boxed meeting agenda with attendee context pulled from stakeholder profiles, pre-reads linked to relevant PRDs, and clear success criteria.

## Invocation

```
/meeting-agenda decision on X with Y and Z   → Decision meeting agenda
/meeting-agenda 1:1 with Maya                → Weekly 1:1 agenda
/meeting-agenda sprint planning              → Sprint planning with eng team
/meeting-agenda                              → I'll ask for topic and attendees
```

## Brain Context

Load if available:
- `brain/stakeholders/<slug>.md` for each named attendee — communication style, open asks, recent interaction history, and what they care about
- `brain/knowledge/strategy.md` — to frame the meeting's strategic purpose
- `brain/knowledge/product/` area relevant to the meeting topic — for pre-read context
- `brain/decisions/` — recent decisions that may affect this meeting's discussion
- Recent `brain/ingestion/meetings/` for recurring meetings — open items from last time

## Workflow

### Step 1: Load Brain Context

Identify attendees from the input. Load each attendee's stakeholder profile to surface their communication preferences, open asks, and last interaction date. Check for prior meetings on the same topic.

### Step 2: Apply the Skill

Apply the **meeting-agenda** skill.

Use stakeholder profiles to tailor the agenda format (detail-heavy for analytical stakeholders, BLUF for executives). Reference recent meeting context to carry forward open items. Link relevant PRDs or strategy docs as pre-reads.

### Step 3: Save Output

Save agenda to `outputs/<YYYY-MM-DD>-<meeting-slug>-agenda.md`.

The skill also generates a matching meeting notes stub — save it alongside the agenda for use with `/meeting-notes` after the meeting.

### Step 4: Offer Follow-ups

- "Agenda sent? Run `/meeting-notes` after the meeting to capture outcomes."
- "Want to add stakeholder context to your brain? Run `/ingest` on any new profiles."
- "Need a pre-read doc for this meeting? Run `/prd-draft` or `/status-update`."
