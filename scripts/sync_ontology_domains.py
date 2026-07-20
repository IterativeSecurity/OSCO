from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


ACTIONS_KEY = "_actions"


def insert_path(tree: dict[str, Any], parts: list[str]) -> None:
    node = tree
    for segment in parts[:-1]:
        node = node.setdefault(segment, {})
        if not isinstance(node, dict):
            raise ValueError(f"Invalid taxonomy tree state at segment '{segment}'")

    actions = node.setdefault(ACTIONS_KEY, set())
    if not isinstance(actions, set):
        raise ValueError(f"Invalid actions container for path: {'.'.join(parts)}")
    actions.add(parts[-1])


def to_yaml_node(node: dict[str, Any]) -> Any:
    keys = [k for k in node.keys() if k != ACTIONS_KEY]
    keys.sort()
    children = {k: to_yaml_node(node[k]) for k in keys}

    actions = sorted(node.get(ACTIONS_KEY, set()))

    if children and actions:
        children[ACTIONS_KEY] = actions
        return children
    if children:
        return children
    return actions


def build_taxonomy_from_catalogs(catalog_paths: list[Path]) -> dict[str, Any]:
    root: dict[str, Any] = {}

    for catalog_path in catalog_paths:
        payload = json.loads(catalog_path.read_text())
        if not isinstance(payload, list):
            raise ValueError(f"Catalog must be a JSON list: {catalog_path}")

        for item in payload:
            if not isinstance(item, dict) or "capability_id" not in item:
                raise ValueError(f"Invalid catalog entry in {catalog_path}")
            capability_id = item["capability_id"]
            if not isinstance(capability_id, str):
                raise ValueError(f"Non-string capability_id in {catalog_path}")
            parts = capability_id.split(".")
            if len(parts) < 3:
                raise ValueError(
                    f"capability_id must have at least 3 segments: {capability_id}"
                )
            insert_path(root, parts)

    return root


def canonical_yaml_text(payload: dict[str, Any]) -> str:
    return yaml.safe_dump(payload, sort_keys=False)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build ontology/domains.yaml from capability catalogs"
    )
    parser.add_argument(
        "--catalog",
        action="append",
        default=[],
        help="Catalog JSON path (repeatable). Defaults to curated + extended catalogs.",
    )
    parser.add_argument(
        "--output",
        default="ontology/domains.yaml",
        help="Output YAML path (default: ontology/domains.yaml)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check mode: fail if output is stale, do not write",
    )
    args = parser.parse_args()

    catalog_paths = [Path(p) for p in args.catalog] if args.catalog else [
        Path("capability/catalog.json"),
        Path("capability/catalog.extended.json"),
    ]
    output_path = Path(args.output)

    taxonomy_tree = build_taxonomy_from_catalogs(catalog_paths)
    yaml_payload = {
        "version": "0.1.0",
        "domains": to_yaml_node(taxonomy_tree),
    }
    new_text = canonical_yaml_text(yaml_payload)

    if args.check:
        if not output_path.exists() or output_path.read_text() != new_text:
            raise SystemExit(
                f"{output_path} is stale. Run: uv run scripts/sync_ontology_domains.py"
            )
        print(f"{output_path} is up to date")
        return

    output_path.write_text(new_text)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
