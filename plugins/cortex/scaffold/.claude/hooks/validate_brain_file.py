#!/usr/bin/env python3
"""
Brain file schema validator. Fires via a PostToolUse hook on Write|Edit.

Because PostToolUse runs *after* the tool, the file is already on disk — this
hook does not prevent a bad write, it catches it. On a schema violation it
writes the problem to stderr and exits 2, the code that feeds stderr back to
Claude, so the model sees the error and rewrites the file with the correct
fields. A clean file exits 0 and is silent.

Validates decisions/, hypotheses/, stakeholders/, and knowledge/product/features/.
Free-form dirs (ingestion/, source/, style/, outputs/) are silently skipped.

Beyond the required-field substring check, decision files get two structural
checks (what .claude/commands/decide.md promises): the Reversal Condition must
name a specific, observable signal (not "if things change"), and every Evidence
row must carry a provenance tag (COUNT-THE-TAGS).

Input: the PostToolUse JSON payload on stdin (written path at
`tool_input.file_path`). A path argument is also accepted, so the script stays
runnable by hand for tests and manual sweeps.

Subcommands (do not fire from the hook — run manually or from /review):
  --all [root]       Validate every brain file in the validated dirs. Catches
                     files authored via Bash, which Write|Edit hooks never see.
  --selftest [root]  Assert every _SCHEMA.md emits the literals its own
                     validator requires — a guard against schema/validator drift.
"""

import sys
import os
import re
import json


VALIDATED_DIRS = {
    "decisions": {
        # Substrings must match the section headers/fields the schema actually
        # emits (see brain/decisions/_SCHEMA.md), lowercased. "what we are
        # deciding" and "reversal condition" are section headers, not `field:`
        # labels — matching the earlier `question:` / `reversal-condition:`
        # forms blocked every conformant decision write.
        "required_fields": [
            "status:",
            "driver:",
            "what we are deciding",
            "decision:",
            "reversal condition",
            "blocked by:",
            "blocks:",
        ],
        "name": "Decision",
        "schema": "brain/decisions/_SCHEMA.md",
    },
    "hypotheses": {
        # Substrings must match what brain/hypotheses/_SCHEMA.md actually
        # emits, lowercased. The field is `**Decision trigger:**` (a space,
        # not a hyphen) — the old `decision-trigger:` form blocked every
        # conformant hypothesis write.
        "required_fields": [
            "confidence:",
            "status:",
            "decision trigger:",
        ],
        "name": "Hypothesis",
        "schema": "brain/hypotheses/_SCHEMA.md",
    },
    "stakeholders": {
        # `**Last touched:**` (a space, not a hyphen). The old
        # `last-touched:` form blocked every conformant stakeholder write.
        "required_fields": [
            "role:",
            "influence:",
            "last touched:",
        ],
        "name": "Stakeholder",
        "schema": "brain/stakeholders/_SCHEMA.md",
    },
}

FEATURE_DIR_PATTERN = re.compile(
    r"brain[/\\]knowledge[/\\]product[/\\]features[/\\](?!_SCHEMA\.md).+\.md$"
)

# Substrings must match what brain/knowledge/product/features/_SCHEMA.md
# actually emits, lowercased. The hypothesis part is a `## Hypothesis`
# section header, not a `hypothesis:` field — the old `hypothesis:` form
# blocked every conformant feature write.
FEATURE_REQUIRED_FIELDS = [
    "status:",
    "## hypothesis",
]


# --- Decision-specific structural checks -------------------------------------
# A substring field-check can confirm the words "reversal condition" appear; it
# cannot tell "if NPS drops below 30 for two months" from "if things change".
# These two checks are what `.claude/commands/decide.md` promises and what the
# field-check alone could not deliver:
#   1. the Reversal Condition must name a specific, observable signal
#   2. every Evidence row must carry a provenance tag (COUNT-THE-TAGS)
# They run only for files in brain/decisions/.

# Reject a reversal condition that is empty, still the placeholder, or one of
# these known-vague fillers. This is a "reject known-bad" list, not a
# "prove-it-is-good" gate, so a genuinely specific condition never trips it.
VAGUE_REVERSAL_PHRASES = [
    "if things change", "things change",
    "if it's not working", "if it isn't working", "if this isn't working",
    "if it doesn't work", "if this doesn't work",
    "if the market shifts", "if market shifts", "market shifts",
    "if we get pushback", "if there's pushback", "if there is pushback",
    "if needed", "if necessary", "if appropriate", "when appropriate",
    "if circumstances change", "if something changes", "as needed",
    "revisit later", "revisit if needed", "tbd", "n/a", "none", "unknown",
]

