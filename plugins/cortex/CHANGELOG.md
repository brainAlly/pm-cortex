# Changelog — PM Brain

All notable changes to the PM Brain plugin are documented here. Run `/pm-brain upgrade` after updating the plugin in Claude Desktop to apply changes to your local brain.

---

## v1.0.0 — Initial Release

### What's included

**Brain architecture**
- Three-tier memory system: source/ → ingestion/ → knowledge/ with promotion threshold at 3+ independent observations
- style/ layer: writing.md, frameworks.md, patterns.md — personalization that evolves from usage
- Schema-validated directories: decisions/, hypotheses/, stakeholders/
- Provenance tagging system with 5 trust levels
- Validation hook (validate_brain_file.py) enforcing schema compliance

**Commands (45)**
- 9 brain commands: /ingest, /prep, /review, /decide, /strategy-check, /ideate, /risk, /hypothesize, /plan
- 36 skill and workflow commands organized by frequency: daily (6), weekly (6), sprint (14), occasional (11), strategic (6)

**Standalone skills (8)**
- User-invocable and auto-selected by Claude: opportunity-solution-tree, market-sizing, porters-five-forces, pricing-strategy, lean-canvas, sentiment-analysis, user-personas, swot-analysis

**Sub-agents (7)**
- engineer-reviewer, designer-reviewer, executive-reviewer, legal-advisor, customer-voice, skeptic, uxr-analyst
- All 7 run simultaneously via /prd-review-panel

**Upgrade system**
- /pm-brain upgrade command
- UPGRADE_MANIFEST.md for deterministic file routing
- Version tracking via .pm-os-version
