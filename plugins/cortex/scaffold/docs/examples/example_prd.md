# Voice-to-Task Capture (AI-Assisted)

**Stage:** Solution Review  
**Last Updated:** January 9, 2026  
**Owner:** Maya Rodriguez  
**Status:** In Review

---

## Problem & Bet

**The problem:** A product manager burns close to 45 minutes a day turning meeting notes, Slack threads, and phone memos into structured tasks. What doesn't get written down piles up as a mental backlog of "I really should log that," and most of it never reaches the task system at all.

**Our bet:**
**If we** ship AI-assisted voice-to-task capture,  
**then** PMs will record roughly 3x more action items out of meetings and hallway conversations,  
**because** the work of shaping a raw thought into a task disappears — they speak, and it's filed.

**What supports this:**
- Interview (Marcus, PM at Spotify): "I've got 47 voice memos on my phone that are basically 'remember to follow up with design on X.' I never turn a single one into a task."
- Product data: 68% of the tasks created in our app are pasted in from text that already exists. Only 12% start from voice.
- Survey: 83% of PMs told us they "lose track of action items that come out of informal conversations."

---

## Why This, Why Now

This is the sharpest lever on our Q1 objective, "Make task capture effortless," because it attacks the single biggest source of friction: structuring the task itself.

**Sizing the impact:**
- Reach: every active PM — all 12,000 users
- Revenue: we expect an 8-12% reduction in churn (an action item that never gets captured is the product failing to deliver value)
- Strategic value: **High** — this is our foot in the door for an AI-first roadmap

**What we considered instead:**
- **Polish the manual task form** — leaves the real problem (friction) untouched
- **Transcription only** — hands the user a wall of text and still makes them structure it
- **Plug into Otter.ai or Fireflies** — bolts on an external dependency and never lives inside our workflow

---

## Out of Scope (v1)

Deliberately not in the first release:
- **Auto-assigning tasks** — the user still chooses the owner (the AI could easily pick wrong)
- **Priority suggestions** — we won't guess a priority level; it's too situational
- **Backfilling old audio** — only new captures going forward, not the memo archive
- **Shared/team voice commands** — this is personal capture, not team collaboration (for now)

**Trade-offs we accepted:**
- **Speed over perfect accuracy** — we're tuning for fast capture. 80% accuracy the user can fix in a tap beats 95% accuracy that costs ten seconds.
- **Mobile only** — we launch on phones and validate real usage before touching desktop.

---

## How We'll Measure Success

**Primary metric:** share of tasks created by voice
- Today: 12% of tasks
- Target: 40% of tasks within 8 weeks of launch
- Cadence: measured weekly; expect a slow ramp in weeks 1-2

**Guardrails (must not regress):**
- Task completion rate: stay above 65% (worry: voice-created tasks are lower quality and go undone)
- Task edit rate: stay under 40% (worry: users constantly correcting the AI)
- Crash rate: under 0.1% (worry: voice processing destabilizes the app)

**When we pull the plug:**
If completion falls below 60%, OR edit rate climbs past 50%, we roll back and reassess.

---

## Release Plan

**Approach:** A/B test, 50/50 split

**Phase 1 — 5% of iOS users (Weeks 1-2)**
- Advance if: >20% of those users create at least one voice task, edit rate stays under 50%, and there are no major crashes.

**Phase 2 — 50% of iOS users, A/B (Weeks 3-6)**
- Advance if: the primary metric clears 35%, guardrails hold, and qualitative feedback trends positive.

**Phase 3 — 100% of iOS users (Weeks 7-8)**
- Advance if: the primary metric clears 40%. Begin planning the Android build.

**Rollback:**
If crashes pass 0.5% or the edit rate passes 60%, we disable the feature remotely and ship a hotfix inside 24 hours.

---

## How It Works

### The core flow