# A provenance tag is a bracketed path ([ingestion/...] / [source/...]) or one
# of the parenthetical enum forms (see brain/decisions/_SCHEMA.md).
_TAG_PATH = re.compile(r"\[[^\]\n]*/[^\]\n]*\]")
_TAG_PAREN = re.compile(
    r"\((?:stakeholder-verbal|intuition|industry-knowledge|chat)\b[^)]*\)", re.I
)


def _section_body(raw: str, heading: str):
    """Return the text under a `## <heading>` up to the next `## ` or `---`.

    Returns None if the heading is absent (the required-field check already
    flags a missing section, so the structural check stays silent there).
    """
    lines = raw.splitlines()
    target = heading.strip().lower()
    start = None
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("#") and s.lstrip("#").strip().lower() == target:
            start = i + 1
            break
    if start is None:
        return None
    body = []
    for line in lines[start:]:
        s = line.strip()
        if s.startswith("## ") or s == "---":
            break
        body.append(line)
    return "\n".join(body)


def _has_provenance_tag(text: str) -> bool:
    return bool(_TAG_PATH.search(text) or _TAG_PAREN.search(text))


def check_reversal_condition(raw: str) -> list[str]:
    """A decision's Reversal Condition must name a specific, observable signal."""
    body = _section_body(raw, "Reversal Condition")
    if body is None:
        return []  # heading absent — required-field check handles that
    text = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
    if not text or (text.startswith("[") and text.endswith("]")):
        return ["Reversal Condition is empty or still the schema placeholder — "
                "name a specific, observable signal."]
    norm = " ".join(text.lower().split())
    if len(norm.split()) <= 12 and any(p in norm for p in VAGUE_REVERSAL_PHRASES):
        return ["Reversal Condition is too vague — name a specific, observable "
                "signal (a metric crossing a threshold, a named event, a "
                "stakeholder withdrawing support), not e.g. 'if things change'."]
    return []


def check_evidence_tags(raw: str) -> list[str]:
    """Every Evidence row in a decision must carry a provenance tag."""
    body = _section_body(raw, "Evidence")
    if body is None:
        return []
    errors = []
    for line in body.splitlines():
        s = line.strip()
        if not (s.startswith("- ") or s.startswith("* ")):
            continue
        item = s[2:].strip()
        if not item or item.startswith("<!--"):
            continue
        if not _has_provenance_tag(item):
            snippet = item if len(item) <= 60 else item[:57] + "..."
            errors.append(f"Evidence row has no provenance tag: '{snippet}'")
    return errors


def is_schema_file(path: str) -> bool:
    return os.path.basename(path) == "_SCHEMA.md"


def is_index_file(path: str) -> bool:
    return os.path.basename(path) == "INDEX.md"


def classify_path(path: str):
    """Return (dir_key, rule_dict) if path is in a validated dir, else None."""
    normalized = path.replace("\\", "/")

    # Feature files
    if FEATURE_DIR_PATTERN.search(normalized):
        return ("features", {
            "required_fields": FEATURE_REQUIRED_FIELDS,
            "name": "Feature",
            "schema": "brain/knowledge/product/features/_SCHEMA.md",
        })

    # Decisions / hypotheses / stakeholders
    for dir_key, rules in VALIDATED_DIRS.items():
        pattern = f"brain/{dir_key}/"
        if pattern in normalized:
            return (dir_key, rules)

    return None


def validate(path: str) -> list[str]:
    """Return list of validation error strings, empty if valid."""
    classification = classify_path(path)
    if classification is None:
        return []  # not a validated path — silently pass

    if is_schema_file(path) or is_index_file(path):
        return []  # schema and index files are exempt

    if not os.path.exists(path):
        return []  # file was deleted — not a write error

    dir_key, rules = classification

    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
    except Exception as e:
        return [f"Could not read file for validation: {e}"]

    content = raw.lower()

    errors = []
    for field in rules["required_fields"]:
        if field.lower() not in content:
            errors.append(f"Missing required field: '{field}'")

    # Decision files get two structural checks the substring check can't do.
    if dir_key == "decisions":
        errors.extend(check_reversal_condition(raw))
        errors.extend(check_evidence_tags(raw))

    return errors


def resolve_path() -> str:
    """Resolve the file to validate.

    An explicit path argument wins (manual runs, tests). Otherwise read the
    PostToolUse JSON payload from stdin and take `tool_input.file_path`. Any
    parse failure resolves to "" — the hook then no-ops rather than wedging
    every write in the session (fail open, never fail closed).
    """
    if len(sys.argv) >= 2 and sys.argv[1].strip():
        return sys.argv[1]

    try:
        raw = sys.stdin.read()
    except Exception:
        return ""
    if not raw.strip():
        return ""
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return ""
    return (payload.get("tool_input", {}) or {}).get("file_path", "") or ""


