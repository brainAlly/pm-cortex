# Testing Documentation

This directory contains testing materials and validation approaches for PM Cortex.

## Contents

### [setup-testing.md](setup-testing.md)
Evaluation report for the PM Cortex brain architecture, covering:
- Knowledge retrieval accuracy
- Ingestion and memory propagation
- Cross-document reasoning
- Hallucination resistance
- New-session memory persistence

### [interview-qa-example.md](interview-qa-example.md)
Mock answers to the PM Cortex 6-batch onboarding interview. Use as:
- Reference for the kind of answers that work well
- Template for your own onboarding
- Validation that the interview flow and scaffold work correctly

## Testing the Installation

### Quick Validation

After installing PM Cortex and initializing a brain, verify the structure:

```bash
ls brain/
# → decisions  hypotheses  ingestion  knowledge  source  stakeholders  style

ls .claude/commands/ | wc -l
# → 45 (plus INDEX.md = 46 entries)

ls .claude/sub-agents/
# → customer-voice.md  designer-reviewer.md  engineer-reviewer.md
#   executive-reviewer.md  legal-advisor.md  skeptic.md  uxr-analyst.md
```

Then test the core commands:

```bash
/ingest [paste a short meeting note]
/prep [stakeholder-name from your init answers]
/review
```

### Manual Testing

To test PM Cortex thoroughly:

1. **Install PM Cortex**
   ```
   claude plugin marketplace add brainAlly/pm-cortex
   claude plugin install pm-brain@pm-cortex
   ```

2. **Initialize a test brain**
   ```bash
   mkdir test-brain && cd test-brain
   claude
   /pm-brain
   ```

3. **Use mock answers** from [interview-qa-example.md](interview-qa-example.md) for the 6-batch interview

4. **Validate core commands**
   - `/ingest` with sample artifacts
   - `/prep` for a stakeholder from the init answers
   - `/review` for maintenance
   - `/prd-draft`, `/discover`, `/decide` for workflow commands

5. **Verify brain structure**
   ```bash
   ls brain/
   ls brain/knowledge/
   ls brain/hypotheses/
   ls brain/decisions/
   ls brain/stakeholders/
   ls brain/style/
   ```

6. **Verify command and skill presence**
   ```bash
   ls .claude/commands/ | wc -l    # expect 46 (45 commands + INDEX.md)
   ls .claude/skills/ | wc -l      # expect 54 dirs
   ls .claude/sub-agents/          # expect 7 files
   ```

## Related Documentation

- [Quickstart Guide](../quickstart.md) — Get started quickly
- [Architecture Overview](../architecture.md) — System design
- [Integration Guide](../integration-guide.md) — Advanced workflow patterns