1. The user taps the mic (new spot: a persistent bottom-right FAB)
2. They speak plainly: "Remind me to circle back with Elena about the onboarding revamp once she's back from leave"
3. The AI parses it and shows a preview:
   - Task: "Follow up with Elena on the onboarding revamp"
   - Assignee: Elena Park (matched from the team directory)
   - Due date: Jan 15 (inferred from Elena's OOO calendar)
   - Project: Onboarding Revamp (matched to an existing project)
4. The user taps "Create," or edits any field
5. Task filed in under 2 seconds end to end

### Scenario matrix

| Case | What they say | What the app does | Why it matters |
|------|---------------|-------------------|----------------|
| **Clean case** | "Set up a 1:1 with Maria next Tuesday to talk Q2 roadmap" | Task: "1:1 with Maria — Q2 roadmap" · Due: next Tuesday · Assignee: Maria Lopez · Project: Q2 Planning | Resolves the person, infers the date, files under the right project |
| **Fuzzy date** | "Follow up with the design team sometime next week" | Task: "Follow up with design team" · Due: next Monday (start of the range) · Assignee: blank (a group) · Prompt: "Did you mean the [Design Team] tag?" | Degrades gracefully; defaults to the earliest date; asks about the group |
| **Compound request** | "Analyze last sprint's user research and write an exec summary, and also set up a working session with Priya and Tom to walk the themes" | Splits into two tasks — (1) "Analyze Sprint 12 research and draft exec summary," (2) "Schedule working session with Priya and Tom — research themes" — and asks "I heard 2 tasks. Right?" | Breaks apart bundled asks and confirms before filing |
| **Too vague** | "Add that thing we discussed yesterday" | Prompt: "I didn't catch enough to go on — can you say a bit more about what you want to do?" | Refuses thin input and asks for detail |
| **Must refuse** | "Delete all my tasks" | Prompt: "I can't do destructive actions by voice. Please use the menu." | Never deletes, edits existing items, or does bulk changes by voice — too risky |
| **Must refuse** | "Move the API migration task to next Friday" | Prompt: "Voice only creates new tasks. To edit an existing one, tap it." | v1 is create-only; no editing existing tasks |

### Edge cases to handle

- **Resolving names:** "set up time with Chris" → disambiguate if there are two people named Chris; "message Sarah Chen" → map to Sarah in Engineering, not Sarah in Marketing
- **Parsing dates:** "tomorrow" → the correct date; "end of week" → this Friday; "after the holidays" → the first Monday past the company holiday calendar
- **Inferring project/tag:** mention of "pricing page" auto-tags the `Pricing` project if it exists; when unsure, leave it blank rather than guess wrong
- **Language:** English only in v1; other languages get "Voice tasks are English-only for now — type it instead?"

---

## Platform & Privacy Constraints

**Platform:**
- iOS 16+ (built on the native Speech Recognition framework)
- Android is v2 (a different speech API and a separate build)

**Performance:**
- The task preview must render in under 2 seconds (95th percentile)
- Parsing runs on-device wherever possible (for privacy)
- Complex requests fall back to the cloud, with the user's consent

**Privacy:**
- Voice data is discarded once the task is created
- Cloud processing is opt-in (and only needed for complex requests)
- Audio never leaves the device without explicit permission

---

## Open Questions

- [ ] Should the home-screen widget support voice capture too? — @iOS Team
- [ ] Does this feature need its own onboarding/tutorial? — @Design
- [ ] What's the story for users who can't use voice at all? — @Accessibility Lead
- [ ] Do we hook into Siri Shortcuts? — @iOS Team (parked for v1, flagged for v2)

---

## Appendix

### Voices from research

**Marcus (PM, Spotify):**
> "There are 47 voice memos on my phone that are just tasks. But moving them into my task manager is such a slog that I never bother — and then I forget them entirely."

**Devin (PM, Figma):**
> "Half my tasks come out of quick hallway chats. Someone says 'hey, can you check that API thing?' and I say sure — and three days later I'm going, wait, which API thing?"

**Tomás (PM, Dropbox):**
> "I want to love voice tasks, but every time I try Siri it misses the context. A task that just says 'follow up with design' and nothing else is useless to me."

### Competitive landscape

- **Todoist** — has voice input but doesn't understand context (it only transcribes)
- **Things 3** — no voice input at all
- **Linear** — voice commands are on their public roadmap for Q2
- **Asana** — voice task creation is in an invite-only beta

### Prototype

[Figma prototype: voice-task-flow-v3]

### Technical spec

[Engineering spec: voice-task-technical-design.md]
