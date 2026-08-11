# /ideate

Generate solution directions for a problem, grounded in what the brain already knows. Not a brainstorm. A synthesis.

## Input

A problem statement, an opportunity, or a `knowledge/users/insights.md § <theme>` reference. Example: `/ideate onboarding drop-off in mid-market`.

## Loads

- `brain/knowledge/strategy.md` (priorities, non-goals, north-star)
- `brain/knowledge/users/insights.md` and any matching `brain/knowledge/users/personas.md` / `brain/knowledge/users/segments.md`
- Active `brain/hypotheses/` files in the same area
- Recent `brain/decisions/` that constrain or invalidate options
- `brain/knowledge/market/competitors/` and `brain/knowledge/market/trends.md` for adjacent moves
- `rules/discovery.md` and `rules/prioritization.md` if present

## Updates

Drafts only. Nothing committed at call time.

- A draft `brain/ingestion/adhoc/<date>-ideate-<slug>.md` capturing the session
- Hypothesis candidates queued under `brain/hypotheses/<slug>.md § Candidates` (PM confirms before promotion)

## Surfaces

- 3-7 solution directions, each tagged with the evidence supporting it (insight, hypothesis, decision, or market signal)
- For each direction: which strategy priority it serves, which non-goal it might violate, which active hypothesis it would test or contradict
- 1-2 directions explicitly marked as **off-strategy** if surfaced, so the operator can decide whether to pivot strategy or reject the direction
- The thinnest viable next step for the top 2 (a discovery question, an experiment, a competitor study)

Anti-pattern: do not generate directions that ignore the strategy doc or the non-goals. If the evidence forces an off-strategy direction, surface the tension instead of swallowing it.
