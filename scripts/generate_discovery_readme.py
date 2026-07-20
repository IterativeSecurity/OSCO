#!/usr/bin/env python3
"""
Generate discovery/catalog.md from discovery/discoveries.json.

Usage:
    uv run scripts/generate_discovery_readme.py
    uv run scripts/generate_discovery_readme.py --dry-run
"""
from __future__ import annotations

import argparse
from pathlib import Path

from osco.generators.discoveries import DISCOVERIES_PATH, OUTPUT_PATH, generate


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate discovery catalog markdown")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing")
    parser.add_argument("--discoveries", type=Path, default=DISCOVERIES_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()
    generate(discoveries_path=args.discoveries, output_path=args.output, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
