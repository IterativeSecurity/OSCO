from __future__ import annotations

import json
from pathlib import Path

from jsonschema import validate

from osco.models.core import Capability


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    schema = json.loads((ROOT / "jsonschema" / "capability.schema.json").read_text())
    capabilities = json.loads((ROOT / "capability" / "catalog.json").read_text())

    for item in capabilities:
        Capability.model_validate(item)
        validate(item, schema)

    print(f"Validated {len(capabilities)} capabilities successfully.")


if __name__ == "__main__":
    main()
