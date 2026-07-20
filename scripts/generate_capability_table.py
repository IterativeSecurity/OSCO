#!/usr/bin/env python3
"""
Generate capability/catalog.md and optionally capability/catalog.extended.md.

Usage:
    uv run scripts/generate_capability_table.py
    uv run scripts/generate_capability_table.py --extended
    uv run scripts/generate_capability_table.py --dry-run
"""
from __future__ import annotations

import argparse
from pathlib import Path

from osco.generators.capabilities import (
    CATALOG_PATH,
    EXTENDED_OUTPUT_PATH,
    EXTENDED_PATH,
    OUTPUT_PATH,
    generate,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate capability catalog markdown")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing")
    parser.add_argument("--extended", action="store_true", help="Also generate extended catalog")
    parser.add_argument("--catalog", type=Path, default=CATALOG_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    generate(catalog_path=args.catalog, output_path=args.output, dry_run=args.dry_run)

    if args.extended:
        generate(
            catalog_path=EXTENDED_PATH,
            output_path=EXTENDED_OUTPUT_PATH,
            title="Capability Catalog (Extended)",
            dry_run=args.dry_run,
        )


if __name__ == "__main__":
    main()
