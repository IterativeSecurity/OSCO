#!/usr/bin/env python3
"""
Generate detection/catalog.md from detection/detections.json.

Usage:
    uv run scripts/generate_detection_readme.py
    uv run scripts/generate_detection_readme.py --dry-run
"""
from __future__ import annotations

import argparse
from pathlib import Path

from osco.generators.detections import DETECTIONS_PATH, OUTPUT_PATH, generate


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate detection catalog markdown")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing")
    parser.add_argument("--detections", type=Path, default=DETECTIONS_PATH)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()
    generate(detections_path=args.detections, output_path=args.output, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
