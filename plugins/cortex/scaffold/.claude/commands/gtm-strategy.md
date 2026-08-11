---
name: gtm-strategy
description: Full GTM — ICP, positioning, channel selection, motion design (PLG/SLG/MLG), and success metrics. Updates brain/knowledge/market/landscape.md and strategy.md.
---

# /gtm-strategy

Usage: `/gtm-strategy [product, feature, or segment — or omit for full product GTM]`

Produces a complete go-to-market strategy with ICP, positioning, channel selection, and motion design. Updates the brain with the resulting strategy.

## Execution

### Step 1 — Load context

- `brain/knowledge/strategy.md` — North Star, OKRs, and current positioning
- `brain/knowledge/market/landscape.md` — market context and existing GTM signals
- `brain/knowledge/market/competitors/` — how competitors go to market
- `brain/knowledge/users/personas.md` — target personas
- `brain/knowledge/users/insights.md` — user needs and buying signals
- `brain/knowledge/product/metrics.md` — current acquisition and activation metrics
- `brain/style/frameworks.md` + `brain/style/patterns.md`

### Step 2 — Clarify GTM scope

Confirm:
- Is this a new product, a new feature, or expansion into a new segment?
- What's the launch window?
- What resources are available (dedicated headcount, budget, partnerships)?

### Step 3 — Define the ICP (Ideal Customer Profile)

**Firmographic criteria:**
- Company size: [employees / revenue range]
- Industry: [verticals where the problem is most acute]
- Geography: [regions to target in this phase]
- Stage: [startup / growth / enterprise]
- Technology: [tech stack signals if applicable — e.g., "uses Salesforce," "on AWS"]

**Behavioral criteria (the jobs-based lens):**
- The job they're trying to get done: [JTBD statement]
- Current tools they use for this job: [tools and their pain points]
- Trigger events that cause them to look for a solution: [e.g., "team grows past 20," "raised a Series B," "lost a deal due to X"]

**Negative ICP (explicitly not targeting):**
- [segment]: excluded because [specific reason — poor fit, wrong economics, too complex]

**Validation:** Cross-check ICP against `knowledge/users/personas.md` and interview signals. Flag any ICP claim not supported by brain evidence.

### Step 4 — Positioning

**Positioning statement (internal):**
"For [ICP], who [trigger or situation], [product name] is the [category] that [primary benefit] because [reason to believe]. Unlike [primary alternative], we [key differentiator]."

**Messaging hierarchy:**
- Headline: [8 words or fewer — the first thing they read]
- Value proposition: [2–3 sentences — what it does, for whom, and why it's better]
- Proof points: [3 specific, concrete claims — with evidence or examples]
- Objection handling: [top 3 objections and responses]

**Category play:**
- Creating a new category? [yes / no — if yes, name the category]
- Repositioning within an existing category? [yes / no — against whom]
- Challenger in an established market? [yes / no — what's the wedge]

### Step 5 — Motion design

Select the primary GTM motion and design it:

**Motion assessment:**

| Motion | Fits when | Signal it's right |
|--------|----------|-----------------|
| PLG (Product-Led Growth) | Low ACV, self-serve capable, network effects, viral coefficient | Users can reach value without sales; viral or community sharing observed |
| SLG (Sales-Led Growth) | High ACV, complex buying process, enterprise compliance, multi-stakeholder | Trial → sale handoff required; legal/procurement involved |
| MLG (Marketing-Led Growth) | Strong brand differentiation, content moat, SEO/community play | Organic demand exists; category awareness is the unlock |
| Community-Led | Network value, peer influence, practitioner identity | Users identify as a community; peer referrals are organic |

**Recommended motion:** [PLG / SLG / MLG / hybrid]
**Rationale:** [specific — why this motion given ICP, ACV, and product characteristics]

**Motion design for [recommended]:**

*If PLG:*
- Free tier or trial: [what's free, what's gated]
- Aha moment definition: [specific first-value event]
- Viral or expansion hook: [how users naturally bring in colleagues or spread the product]
- Conversion trigger: [what causes free → paid]
- Self-serve upgrade path: [steps from free to paid with no sales]

*If SLG:*
- Demand generation: [how leads enter the top of funnel]
- Qualification criteria: [MEDDIC or equivalent — what makes a lead worth sales time]
- Sales cycle stages: [steps and average time in each]
- Proof of value: [pilot / POC / demo — what de-risks the purchase]
- Champion → economic buyer path: [how the champion gets internal budget approval]

*If MLG:*
- Content strategy: [formats, topics, and channels for organic reach]
- SEO / category keywords: [what the ICP searches when they have the problem]
- Community channels: [Slack communities, subreddits, industry events]
- Brand play: [what the brand stands for that creates affinity]

### Step 6 — Channel selection

For each channel: [name], [fit for ICP], [expected CAC], [scalable: yes/no], [priority: P0/P1/P2]

**Top 3 channels for phase 1:**
1. [channel] — [why it's the highest-confidence bet for this ICP]
2. [channel]
3. [channel]

**Channels to avoid this phase:** [channels that don't fit ICP or are too expensive to learn now]

### Step 7 — Success metrics

| Metric | Definition | Phase 1 target | Phase 2 target |
|--------|-----------|---------------|---------------|
| CAC | Cost to acquire a new customer | | |
| Time to first value | Time from sign-up to Aha | | |
| Activation rate | % of sign-ups who activate | | |
| Pipeline coverage | Qualified pipeline vs. target | | |
| Win rate | % of qualified leads → close | | |
| Payback period | Months to recover CAC | | |

### Step 8 — Update the brain (one-line confirmation)

Ask: "Update `brain/knowledge/market/landscape.md` and `brain/knowledge/strategy.md` with this GTM strategy? (y/n)"

On yes:
- Update `knowledge/market/landscape.md` with ICP, positioning, and channel strategy
- Update `knowledge/strategy.md` GTM section with motion design and success metrics

Save shareable version to `outputs/YYYY-MM-DD-gtm-strategy.md`.

Report: "GTM strategy saved. `knowledge/market/landscape.md` and `knowledge/strategy.md` updated."
