from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "capability" / "catalog.json"
EXTENDED_PATH = ROOT / "capability" / "catalog.extended.json"

TARGET_COUNT = 320
MIN_PER_DOMAIN = 4

SEED_IDS = {
    "filesystem.file.create",
    "registry.key.set",
    "windows.task.create",
    "cloud.iam.role.create",
    "mail.forwarding.create",
    "network.dns.query",
    "kubernetes.secret.read",
    "browser.cookie.read",
    "database.role.grant",
    "collection.persistence.evidence.collect",
    "detection.registry.persistence.detect",
    "validation.persistence.endpoint.validate",
}

HIGH_VALUE_FRAMEWORKS = {
    "mitre_attack",
    "sigma",
    "ocsf",
    "atomic_red_team",
    "velociraptor",
    "ecs",
    "osquery",
    "event_maturity_matrix",
}


def score_capability(capability: dict) -> int:
    score = 0

    if capability["capability_id"] in SEED_IDS:
        score += 100

    frameworks = {mapping.get("framework") for mapping in capability.get("mappings", [])}
    score += 8 * len(frameworks & HIGH_VALUE_FRAMEWORKS)
    score += 2 * len(frameworks)

    safety = capability.get("safety", "caution")
    if safety == "safe":
        score += 12
    elif safety == "caution":
        score += 8
    elif safety == "destructive":
        score += 2

    score += min(len(capability.get("providers", [])), 4)
    score += min(len(capability.get("platforms", [])), 4)

    category = capability.get("category", "")
    if category in {"collection", "detection", "validation", "response", "telemetry", "identity"}:
        score += 6

    return score


def main() -> None:
    full_catalog = json.loads(CATALOG_PATH.read_text())

    # Preserve the complete corpus as an extended catalog.
    EXTENDED_PATH.write_text(json.dumps(full_catalog, indent=2) + "\n")

    by_domain: dict[str, list[dict]] = defaultdict(list)
    for capability in full_catalog:
        by_domain[capability["domain"]].append(capability)

    for domain in by_domain:
        by_domain[domain].sort(
            key=lambda item: (
                -score_capability(item),
                item["capability_id"],
            )
        )

    selected: list[dict] = []
    selected_ids: set[str] = set()

    # Pass 1: guarantee domain breadth.
    for domain in sorted(by_domain):
        domain_items = by_domain[domain]
        for capability in domain_items[:MIN_PER_DOMAIN]:
            cap_id = capability["capability_id"]
            if cap_id not in selected_ids:
                selected.append(capability)
                selected_ids.add(cap_id)

    # Pass 2: global quality fill up to target.
    global_ranked = sorted(
        full_catalog,
        key=lambda item: (-score_capability(item), item["capability_id"]),
    )
    for capability in global_ranked:
        if len(selected) >= TARGET_COUNT:
            break
        cap_id = capability["capability_id"]
        if cap_id in selected_ids:
            continue
        selected.append(capability)
        selected_ids.add(cap_id)

    selected.sort(key=lambda item: item["capability_id"])
    for idx, capability in enumerate(selected, start=1):
        capability["stable_id"] = f"OSCO-CAP-{idx:04d}"

    CATALOG_PATH.write_text(json.dumps(selected, indent=2) + "\n")

    print(f"Extended catalog size: {len(full_catalog)}")
    print(f"Gold catalog size: {len(selected)}")
    print(f"Domains covered: {len({item['domain'] for item in selected})}")


if __name__ == "__main__":
    main()
