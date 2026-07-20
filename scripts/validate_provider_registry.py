from __future__ import annotations

import json
from pathlib import Path

from osco.models.core import Capability, Provider


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    providers_payload = json.loads((ROOT / "provider" / "providers.json").read_text())
    capabilities_payload = json.loads((ROOT / "capability" / "catalog.json").read_text())

    providers = [Provider.model_validate(item) for item in providers_payload]
    capabilities = [Capability.model_validate(item) for item in capabilities_payload]

    provider_ids = {provider.provider_id for provider in providers}

    unknown_refs: list[tuple[str, str]] = []
    for capability in capabilities:
        for provider_id in capability.providers:
            if provider_id not in provider_ids:
                unknown_refs.append((capability.capability_id, provider_id))

    if unknown_refs:
        print("[FAIL] Unknown provider references found in capability catalog:")
        for capability_id, provider_id in unknown_refs[:50]:
            print(f"  - {capability_id} -> {provider_id}")
        if len(unknown_refs) > 50:
            print(f"  ... and {len(unknown_refs) - 50} more")
        raise SystemExit(1)

    print(f"[OK] Providers validated: {len(providers)}")
    print(f"[OK] Capabilities checked: {len(capabilities)}")
    print("Provider registry validation passed.")


if __name__ == "__main__":
    main()
