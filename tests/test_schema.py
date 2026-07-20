import json
from pathlib import Path

from jsonschema import validate


ROOT = Path(__file__).resolve().parents[1]


def test_capabilities_validate_against_schema() -> None:
    schema = json.loads((ROOT / "jsonschema" / "capability.schema.json").read_text())
    capabilities = json.loads((ROOT / "capability" / "catalog.json").read_text())

    for capability in capabilities:
        validate(instance=capability, schema=schema)
