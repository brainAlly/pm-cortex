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

Input: the PostToolUse JSON payload on stdin (written path at
`tool_input.file_path`). A path argument is also accepted, so the script stays
runnable by hand for tests and manual sweeps.
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
            content = f.read().lower()
    except Exception as e:
        return [f"Could not read file for validation: {e}"]

    errors = []
    for field in rules["required_fields"]:
        if field.lower() not in content:
            errors.append(f"Missing required field: '{field}'")

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


def main():
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
    print("Missing required fields:", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    print("\nFix the missing fields and rewrite the file to match the schema.\n", file=sys.stderr)

    sys.exit(2)


if __name__ == "__main__":
    main()
