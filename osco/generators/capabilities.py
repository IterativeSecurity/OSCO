"""Generate the capability catalog markdown table."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from osco.generators.common import ROOT, write_generated_file

CATALOG_PATH = ROOT / "capability" / "catalog.json"
EXTENDED_PATH = ROOT / "capability" / "catalog.extended.json"
OUTPUT_PATH = ROOT / "capability" / "catalog.md"
EXTENDED_OUTPUT_PATH = ROOT / "capability" / "catalog.extended.md"
COMMAND = "make generate  # or: uv run scripts/generate_capability_table.py"


def _count(item: dict, key: str) -> int:
    v = item.get(key, [])
    return len(v) if isinstance(v, list) else 0


def build_table(capabilities: list[dict]) -> str:
    lines = [
        "| Stable ID | Capability ID | Name | Domain | Category | Safety | Status | Confidence | Providers | Platforms | Mappings |",
        "|---|---|---|---|---|---|---|---:|---:|---:|---:|",
    ]
    for item in capabilities:
        lines.append(
            "| "
            + " | ".join([
                item.get("stable_id", ""),
                item.get("capability_id", ""),
                item.get("name", ""),
                item.get("domain", ""),
                item.get("category", ""),
                item.get("safety", ""),
                item.get("status", ""),
                f"{item.get('confidence', 0):.2f}",
                str(_count(item, "providers")),
                str(_count(item, "platforms")),
                str(_count(item, "mappings")),
            ])
            + " |"
        )
    return "\n".join(lines)


def build_content(capabilities: list[dict], source_name: str, title: str) -> str:
    capabilities = sorted(capabilities, key=lambda c: c.get("capability_id", ""))
    domain_counts = Counter(c.get("domain", "unknown") for c in capabilities)
    category_counts = Counter(c.get("category", "unknown") for c in capabilities)
    top_domains = ", ".join(f"{n} ({v})" for n, v in domain_counts.most_common(10))
    top_categories = ", ".join(f"{n} ({v})" for n, v in category_counts.most_common(10))

    return f"""# {title}

## Summary

- **Total capabilities:** {len(capabilities)}
- **Distinct domains:** {len(domain_counts)}
- **Distinct categories:** {len(category_counts)}
- **Top domains:** {top_domains}
- **Top categories:** {top_categories}

## Table

{build_table(capabilities)}
"""


def generate(
    catalog_path: Path = CATALOG_PATH,
    output_path: Path = OUTPUT_PATH,
    title: str = "Capability Catalog",
    dry_run: bool = False,
) -> str:
    capabilities = json.loads(catalog_path.read_text())
    content = build_content(capabilities, catalog_path.name, title)

    if dry_run:
        print(content)
        return content

    write_generated_file(output_path, content, COMMAND)
    return content