def iter_schema_rules(root="."):
    """Yield (schema_path, required_fields, name) for every validated type."""
    for _, rules in VALIDATED_DIRS.items():
        yield (os.path.join(root, rules["schema"]), rules["required_fields"], rules["name"])
    yield (
        os.path.join(root, "brain/knowledge/product/features/_SCHEMA.md"),
        FEATURE_REQUIRED_FIELDS,
        "Feature",
    )


def run_selftest(root=".") -> int:
    """Assert every _SCHEMA.md emits the literals its own validator requires.

    Guards against validator/schema drift — the defect class behind the
    hyphen-vs-space field bugs. _SCHEMA.md files are exempt from runtime
    validation, so nothing else checks this. Returns a process exit code.
    """
    drift = []
    for schema_path, fields, name in iter_schema_rules(root):
        if not os.path.exists(schema_path):
            drift.append(f"{name}: schema not found at {schema_path}")
            continue
        try:
            with open(schema_path, "r", encoding="utf-8") as f:
                content = f.read().lower()
        except Exception as e:
            drift.append(f"{name}: could not read {schema_path}: {e}")
            continue
        for field in fields:
            if field.lower() not in content:
                drift.append(f"{name}: {schema_path} does not emit required literal {field!r}")

    if drift:
        print("[PM Cortex] Schema/validator drift — a schema fails its own rules:", file=sys.stderr)
        for d in drift:
            print(f"  - {d}", file=sys.stderr)
        print("\nAlign the required_fields literal and the schema so they match.\n", file=sys.stderr)
        return 1
    print("[PM Cortex] selftest OK — every _SCHEMA.md satisfies its own validator.")
    return 0


def run_validate_all(root=".") -> int:
    """Validate every existing brain file in the validated dirs.

    Catches files authored outside Write/Edit (e.g. via Bash), which the
    PostToolUse hook never sees. Meant to be run as a /review step and by hand.
    Returns a process exit code (1 if any file fails).
    """
    dirs = [os.path.join(root, f"brain/{k}") for k in VALIDATED_DIRS]
    dirs.append(os.path.join(root, "brain/knowledge/product/features"))
    failures = []
    checked = 0
    for d in dirs:
        if not os.path.isdir(d):
            continue
        for dirpath, _, filenames in os.walk(d):
            for fn in filenames:
                if not fn.endswith(".md"):
                    continue
                p = os.path.join(dirpath, fn)
                if is_schema_file(p) or is_index_file(p):
                    continue
                checked += 1
                errs = validate(p)
                if errs:
                    failures.append((p, errs))

    if failures:
        print(f"[PM Cortex] Schema sweep — {len(failures)} of {checked} file(s) non-conformant:", file=sys.stderr)
        for p, errs in failures:
            print(f"  {p}", file=sys.stderr)
            for e in errs:
                print(f"    - {e}", file=sys.stderr)
        print("\nRewrite the files above to match their schema, then re-run.\n", file=sys.stderr)
        return 1
    print(f"[PM Cortex] Schema sweep OK — {checked} file(s) conform.")
    return 0


def main():
    # Subcommands (manual / /review / self-test) — intercepted before the hook path.
    if len(sys.argv) >= 2 and sys.argv[1] in ("--all", "--selftest"):
        root = sys.argv[2] if len(sys.argv) >= 3 else "."
        sys.exit(run_selftest(root) if sys.argv[1] == "--selftest" else run_validate_all(root))

    path = resolve_path()
    if not path:
        sys.exit(0)  # nothing to validate (no path, or not a hook invocation)

    errors = validate(path)
    if not errors:
        sys.exit(0)

    classification = classify_path(path)
    if classification:
        _, rules = classification
        kind = rules["name"]
        schema = rules["schema"]
    else:
        kind = "Brain file"
        schema = "brain/"

    # The write already landed (PostToolUse). Report to stderr and exit 2 so
    # Claude receives this and rewrites the file — do not claim it was blocked.
    print(f"\n[PM Cortex] Schema violation written to disk — {kind} file: {path}", file=sys.stderr)
    print(f"Schema reference: {schema}", file=sys.stderr)
    print("Problems found:", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    print("\nFix the problems above and rewrite the file to match the schema.\n", file=sys.stderr)

    sys.exit(2)


if __name__ == "__main__":
    main()
