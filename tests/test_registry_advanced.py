"""Test registry advanced functionality."""

import pytest

from osco.registry import OSCORegistry


class TestRegistrySearch:
    """Test registry search and filtering capabilities."""

    @pytest.fixture
    def registry(self) -> OSCORegistry:
        return OSCORegistry()

    def test_search_capabilities_by_name(self, registry: OSCORegistry) -> None:
        results = registry.search_capabilities("persistence")
        assert len(results) > 0
        assert any("persistence" in cap.capability_id.lower() for cap in results)

    def test_search_capabilities_case_insensitive(self, registry: OSCORegistry) -> None:
        results_lower = registry.search_capabilities("persistence")
        results_upper = registry.search_capabilities("PERSISTENCE")
        assert len(results_lower) == len(results_upper)

    def test_search_capabilities_no_results(self, registry: OSCORegistry) -> None:
        results = registry.search_capabilities("nonexistent_capability_xyz")
        assert len(results) == 0

    def test_list_capabilities_count(self, registry: OSCORegistry) -> None:
        capabilities = registry.list_capabilities()
        assert len(capabilities) >= 320

    def test_list_providers_count(self, registry: OSCORegistry) -> None:
        providers = registry.list_providers()
        assert len(providers) >= 16

    def test_bundle_has_detections(self, registry: OSCORegistry) -> None:
        detections = registry.bundle.detections
        assert isinstance(detections, list)

    def test_bundle_has_validations(self, registry: OSCORegistry) -> None:
        validations = registry.bundle.validations
        assert isinstance(validations, list)

    def test_get_capability_by_id(self, registry: OSCORegistry) -> None:
        capabilities = registry.list_capabilities()
        if capabilities:
            cap_id = capabilities[0].capability_id
            # Try to get it via search
            results = registry.search_capabilities(cap_id)
            assert len(results) > 0
            assert results[0].capability_id == cap_id

    def test_bundle_structure(self, registry: OSCORegistry) -> None:
        bundle = registry.bundle
        assert hasattr(bundle, "capabilities")
        assert hasattr(bundle, "providers")
        assert isinstance(bundle.capabilities, list)
        assert isinstance(bundle.providers, list)

    def test_registry_loads_all_catalogs(self, registry: OSCORegistry) -> None:
        # Verify all required catalogs are loaded
        assert len(registry.list_capabilities()) > 0
        assert len(registry.list_providers()) > 0
        assert isinstance(registry.bundle.detections, list)
        assert isinstance(registry.bundle.validations, list)

    def test_search_returns_capabilities(self, registry: OSCORegistry) -> None:
        results = registry.search_capabilities("execute")
        for cap in results:
            assert hasattr(cap, "capability_id")
            assert hasattr(cap, "name")
            assert hasattr(cap, "description")


class TestRegistryConsistency:
    """Test data consistency in loaded catalogs."""

    @pytest.fixture
    def registry(self) -> OSCORegistry:
        return OSCORegistry()

    def test_all_capabilities_have_required_fields(self, registry: OSCORegistry) -> None:
        for cap in registry.list_capabilities():
            assert cap.capability_id
            assert cap.name
            assert cap.description
            assert cap.domain
            assert cap.category
            assert len(cap.platforms) > 0

    def test_all_providers_have_required_fields(self, registry: OSCORegistry) -> None:
        for provider in registry.list_providers():
            assert provider.provider_id
            assert provider.name
            assert provider.category
            assert len(provider.platforms) > 0
            assert provider.description

    def test_capability_ids_are_unique(self, registry: OSCORegistry) -> None:
        capability_ids = [cap.capability_id for cap in registry.list_capabilities()]
        assert len(capability_ids) == len(set(capability_ids))

    def test_provider_ids_are_unique(self, registry: OSCORegistry) -> None:
        provider_ids = [p.provider_id for p in registry.list_providers()]
        assert len(provider_ids) == len(set(provider_ids))

    def test_capability_providers_are_valid(self, registry: OSCORegistry) -> None:
        valid_provider_ids = {p.provider_id for p in registry.list_providers()}
        for cap in registry.list_capabilities():
            for provider_id in cap.providers:
                assert provider_id in valid_provider_ids, f"Invalid provider {provider_id} in {cap.capability_id}"

    def test_all_mappings_have_valid_frameworks(self, registry: OSCORegistry) -> None:
        for cap in registry.list_capabilities():
            for mapping in cap.mappings:
                assert mapping.framework
                assert mapping.external_id
                assert mapping.external_name
