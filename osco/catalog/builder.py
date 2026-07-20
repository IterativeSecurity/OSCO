"""
Catalog build pipeline.

Applies curated mappings and critical capabilities to a raw capability source,
producing a clean gold catalog with verified framework cross-references.

Usage as library:
    from osco.catalog.builder import build_catalog, load_source, write_catalog

Usage via CLI:
    uv run scripts/build_catalog.py
    osco catalog build
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from osco.catalog.critical_capabilities import CRITICAL_CAPABILITIES
from osco.catalog.curated_mappings import CURATED_DESCRIPTIONS, CURATED_MAPPINGS

# Auto-generated fake IDs look like: sigma-3001, ecs-2338, mitre_attack-2336
_FAKE_ID_PATTERN = re.compile(r"^[a-z_]+-\d{3,6}$")


def _is_fake(external_id: str) -> bool:
    """Return True if external_id matches the auto-generated placeholder pattern."""
    return bool(_FAKE_ID_PATTERN.match(external_id))


def build_catalog(
    source: list[dict],
    *,
    apply_curated_mappings: bool = True,
    apply_curated_descriptions: bool = True,
    add_critical_capabilities: bool = True,
    strip_fake_mappings: bool = True,
) -> list[dict]:
    """
    Build a curated catalog from a source capability list.

    Steps:
    1. Optionally update descriptions for known capabilities.
    2. Strip auto-generated fake mapping IDs.
    3. Inject verified framework mappings for known capabilities.
    4. Append critical hand-authored capabilities not present in source.

    Args:
        source: Raw capability list (e.g. loaded from catalog.extended.json).
        apply_curated_mappings: Replace fake mappings with verified ones.
        apply_curated_descriptions: Update descriptions for curated capabilities.
        add_critical_capabilities: Append hand-authored capabilities not in source.
        strip_fake_mappings: Remove fake placeholder IDs with no verified replacement.

    Returns:
        Curated capability list ready to write as the gold catalog.
    """
    catalog = [dict(cap) for cap in source]

    for cap in catalog:
        cid = cap["capability_id"]

        if apply_curated_descriptions and cid in CURATED_DESCRIPTIONS:
            cap["description"] = CURATED_DESCRIPTIONS[cid]

        original_mappings = cap.get("mappings", [])
        real_existing = [m for m in original_mappings if not _is_fake(m["external_id"])]

        if apply_curated_mappings and cid in CURATED_MAPPINGS:
            # Merge base: real-only when stripping, full original when preserving
            merge_base = real_existing if strip_fake_mappings else list(original_mappings)
            existing_keys = {(m["framework"], m["external_id"]) for m in merge_base}
            merged = list(merge_base)
            for new_mapping in CURATED_MAPPINGS[cid]:
                key = (new_mapping["framework"], new_mapping["external_id"])
                if key not in existing_keys:
                    merged.append(new_mapping)
            cap["mappings"] = merged
        elif strip_fake_mappings:
            cap["mappings"] = real_existing

    if add_critical_capabilities:
        existing_ids = {c["capability_id"] for c in catalog}
        for cap in CRITICAL_CAPABILITIES:
            if cap["capability_id"] not in existing_ids:
                catalog.append(dict(cap))

    return catalog


def load_source(path: Path) -> list[dict]:
    """Load a capability catalog JSON file."""
    payload = json.loads(path.read_text())
    if not isinstance(payload, list):
        raise ValueError(f"Expected a JSON list in {path}")
    return payload


def write_catalog(catalog: list[dict], path: Path) -> None:
    """Write a capability catalog to JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(catalog, indent=2) + "\n")


def catalog_stats(catalog: list[dict]) -> dict[str, int]:
    """Return summary statistics for a catalog."""
    with_mappings = sum(1 for c in catalog if c.get("mappings"))
    without_mappings = sum(1 for c in catalog if not c.get("mappings"))
    total_mappings = sum(len(c.get("mappings", [])) for c in catalog)
    return {
        "total": len(catalog),
        "with_mappings": with_mappings,
        "without_mappings": without_mappings,
        "total_mapping_references": total_mappings,
    }
