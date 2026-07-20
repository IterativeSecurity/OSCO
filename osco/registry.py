from __future__ import annotations

import json
from pathlib import Path

from osco.models.core import Capability, OSCOBundle, Provider


class OSCORegistry:
    """Loads and queries OSCO catalog data."""

    def __init__(self, root: Path | None = None) -> None:
        package_root = Path(__file__).resolve().parents[1]
        self.root = root or package_root
        self.bundle = self._load_bundle()

    def _load_bundle(self) -> OSCOBundle:
        data_file = self.root / "capability" / "catalog.json"
        provider_file = self.root / "provider" / "providers.json"
        detection_file = self.root / "detection" / "detections.json"
        validation_file = self.root / "validation" / "validations.json"

        capabilities = json.loads(data_file.read_text())
        providers = json.loads(provider_file.read_text())
        detections = json.loads(detection_file.read_text())
        validations = json.loads(validation_file.read_text())

        return OSCOBundle(
            capabilities=[Capability.model_validate(item) for item in capabilities],
            providers=[Provider.model_validate(item) for item in providers],
            detections=detections,
            validations=validations,
        )

    def search_capabilities(self, query: str) -> list[Capability]:
        needle = query.lower()
        return [
            capability
            for capability in self.bundle.capabilities
            if needle in capability.capability_id.lower()
            or needle in capability.name.lower()
            or needle in capability.description.lower()
        ]

    def list_providers(self) -> list[Provider]:
        return self.bundle.providers

    def list_capabilities(self) -> list[Capability]:
        return self.bundle.capabilities
