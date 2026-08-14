---
description: Design and analyze growth loops — acquisition, engagement, and monetization — for compounding traction
argument-hint: "[product or growth challenge]"
---

# /growth-loops

Usage: `/growth-loops`

Designs or analyzes your product's growth loops across three dimensions: acquisition, engagement, and monetization. Systems-level thinking for compounding growth.

## Execution

### Step 1 — Load context

- `brain/knowledge/strategy.md` — North Star, OKRs, and current growth priorities
- `brain/knowledge/market/landscape.md` — GTM motion and channel strategy
- `brain/knowledge/users/insights.md` — what drives user behavior and sharing
- `brain/knowledge/product/metrics.md` — current growth metrics
- `brain/knowledge/product/features/` — features with viral or network potential
- `brain/style/frameworks.md` + `brain/style/patterns.md`

### Step 2 — Define what a loop is

A growth loop is a closed system where the output of one action becomes the input for the next cycle. Unlike funnels, loops compound: each cycle through the loop adds more users, engagement, or revenue than the last.

Ask the PM: "Are we designing loops from scratch, analyzing existing loops for leaks, or both?"

### Step 3 — Map the acquisition loop

The acquisition loop answers: how does one new user bring in the next new user?

**Acquisition loop analysis:**

Current path: [Describe step by step how a new user enters today — e.g., "User signs up via Google search → activates → invites 2 colleagues → 1 of those becomes a new user"]

**Loop components:**
- **Seed:** [What triggers a new user to discover the product? — e.g., referral link, SEO, word of mouth, embed, export]
- **Action:** [What behavior within the product creates the output that acquires the next user?]
- **Output:** [What does that action produce that a non-user encounters? — e.g., shared report, embed, mention, public profile]
- **Conversion:** [Of those who encounter the output, what % become new users?]
- **Cycle time:** [How long does one full loop take?]

**Loop strength:**
- Viral coefficient (K): [average new users generated per existing user per cycle]
  - K > 1: exponential growth
  - 0.5 < K < 1: supplementary channel, won't drive standalone growth
  - K < 0.5: the loop exists but is weak
- Current K estimate: [value or "unknown — needs measurement"]

**Biggest leak in the acquisition loop:**
[The step with the lowest conversion rate or longest cycle time — this is where to invest first]

**Interventions to strengthen the loop:**
| Lever | Effect | Effort | Priority |
|-------|--------|--------|---------|
| [specific product or marketing change] | [expected improvement to K or cycle time] | S/M/L | P0/P1/P2 |

### Step 4 — Map the engagement loop

The engagement loop answers: what brings users back, and what deepens their usage over time?

**Engagement loop analysis:**

**Trigger:** [What brings the user back? — external trigger: email, notification, push; internal trigger: habit, anxiety, aspiration]
**Action:** [Core behavior in the product — the job they're getting done]
**Reward:** [What does the user get — variable or fixed? Information, social validation, progress, accomplishment]
**Investment:** [What does the user put in that makes them more likely to return — data, connections, customization, history]

This is the Hook Model. Each element matters:
- If the trigger is absent: users don't return unless they decide to
- If the reward is fixed: novelty wears off
- If there's no investment: there's no switching cost

**Current engagement loop strength:**
- D7 retention: [from `knowledge/product/metrics.md`]
- D30 retention: [value]
- Average sessions per user per week: [value]
- Core behavior frequency among retained users: [value]

**Biggest weakness in the engagement loop:**
[Weak trigger / weak reward / no investment mechanic / unclear core action]

**Interventions to strengthen the loop:**
| Lever | Targets | Expected impact | Priority |
|-------|---------|----------------|---------|
| [specific change] | [trigger / action / reward / investment] | [metric and expected improvement] | P0/P1/P2 |

### Step 5 — Map the monetization loop

The monetization loop answers: how does growth in users and engagement convert to revenue that funds more growth?

**Monetization loop analysis:**

**Value accumulation:** [How does user value grow over time? — more data, more integrations, more colleagues, more output]
**Conversion event:** [What triggers the purchase decision? — usage limit, team size, feature gate, time-based trial end]
**Revenue:** [What does the customer pay? — per seat, usage-based, subscription tier]
**Reinvestment:** [How does revenue fund the next cycle of acquisition or product improvement?]

**Monetization metrics:**
- Free → paid conversion rate: [%]
- Average ACV or MRR per paying customer: [value]
- Time from activation to first payment: [days]
- Expansion revenue rate: [%]

**Biggest leak in the monetization loop:**
[Low free-to-paid conversion / long time to payment / high churn after first payment]

**Interventions to strengthen the loop:**
| Lever | Expected impact | Priority |
|-------|----------------|---------|
| [specific change] | [metric and improvement] | P0/P1/P2 |

### Step 6 — Cross-loop opportunities

Identify where loops reinforce each other:
- Engagement → Acquisition: [Does higher engagement increase virality? e.g., "Users who complete X share 3x more"]
- Acquisition → Monetization: [Does the acquisition channel predict payment rate? e.g., "Organic users convert at 2× paid"]
- Monetization → Engagement: [Does paying correlate with higher retention? e.g., "Paid users are 5× more likely to be retained at 90 days"]

Name any loops that are working against each other (anti-reinforcing).

### Step 7 — Prioritized growth loop roadmap

Based on the analysis:

**Highest-leverage investments (next quarter):**
1. [Loop] → [Specific intervention] → [Expected metric improvement] → Effort: [S/M/L]
2.
3.

**Experiments to run:**
- [hypothesis about loop improvement] → [specific test design] → [metric that confirms or refutes]

For each experiment: suggest `/experiment-decision` to determine whether to A/B test or ship directly.

### Step 8 — Update strategy.md (one-line confirmation)

Ask: "Update `brain/knowledge/strategy.md` growth section with this loop analysis? (y/n)"

On yes: update `knowledge/strategy.md` with:
- Acquisition loop diagram and current K
- Engagement loop summary and retention baseline
- Monetization loop conversion rates
- Top 3 prioritized interventions

Report: "`brain/knowledge/strategy.md` growth section updated."
