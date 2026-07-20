"""Generate the detection catalog markdown table."""
from __future__ import annotations

import json
from pathlib import Path

from osco.generators.common import ROOT, write_generated_file

DETECTIONS_PATH = ROOT / "detection" / "detections.json"
OUTPUT_PATH = ROOT / "detection" / "catalog.md"
COMMAND = "make generate  # or: uv run scripts/generate_detection_readme.py"

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}
SEVERITY_BADGE = {
    "critical": "🔴 critical",
    "high": "🟠 high",
    "medium": "🟡 medium",
    "low": "🟢 low",
}


def build_table(detections: list[dict]) -> str:
    detections = sorted(
        detections,
        key=lambda d: (SEVERITY_ORDER.get(d.get("severity", "medium"), 99), d["detection_id"]),
    )

    lines = [
        "# Detection Catalog",
        "",
        "| Detection ID | Name | Severity | Platforms | Capabilities | ATT&CK |",
        "|---|---|---|---|---|---|",
    ]

    for det in detections:
        det_id = f"`{det['detection_id']}`"
        name = det.get("name", "")
        severity = SEVERITY_BADGE.get(det.get("severity", "medium"), det.get("severity", ""))
        platforms = ", ".join(det.get("platforms", []))
        cap_ids = ", ".join(f"`{c}`" for c in det.get("capability_ids", []))
        attack_ids = [
            m["external_id"]
            for m in det.get("mappings", [])
            if m.get("framework") == "mitre_attack"
        ]
        attack = ", ".join(attack_ids) if attack_ids else "—"
        lines.append(f"| {det_id} | {name} | {severity} | {platforms} | {cap_ids} | {attack} |")

    by_severity: dict[str, int] = {}
    for d in detections:
        s = d.get("severity", "medium")
        by_severity[s] = by_severity.get(s, 0) + 1

    severity_summary = ", ".join(
        f"{SEVERITY_BADGE.get(k, k)}: {v}"
        for k, v in sorted(by_severity.items(), key=lambda x: SEVERITY_ORDER.get(x[0], 99))
    )

    lines += [
        "",
        f"**Total:** {len(detections)} detections — {severity_summary}.",
    ]

    return "\n".join(lines)


def generate(
    detections_path: Path = DETECTIONS_PATH,
    output_path: Path = OUTPUT_PATH,
    dry_run: bool = False,
) -> str:
    detections = json.loads(detections_path.read_text())
    content = build_table(detections)

    if dry_run:
        print(content)
        return content

    write_generated_file(output_path, content, COMMAND)
    return content
