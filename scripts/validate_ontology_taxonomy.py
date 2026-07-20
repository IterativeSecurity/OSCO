from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


def iter_allowed_paths(node: object, prefix: list[str]) -> set[tuple[str, ...]]:
    allowed: set[tuple[str, ...]] = set()

    if isinstance(node, dict):
        for key, value in node.items():
            if key == "_actions":
                if not isinstance(value, list):
                    raise ValueError("'_actions' entries must be a list of strings")
                for action in value:
                    if not isinstance(action, str):
                        raise ValueError("'_actions' list entries must be strings")
                    allowed.add(tuple(prefix + action.split(".")))
            else:
                allowed |= iter_allowed_paths(value, prefix + [key])
    elif isinstance(node, list):
        for item in node:
            if isinstance(item, str):
                allowed.add(tuple(prefix + item.split(".")))
            else:
                allowed |= iter_allowed_paths(item, prefix)
    elif isinstance(node, str):
        allowed.add(tuple(prefix + node.split(".")))
    else:
        raise ValueError(f"Unsupported taxonomy node type: {type(node)!r}")

    return allowed


def load_allowed_capabilities(taxonomy_path: Path) -> set[tuple[str, ...]]:
    data = yaml.safe_load(taxonomy_path.read_text())
    if not isinstance(data, dict) or "domains" not in data:
        raise ValueError("taxonomy file must be a mapping with a top-level 'domains' key")

    domains = data["domains"]
    if not isinstance(domains, dict):
        raise ValueError("'domains' must be a mapping")

    return iter_allowed_paths(domains, [])


def load_capability_ids(catalog_path: Path) -> list[str]:
    payload = json.loads(catalog_path.read_text())
    if not isinstance(payload, list):
        raise ValueError(f"catalog file must contain a list of capabilities: {catalog_path}")

    capability_ids: list[str] = []
    for idx, item in enumerate(payload):
        if not isinstance(item, dict) or "capability_id" not in item:
            raise ValueError(
                f"catalog entry {idx} in {catalog_path} is missing capability_id"
            )
        capability_id = item["capability_id"]
        if not isinstance(capability_id, str):
            raise ValueError(
                f"catalog entry {idx} in {catalog_path} has non-string capability_id"
            )
        capability_ids.append(capability_id)

    return capability_ids


def validate_catalog(catalog_path: Path, allowed_paths: set[tuple[str, ...]]) -> list[str]:
    missing: list[str] = []
    for capability_id in load_capability_ids(catalog_path):
        if tuple(capability_id.split(".")) not in allowed_paths:
            missing.append(capability_id)
    return missing


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate capability_id taxonomy against ontology/domains.yaml"
    )
    parser.add_argument(
        "--taxonomy",
        default="ontology/domains.yaml",
        help="Path to taxonomy YAML file (default: ontology/domains.yaml)",
    )
    parser.add_argument(
        "--catalog",
        action="append",
        default=[],
        help="Catalog JSON path (repeatable). Defaults to curated + extended catalogs.",
    )
    args = parser.parse_args()

    taxonomy_path = Path(args.taxonomy)
    catalog_paths = [Path(p) for p in args.catalog] if args.catalog else [
        Path("capability/catalog.json"),
        Path("capability/catalog.extended.json"),
    ]

    allowed_paths = load_allowed_capabilities(taxonomy_path)

    total_missing = 0
    for catalog_path in catalog_paths:
        missing = validate_catalog(catalog_path, allowed_paths)
        if missing:
            total_missing += len(missing)
            print(f"[FAIL] {catalog_path}: {len(missing)} capability_ids not in taxonomy")
            preview = "\n".join(f"  - {capability_id}" for capability_id in missing[:30])
            print(preview)
            if len(missing) > 30:
                print(f"  ... and {len(missing) - 30} more")
        else:
            print(f"[OK] {catalog_path}: all capability_ids covered by taxonomy")

    if total_missing:
        raise SystemExit(1)

    print(
        f"Taxonomy validation passed. Allowed capability paths: {len(allowed_paths)}"
    )


if __name__ == "__main__":
    main()
