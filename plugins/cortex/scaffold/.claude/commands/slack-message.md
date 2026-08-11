---
description: Draft a contextual Slack message with the right tone and framing for the recipient
argument-hint: "<recipient> <situation>"
---

# /slack-message -- Slack Message

Craft a Slack message that matches the recipient's communication style, includes the right context, and gets the response you need.

## Invocation

```
/slack-message                              → I'll ask who and what
/slack-message ask Sarah about timeline     → Targeted draft
/slack-message escalate blocker to manager  → Escalation draft
/slack-message share meeting recap to #eng  → Channel update
```

## Brain Context

Load if available:
- `brain/stakeholders/<recipient-slug>.md` — communication preferences, decision style, relationship history, and what they care about
- `brain/style/writing.md` — your voice and banned words so the message sounds like you
- Recent `brain/ingestion/meetings/` or `brain/decisions/` relevant to the topic — for specific context references instead of generic framing

## Workflow

### Step 1: Load Brain Context

Identify the recipient from the input. Load their stakeholder profile — tone, detail preference, and seniority determine everything about how this message is framed. Load `brain/style/writing.md` so the draft matches your voice.

### Step 2: Apply the Skill

Apply the **slack-message** skill.

Use the stakeholder profile to select tone (direct, friendly, formal, tactful, urgent) and format (BLUF for executives, conversational for peers). Reference specific meeting dates or decisions from brain context instead of vague "our conversation."

### Step 3: Output

Display the drafted message. Do not save to file — Slack messages are ephemeral. Offer to iterate on tone or length.

### Step 4: Offer Follow-ups

- "Need a full status update instead? Run `/status-update`."
- "Following up on meeting outcomes? Run `/meeting-notes` first to get the details."
- "Want to update the stakeholder's profile with context from this exchange? Run `/ingest`."
