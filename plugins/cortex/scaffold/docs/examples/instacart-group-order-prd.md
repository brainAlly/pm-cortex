# Group Order Feature for Instacart

**Stage:** Solution Review
**Last Updated:** January 7, 2026
**Owner:** Product Team
**Status:** Draft

---

## Hypothesis

Households rarely shop for groceries as a single person. Partners, roommates, and family members all have input on what lands in the cart, but today an Instacart order belongs to one account. People either hand over their phone, text a running list back and forth, or place a second order an hour later for the items someone forgot. That coordination overhead means smaller baskets, duplicate delivery fees, and abandoned "add this too" requests.

**If we** build a real-time collaborative group cart where several people can add to one shared order at the same time,
**then** we expect a 25-30% lift in average order value (AOV) and a 15% increase in order frequency among active households,
**because** most grocery orders are household decisions with two or more contributors, and taking the friction out of that shared decision unlocks larger, more complete baskets.

**Supporting Evidence:**
- User research: "My partner texts me a list, but by the time I've added it all she's remembered three more things and I'm editing the cart again. It's exhausting." — one of 40+ similar themes in support tickets and interviews
- Analytics: 23% of Instacart orders under $60 are followed by a second order to the same address within two hours, a strong signal of forgotten items
- Market data: DoorDash and Uber Eats reported roughly a 35% AOV lift after launching group ordering for restaurants
- Competitive gap: no major US grocery-delivery player (Amazon Fresh, Walmart, Kroger, Shipt) offers a real-time shared cart, so this is a first-mover opportunity
- Voice of Customer: a shared/household cart was the #3 most-requested capability in the Q4 2025 user survey, behind only order scheduling and better substitutions

---

## Strategic Fit

**Why this? Why now?**

This maps directly to Instacart's Q1 2026 goal of growing AOV from $115 to $140+ while keeping our fast, reliable same-day delivery promise intact. As we deepen retailer partnerships and defend share against Walmart+ and Amazon Fresh, we need differentiation that isn't just price or speed.

A shared cart builds a habit competitors can't easily copy: it makes Instacart the place a household coordinates ("just add it to our Instacart"), which raises switching costs and creates a light network effect inside each home.

**Impact Sizing:**
- Users affected: ~9 million users (roughly 65% of our ~14M monthly active users live in multi-person households)
- Revenue impact:
  - AOV increase: $115 → $144 (25% lift) = ~$29 per order
  - Applied to group orders at an 18% adoption rate: ~6.5M group orders/month × $29 ≈ $188M incremental GMV per month
  - Estimated ~$2.25B incremental annual GMV (contingent on adoption ramp)
- Strategic value: **CRITICAL** — creates in-home network effects and social lock-in

**Alternatives Considered:**
- **Scheduled "family list" feature** — Not doing, because the real unlock is real-time collaboration; an async shared list doesn't remove the back-and-forth pain
- **Bill splitting only** — Not doing, because splitting payment alone doesn't solve cart coordination; people want to build the basket together, not just divide it
- **Text/SMS list import** — Not doing in v1; parsing free-form messages is unreliable, and a native in-app experience is faster and cleaner

---

## Non-Goals

What we are explicitly NOT doing in v1:
- **Business/office ordering** — Households first; B2B pantry ordering is a v2 use case with its own admin and budgeting needs
- **Multi-address group orders** — Every participant delivers to the same address in v1; splitting one order across addresses roughly triples fulfillment complexity
- **Voice-driven cart collaboration** — Tap and type only; voice adds AI and multilingual complexity we don't need for v1
- **Group-aware recommendations** — v1 ships feature parity; personalization based on who's in the cart comes later
- **In-order group chat** — We're not building a messenger; households can discuss in whatever app they already use

**Trade-offs Made:**
- **Simplicity over flexibility** — One host owns checkout rather than a voting model; this avoids decision paralysis at the finish line
- **Speed over feature breadth** — Real-time sync is harder to build than async, but it's the core value, so it ships first
- **Mobile-first only** — Web can follow; the overwhelming majority of shared-household ordering happens on phones

---

## Success Metrics

**Primary Metric:** Average Order Value (AOV) for orders with 2+ participants
- Current baseline: $115 (overall platform AOV)
- Target: $144+ (25% lift)
- Timeline: Measure 60 days post-launch

**Secondary Metrics:**
- Group order adoption rate: 18% of all orders use group ordering within 90 days
- Repeat group order usage: 55% of users who try it use it again within 30 days
- Items per order: Rise from an average of ~24 items to 30+ items for group orders
- Order completion rate: No degradation (<2% drop) despite the added coordination step

