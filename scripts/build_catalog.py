#!/usr/bin/env python3
"""
Build the OSCO gold capability catalog.

Applies curated mappings and adds critical hand-authored capabilities
to the extended corpus, producing capability/catalog.json.

Usage:
    uv run scripts/build_catalog.py
    uv run scripts/build_catalog.py --dry-run
    uv run scripts/build_catalog.py --source capability/catalog.extended.json --output capability/catalog.json
"""
from __future__ import annotations

import argparse
from pathlib import Path

from osco.catalog.builder import build_catalog, catalog_stats, load_source, write_catalog

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the OSCO gold capability catalog")
    parser.add_argument(
        "--source",
        type=Path,
        default=ROOT / "capability" / "catalog.extended.json",
        help="Source catalog to build from (default: capability/catalog.extended.json)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "capability" / "catalog.json",
        help="Output path (default: capability/catalog.json)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print stats without writing")
    parser.add_argument("--no-critical", action="store_true", help="Skip adding critical capabilities")
    parser.add_argument("--no-strip", action="store_true", help="Keep fake placeholder mapping IDs")
    args = parser.parse_args()

    raw = load_source(args.source)
    curated = build_catalog(
        raw,
        add_critical_capabilities=not args.no_critical,
        strip_fake_mappings=not args.no_strip,
    )

    stats = catalog_stats(curated)
    print(f"Source:           {args.source} ({len(raw)} capabilities)")
    print(f"Total:            {stats['total']} capabilities")
    print(f"With mappings:    {stats['with_mappings']}")
    print(f"Without mappings: {stats['without_mappings']}")
    print(f"Total references: {stats['total_mapping_references']}")

    if not args.dry_run:
        write_catalog(curated, args.output)
        print(f"\nWrote {args.output}")
    else:
        print("\n[dry-run] No files written.")


if __name__ == "__main__":
    main()
