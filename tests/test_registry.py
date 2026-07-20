from osco.registry import OSCORegistry


def test_registry_loads() -> None:
    registry = OSCORegistry()
    assert len(registry.list_capabilities()) >= 10
    assert len(registry.list_providers()) >= 16


def test_capability_search() -> None:
    registry = OSCORegistry()
    results = registry.search_capabilities("persistence")
    assert any(item.capability_id == "collection.persistence.evidence.collect" for item in results)