**Guardrail Metrics:** (Must not harm)
- On-time delivery rate: Must hold at or above baseline (a bigger, jointly built basket can't erode reliability)
- Cart abandonment: <5% increase (real-time sync has to feel smooth, never glitchy)
- App crashes: 0 increase in crash rate tied to the real-time features
- Customer support tickets: <3% increase in order-related contacts

**Kill Criteria:**
If group orders see <10% adoption after 60 days, OR drive a >8% increase in cart abandonment, OR measurably degrade on-time delivery, we will pause the rollout, diagnose the friction, and either iterate or shelve the feature.

---

## Rollout Plan

**Approach:** Phased Rollout with A/B Test

**Phase 1: Internal Beta (Week 1-2)**
- Instacart employees + 500 power users in the San Francisco Bay Area
- Passing criteria:
  - Zero critical bugs affecting checkout
  - <500ms latency for real-time cart sync
  - >70% positive feedback on usability
  - At least 40% of beta users try the feature

**Phase 2: A/B Test in the Bay Area (Week 3-5)**
- 20% of Bay Area users get the group ordering feature
- Passing criteria:
  - AOV lift >15% for group orders
  - Adoption rate >12%
  - No drop in on-time delivery
  - No increase in payment failures
  - Positive NPS delta (+5 points)

**Phase 3: Expand to Top 6 Metros (Week 6-8)**
- New York, Los Angeles, Chicago, Dallas, Houston, and Atlanta
- 50% rollout in each metro
- Watch retailer and shopper metrics closely (can shoppers handle larger baskets on time?)

**Phase 4: North America Launch (Week 9+)**
- 100% rollout across all served markets in the US and Canada
- In-app announcement, social campaign, and creator partnerships
- Track GMV, AOV, and retention closely

**Rollback Plan:**
If critical bugs surface or delivery metrics slip:
- Disable the feature flag within 30 minutes (no app update required)
- Preserve user data (group order history) so we can re-enable cleanly
- Communicate to users: "Group ordering is temporarily unavailable while we make improvements"

---

## Behavior Examples

| Scenario | User Action | Expected Behavior | Notes |
|----------|-------------|-------------------|-------|
| **Create group order** | User taps "Start Group Order" on the cart screen | App generates a unique shareable link + QR code valid for 60 minutes | Link format: `instacart.com/group/ABC123` |
| **Join group order** | Household member scans the QR code or taps the link | Opens the Instacart app to the shared cart with live updates | If the app isn't installed, redirect to the app store first |
| **Add items simultaneously** | Host adds milk while a partner adds bread | Both items appear within a second, with no conflict | WebSocket-based real-time sync |
| **Remove an item someone else added** | Host removes bread a partner added | Bread disappears for everyone immediately | No permissions in v1; anyone can edit anything |
| **Host leaves before checkout** | Host closes the app or drops connection | The group order stays active; others keep adding items | Host can rejoin via the same link |
| **Checkout control** | A participant tries to check out | They see "Waiting for [Host Name] to check out" | Only the host initiates payment, to avoid double-charges and confusion |
| **Payment split** | After the host pays, participants see the confirmation | Optional prompt: "Split this $150 order 3 ways? Request $50 each" | Integrates with Venmo/PayPal for split requests |
| **Timeout scenario** | No activity for 60 minutes | The link expires and the cart is saved to the host's account only | Push notification: "Your group order expired — items are saved to your cart" |
| **Different item variants** | A participant adds "Whole Milk 1 gal" when the host has "Whole Milk ½ gal" | Both variants appear separately (not merged) | Clearly labeled "Added by [Name]" |
| **Out of stock during collaboration** | An item sells out while three people are shopping | Real-time alert to everyone: "[Item] is now unavailable" + removed from cart | Prevents checkout failures |

**Reference Examples:**
- [Uber Eats group ordering](https://www.uber.com/us/en/deliver/group-orders/) — strong flow for inviting participants
- [DoorDash group orders](https://help.doordash.com/consumers/s/article/How-do-I-place-a-group-order) — clean host/guest model
- Google Docs real-time collaboration — the gold standard for multi-user sync UX

---

## Open Questions

- [ ] Should participants be able to "lock" items they added so others can't remove them? — @Design Team
- [ ] What's the cap on simultaneous participants? (Proposed: 8 people) — @Engineering
- [ ] Do we show each person's running subtotal, or only the combined total? — @UX Research
- [ ] Should the host be able to remove participants from the group order? — @Product
- [ ] Do we notify the host when someone adds a high-cost item ($30+)? — @Design Team
- [ ] How do promo codes behave when payment is split? (Host's promo applies to the full order) — @Business
- [ ] Should there be a "suggested items" section based on participants' past orders? — @Data Science
- [ ] Do we tease the feature to build anticipation, or launch by surprise? — @Marketing

---

## Technical Approach

**High-Level Architecture:**

1. **Real-Time Sync:** WebSocket connection (Socket.io) for sub-second cart updates
2. **Link Generation:** Short-lived JWT tokens embedded in shareable links (60-min expiry)
3. **Conflict Resolution:** Last-write-wins with optimistic UI updates + server reconciliation
4. **State Management:** Redis for active group cart state (TTL: 60 min), PostgreSQL for order history
5. **Mobile:** React Native shared state using Redux + WebSocket hooks
6. **Scalability:** Horizontal scaling of WebSocket servers behind a load balancer

**Key Technical Decisions:**
- WebSocket vs. Polling: WebSocket for true real-time (polling would add a 2-5 second lag and feel broken)
- Session Management: Sticky sessions on the WebSocket tier to preserve connection state
- Offline Handling: Queue local changes and sync on reconnect
- Data Model: a `group_orders` table with a `participants` JSONB array

**API Endpoints (New):**
- `POST /api/v2/group-orders/create` — Create a group order session
- `GET /api/v2/group-orders/:id/join` — Join an existing group order
- `WS /api/v2/group-orders/:id/sync` — WebSocket for real-time cart sync
- `POST /api/v2/group-orders/:id/checkout` — Host initiates checkout

**Third-Party Integrations:**
- Venmo / PayPal APIs for split-payment requests
- Firebase Cloud Messaging for push notifications when items are added or removed

**Engineering Effort Estimate:** 6-8 weeks (3 engineers)
- Week 1-2: Backend infrastructure (WebSocket, Redis, APIs)
- Week 3-4: Mobile UI/UX + real-time sync logic
- Week 5-6: Payment splitting, edge cases, error handling
- Week 7-8: Testing (load and edge cases), beta launch prep

---

## Design Considerations

**Entry Points:**
1. **Cart Screen:** A prominent "Start Group Order" button above the cart items (primary CTA)
2. **Home Screen:** A "Shop Together" promotional banner (first two weeks post-launch)
3. **Order History:** A "Reorder as Group" option on past orders

**Visual Design:**
- Each cart item tagged with the participant's avatar (small circular photo)
- A live participant strip at the top of the cart: "Shopping with: [Avatar] [Avatar] [Avatar]"
- A subtle animation when others add items (fade-in + highlight)
- Color coding: Host = blue border, guests = gray border (a light differentiation)

**Copywriting:**
- Primary CTA: "Start Group Order" (not "Share Cart" — more action-oriented)
- Invite message: "Join my Instacart order and add what you need: [link]"
- Empty state: "Waiting for others to add items…" (friendly, not dead air)

**Accessibility:**
- Screen reader support for real-time updates: "Rohan added butter"
- High-contrast mode for participant avatars
- Haptic feedback when others add items

---

## Go-to-Market Plan

**Pre-Launch (2 weeks before):**
- Teaser campaign on Instagram/TikTok: "Grocery shopping just got social 🛒"
- Creator partnerships: family and lifestyle creators demo the feature
- PR outreach: TechCrunch, The Verge, Business Insider (grocery-tech innovation angle)

**Launch Day:**
- In-app modal for existing users: "Introducing Group Orders"
- Push notification: "Shop together with your household. Try Group Orders!"
- Social media: a launch video of families and roommates building a cart together
- Blog post: "How Instacart's Group Ordering Makes Household Shopping Easier"

**Post-Launch (Week 1-4):**
- Onboarding tooltip: first-time cart users see a "Shop with your household" prompt
- Email campaign to power users highlighting the feature
- Success stories: share testimonials ("this saved us two extra orders a week!")
- Referral incentive: "Start a group order and get $5 off when 3+ people join"

**Customer Education:**
- A 15-second in-app tutorial video
- Help center article: "How to use Group Orders"
- Support macros and chatbot flows trained on group-ordering FAQs

---

## Risk Assessment & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Real-time sync bugs/lag** | Medium | High | Extensive load testing; graceful degradation to polling if WebSocket fails |
| **Users confused by collaborative editing** | Medium | Medium | Clear onboarding tutorial; participant avatars on every item |
| **Payment-splitting disputes** | Low | Medium | Keep split payment optional, never mandatory; host controls checkout |
| **Shoppers struggle with larger baskets** | Medium | High | Monitor basket sizes and shop times; flag when group orders stretch fulfillment |
| **Abuse (strangers joining public links)** | Low | Low | Links expire in 60 min; host can end the session anytime; analytics to detect abuse |
| **Bigger baskets slow fulfillment and hurt on-time rate** | Medium | High | Set a 60-min timeout; prompt the host to check out after 20 min of inactivity |
| **App crashes from WebSocket memory leaks** | Low | High | Thorough memory profiling, crash monitoring, and a ready rollback plan |

---

## Dependencies

**Internal:**
- Engineering: 3 full-stack engineers + 1 mobile engineer (6-8 weeks)
- Design: 1 product designer (2 weeks for UI/UX)
- QA: 1 QA engineer (2 weeks for testing)
- Data Science: analytics instrumentation (3 days)
- Operations: shopper-experience team alignment on larger baskets (ongoing)

**External:**
- Venmo / PayPal: API access for split-payment requests (~2-week approval)
- Firebase: Cloud Messaging for notifications (already integrated)
- AWS: additional WebSocket server capacity (provision in Week 1)

**Blockers:**
- None currently; all dependencies are manageable within the timeline

---

## Success Criteria for Launch

**Week 4 Post-Launch (Go/No-Go for Phase 3):**
- ✅ Adoption: >12% of orders use group ordering
- ✅ AOV Lift: >15% for group orders vs. solo orders
- ✅ Retention: >50% of users who try it use it again within 30 days
- ✅ On-time delivery: holds at or above baseline
- ✅ NPS Impact: +5 points among group-order users
- ✅ Tech Stability: <0.1% crash rate, <500ms sync latency

If 5/6 criteria are met → proceed to Phase 3
If <4/6 are met → pause, iterate, retest

---

## Appendix

### User Research Quotes

"My husband and I both open Instacart at the same time, then argue about who already placed the order. It's ridiculous." — Priya, 32, Chicago

"I just want to send a cart link to my roommate so he adds his own stuff. Right now I screenshot items and he texts me more screenshots back. So inefficient." — Arjun, 25, Austin

"When my mom stays with us she wants different things than I usually buy. I hand her my phone and she scrolls forever. A shared cart would be perfect." — Neha, 28, New York

### Competitive Analysis

| Feature | Instacart | Amazon Fresh | Walmart+ | Shipt | DoorDash (US) |
|---------|-----------|--------------|----------|-------|---------------|
| Group Ordering | ✅ (This PRD) | ❌ | ❌ | ❌ | ✅ (restaurants) |
| Real-time Sync | ✅ | - | - | - | ❌ (async) |
| Payment Splitting | ✅ | - | - | - | ❌ |
| Mobile-first | ✅ | ✅ | ✅ | ✅ | ✅ |

**First-mover advantage:** No US grocery-delivery player offers real-time collaborative ordering. Shipping fast buys us a 6-12 month lead.

### Analytics Events to Track

**User Actions:**
- `group_order_created` (host initiates)
- `group_order_joined` (guest joins via link)
- `group_order_item_added` (who added, what item)
- `group_order_item_removed` (who removed, what item)
- `group_order_checkout_initiated` (host proceeds to payment)
- `group_order_payment_split_requested` (optional split)
- `group_order_completed` (successful order)
- `group_order_abandoned` (session expired or manually ended)

**Metrics to Monitor:**
- Time from group order creation to checkout (target: <20 minutes avg)
- Participants per group order (avg, max)
- Items added per participant (engagement)
- WebSocket latency (p50, p95, p99)
- Crash rate during group ordering sessions

### Rollback Procedure

**If a critical bug is detected:**
1. **Immediate:** Disable the `group_ordering_enabled` feature flag via LaunchDarkly (effective in <2 min)
2. **Within 1 hour:** Investigate the root cause and deploy a hotfix to staging
3. **Within 4 hours:** Test the hotfix and re-enable for 10% of users
4. **Within 24 hours:** Full re-enable if the hotfix holds, or communicate a delay to users

**Data preservation:**
- All group order sessions are saved to the database (not lost on rollback)
- Users can resume as individual carts if the group feature is disabled

---

**Timeline Summary:**
- Weeks 1-2: Internal beta (500 users)
- Weeks 3-5: Bay Area A/B test (20% of users)
- Weeks 6-8: Top 6 metros (50% rollout)
- Week 9+: North America launch (100%)

**Total time to full launch:** 9-10 weeks from dev start

---

## Approval & Sign-offs

**Stakeholders:**
- [ ] Product Lead — Strategic alignment
- [ ] Engineering Lead — Technical feasibility
- [ ] Design Lead — UX approval
- [ ] Operations Lead — Shopper/fulfillment readiness
- [ ] Data Science Lead — Metrics framework
- [ ] Marketing Lead — GTM plan

**Next Steps:**
1. Engineering to validate the WebSocket infrastructure approach (by Week 1)
2. Design to create high-fidelity mockups (by Week 2)
3. Operations to analyze shopper capacity for larger baskets (by Week 2)
4. Legal to review split-payment compliance (by Week 3)
5. Schedule the kickoff meeting with all stakeholders (next week)

---

*PRD Version 1.0 - Created using PM Operating System framework*
