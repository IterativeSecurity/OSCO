"""Generate the discovery catalog markdown table."""
from __future__ import annotations

import json
from pathlib import Path

from osco.generators.common import ROOT, write_generated_file

DISCOVERIES_PATH = ROOT / "discovery" / "discoveries.json"
OUTPUT_PATH = ROOT / "discovery" / "catalog.md"
COMMAND = "make generate  # or: uv run scripts/generate_discovery_readme.py"


def build_table(discoveries: list[dict]) -> str:
    api_methods = [d for d in discoveries if d.get("type") == "api"]
    api_methods.sort(key=lambda d: d["method_id"])

    lines = [
        "# Discovery Catalog",
        "",
        "| Method ID | State | Description | Providers |",
        "|---|---|---|---|",
    ]

    for method in api_methods:
        method_id = f"`{method['method_id']}`"
        state = method.get("state", "")
        description = method.get("description", "").rstrip(".")

        if method.get("queries"):
            providers = sorted({q["provider"] for q in method["queries"]})
            providers_str = ", ".join(providers)
        elif method.get("query"):
            providers_str = "legacy"
        else:
            providers_str = "—"

        lines.append(f"| {method_id} | {state} | {description} | {providers_str} |")

    total_api = len(api_methods)
    total_declared = sum(1 for d in discoveries if d.get("type") == "declared")
    total = len(discoveries)

    lines += [
        "",
        f"**Total:** {total} entries — {total_api} API-based, {total_declared} declared.",
    ]

    return "\n".join(lines)


def generate(
    discoveries_path: Path = DISCOVERIES_PATH,
    output_path: Path = OUTPUT_PATH,
    dry_run: bool = False,
) -> str:
    discoveries = json.loads(discoveries_path.read_text())
    content = build_table(discoveries)

    if dry_run:
        print(content)
        return content

    write_generated_file(output_path, content, COMMAND)
    return content
