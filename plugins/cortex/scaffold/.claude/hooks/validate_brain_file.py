#!/usr/bin/env python3
"""
Brain file schema validator. Fires via PostToolUse hook on every Write/Edit.
Validates files in decisions/, hypotheses/, stakeholders/, knowledge/product/features/.
Free-form dirs (ingestion/, source/, style/, outputs/) are silently skipped.
"""

import sys
import os
import re


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
        "required_fields": [
            "confidence:",
            "status:",
            "decision-trigger:",
        ],
        "name": "Hypothesis",
        "schema": "brain/hypotheses/_SCHEMA.md",
    },
    "stakeholders": {
        "required_fields": [
            "role:",
            "influence:",
            "last-touched:",
        ],
        "name": "Stakeholder",
        "schema": "brain/stakeholders/_SCHEMA.md",
    },
}

FEATURE_DIR_PATTERN = re.compile(
    r"brain[/\\]knowledge[/\\]product[/\\]features[/\\](?!_SCHEMA\.md).+\.md$"
)

FEATURE_REQUIRED_FIELDS = [
    "status:",
    "hypothesis:",
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


def main():
    if len(sys.argv) < 2:
        sys.exit(0)

    path = sys.argv[1]
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

    print(f"\n[PM Cortex] Write blocked — schema validation failed for {kind} file: {path}")
    print(f"Schema reference: {schema}")
    print("Missing required fields:")
    for e in errors:
        print(f"  - {e}")
    print("\nFix the missing fields and retry the write.\n")

    sys.exit(1)


if __name__ == "__main__":
    main()
