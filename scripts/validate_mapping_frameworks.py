from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from osco.models.core import MappingFramework


def load_frameworks_yaml(path: Path) -> set[str]:
    payload = yaml.safe_load(path.read_text())
    if not isinstance(payload, dict) or "frameworks" not in payload:
        raise ValueError("frameworks yaml must contain top-level 'frameworks' list")

    frameworks = payload["frameworks"]
    if not isinstance(frameworks, list) or not all(isinstance(item, str) for item in frameworks):
        raise ValueError("'frameworks' must be a list of strings")

    return set(frameworks)


def load_frameworks_enum() -> set[str]:
    return {item.value for item in MappingFramework}


def extract_mapping_frameworks(path: Path) -> list[str]:
    payload = json.loads(path.read_text())
    if not isinstance(payload, list):
        raise ValueError(f"catalog must be a JSON list: {path}")

    found: list[str] = []
    for idx, item in enumerate(payload):
        if not isinstance(item, dict):
            raise ValueError(f"catalog entry {idx} in {path} is not an object")
        mappings = item.get("mappings", [])
        if not isinstance(mappings, list):
            raise ValueError(f"'mappings' must be a list in {path} entry {idx}")
        for m_idx, mapping in enumerate(mappings):
            if not isinstance(mapping, dict):
                raise ValueError(
                    f"mapping item {m_idx} in {path} entry {idx} is not an object"
                )
            framework = mapping.get("framework")
            if framework is None:
                raise ValueError(
                    f"mapping item {m_idx} in {path} entry {idx} missing 'framework'"
                )
            if not isinstance(framework, str):
                raise ValueError(
                    f"mapping item {m_idx} in {path} entry {idx} has non-string framework"
                )
            found.append(framework)
    return found


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate mapping framework consistency across enum, YAML, and catalogs"
    )
    parser.add_argument(
        "--frameworks-yaml",
        default="mappings/frameworks.yaml",
        help="Path to framework registry YAML",
    )
    parser.add_argument(
        "--catalog",
        action="append",
        default=[],
        help="Catalog JSON file to validate (repeatable).",
    )
    args = parser.parse_args()

    frameworks_yaml = Path(args.frameworks_yaml)
    catalogs = [Path(p) for p in args.catalog] if args.catalog else [
        Path("capability/catalog.json"),
        Path("capability/catalog.extended.json"),
        Path("detection/detections.json"),
        Path("validation/validations.json"),
    ]

    yaml_frameworks = load_frameworks_yaml(frameworks_yaml)
    enum_frameworks = load_frameworks_enum()

    missing_in_yaml = sorted(enum_frameworks - yaml_frameworks)
    missing_in_enum = sorted(yaml_frameworks - enum_frameworks)

    has_error = False

    if missing_in_yaml:
        has_error = True
        print("[FAIL] Frameworks present in MappingFramework enum but missing in mappings/frameworks.yaml:")
        for item in missing_in_yaml:
            print(f"  - {item}")

    if missing_in_enum:
        has_error = True
        print("[FAIL] Frameworks present in mappings/frameworks.yaml but missing in MappingFramework enum:")
        for item in missing_in_enum:
            print(f"  - {item}")

    for catalog_path in catalogs:
        frameworks_in_catalog = extract_mapping_frameworks(catalog_path)
        unknown = sorted({item for item in frameworks_in_catalog if item not in yaml_frameworks})
        if unknown:
            has_error = True
            print(f"[FAIL] {catalog_path} contains frameworks not declared in mappings/frameworks.yaml:")
            for item in unknown:
                print(f"  - {item}")
        else:
            print(f"[OK] {catalog_path}: all mapping frameworks are declared")

    if has_error:
        raise SystemExit(1)

    print(f"Framework registry validation passed ({len(yaml_frameworks)} frameworks)")


if __name__ == "__main__":
    main()
