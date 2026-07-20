"""Test OSCO Pydantic models for validation and structure."""

import pytest
from pydantic import ValidationError

from osco.models.core import (
    Capability,
    CapabilityMapping,
    Detection,
    DiscoveryMethod,
    DiscoveryState,
    MappingFramework,
    Platform,
    Provider,
    SafetyClassification,
    Validation,
    VerificationMethod,
)


class TestSafetyClassification:
    """Test SafetyClassification enum."""

    def test_valid_values(self) -> None:
        assert SafetyClassification.safe.value == "safe"
        assert SafetyClassification.caution.value == "caution"
        assert SafetyClassification.destructive.value == "destructive"

    def test_enum_count(self) -> None:
        assert len(list(SafetyClassification)) == 3


class TestDiscoveryState:
    """Test DiscoveryState enum."""

    def test_valid_states(self) -> None:
        assert DiscoveryState.declared.value == "declared"
        assert DiscoveryState.observed.value == "observed"
        assert DiscoveryState.verified.value == "verified"
        assert DiscoveryState.proven.value == "proven"

    def test_enum_count(self) -> None:
        assert len(list(DiscoveryState)) == 4


class TestMappingFramework:
    """Test MappingFramework enum."""

    def test_all_frameworks_exist(self) -> None:
        frameworks = {item.value for item in MappingFramework}
        assert "mitre_attack" in frameworks
        assert "atomic_red_team" in frameworks
        assert "sigma" in frameworks
        assert "aws_security_hub" in frameworks

    def test_framework_count(self) -> None:
        assert len(list(MappingFramework)) == 26


class TestPlatform:
    """Test Platform enum."""

    def test_valid_platforms(self) -> None:
        platforms = {item.value for item in Platform}
        assert "windows" in platforms
        assert "linux" in platforms
        assert "macos" in platforms
        assert "cloud" in platforms


class TestDiscoveryMethod:
    """Test DiscoveryMethod model."""

    def test_discovery_method_minimal(self) -> None:
        method = DiscoveryMethod(
            method_id="discover.test",
            type="api",
            state=DiscoveryState.verified,
            description="Test discovery method",
        )
        assert method.method_id == "discover.test"
        assert method.type == "api"
        assert method.state == DiscoveryState.verified

    def test_discovery_method_with_query(self) -> None:
        method = DiscoveryMethod(
            method_id="discover.process",
            type="api",
            state=DiscoveryState.verified,
            description="Find processes",
            query="Get-Process",
        )
        assert method.query == "Get-Process"

    def test_discovery_method_invalid_state(self) -> None:
        with pytest.raises(ValidationError):
            DiscoveryMethod(
                method_id="discover.test",
                type="api",
                state="invalid",  # type: ignore
                description="Test",
            )


class TestVerificationMethod:
    """Test VerificationMethod model."""

    def test_verification_method_minimal(self) -> None:
        method = VerificationMethod(
            method_id="verify.test",
            type="safe_execute",
            description="Test verification",
        )
        assert method.method_id == "verify.test"
        assert method.type == "safe_execute"

    def test_verification_method_with_flags(self) -> None:
        method = VerificationMethod(
            method_id="verify.test",
            type="safe_execute",
            description="Test verification",
            supports_dry_run=True,
            supports_safe_mode=True,
            supports_cleanup=True,
            supports_rollback=True,
        )
        assert method.supports_dry_run is True
        assert method.supports_cleanup is True


class TestCapabilityMapping:
    """Test CapabilityMapping model."""

    def test_mapping_minimal(self) -> None:
        mapping = CapabilityMapping(
            framework=MappingFramework.mitre_attack,
            external_id="T1234",
            external_name="Test Technique",
        )
        assert mapping.framework == MappingFramework.mitre_attack
        assert mapping.external_id == "T1234"

    def test_mapping_with_relation_and_confidence(self) -> None:
        mapping = CapabilityMapping(
            framework=MappingFramework.atomic_red_team,
            external_id="T1234.001",
            external_name="Test Sub-technique",
            relation="maps_to",
            confidence=0.95,
        )
        assert mapping.relation == "maps_to"
        assert mapping.confidence == 0.95

    def test_mapping_confidence_bounds(self) -> None:
        # Valid confidence
        mapping = CapabilityMapping(
            framework=MappingFramework.mitre_attack,
            external_id="T1234",
            external_name="Test",
            confidence=0.5,
        )
        assert mapping.confidence == 0.5

        # Invalid confidence (out of bounds)
        with pytest.raises(ValidationError):
            CapabilityMapping(
                framework=MappingFramework.mitre_attack,
                external_id="T1234",
                external_name="Test",
                confidence=1.5,  # type: ignore
            )


class TestDetection:
    """Test Detection model."""

    def test_detection_minimal(self) -> None:
        detection = Detection(
            detection_id="det.test.001",
            name="Test Detection",
            description="A test detection",
        )
        assert detection.detection_id == "det.test.001"
        assert detection.name == "Test Detection"

    def test_detection_with_mappings(self) -> None:
        mapping = CapabilityMapping(
            framework=MappingFramework.sigma,
            external_id="sigma-001",
            external_name="Test Rule",
        )
        detection = Detection(
            detection_id="det.test.001",
            name="Test Detection",
            description="A test detection",
            mappings=[mapping],
        )
        assert len(detection.mappings) == 1
        assert detection.mappings[0].framework == MappingFramework.sigma


class TestValidation:
    """Test Validation model."""

    def test_validation_minimal(self) -> None:
        validation = Validation(
            validation_id="val.test.001",
            name="Test Validation",
            description="A test validation scenario",
        )
        assert validation.validation_id == "val.test.001"
        assert validation.name == "Test Validation"

    def test_validation_with_mappings(self) -> None:
        mapping = CapabilityMapping(
            framework=MappingFramework.mitre_attack,
            external_id="T1234",
            external_name="Test Technique",
            confidence=0.9,
        )
        validation = Validation(
            validation_id="val.test.001",
            name="Test Validation",
            description="A test validation scenario",
            mappings=[mapping],
        )
        assert len(validation.mappings) == 1


class TestProvider:
    """Test Provider model."""

    def test_provider_minimal(self) -> None:
        provider = Provider(
            provider_id="test_provider",
            name="Test Provider",
            category="endpoint",
            platforms=[Platform.windows, Platform.linux],
            description="A test provider",
        )
        assert provider.provider_id == "test_provider"
        assert provider.name == "Test Provider"
        assert len(provider.platforms) == 2

    def test_provider_with_optional_fields(self) -> None:
        provider = Provider(
            provider_id="test_provider",
            name="Test Provider",
            category="endpoint",
            platforms=[Platform.windows],
            description="A test provider",
            homepage="https://example.com",
        )
        assert provider.homepage == "https://example.com"

    def test_provider_platforms_field(self) -> None:
        # Verify platforms is required but can have items
        provider = Provider(
            provider_id="test",
            name="Test",
            category="endpoint",
            platforms=[Platform.windows],
            description="Test",
        )
        assert len(provider.platforms) == 1


class TestCapability:
    """Test Capability model."""

    def test_capability_minimal(self) -> None:
        cap = Capability(
            capability_id="test.capability.create",
            stable_id="OSCO-TEST-001",
            name="Test Capability",
            description="A test capability",
            category="test",
            domain="test",
            platforms=[Platform.windows],
        )
        assert cap.capability_id == "test.capability.create"
        assert cap.stable_id == "OSCO-TEST-001"
        assert cap.category == "test"
        assert len(cap.platforms) >= 1

    def test_capability_with_discovery_methods(self) -> None:
        discovery = DiscoveryMethod(
            method_id="discover.test",
            type="declared",
            state=DiscoveryState.declared,
            description="Test discovery",
        )
        cap = Capability(
            capability_id="test.capability.create",
            stable_id="OSCO-TEST-001",
            name="Test Capability",
            description="A test capability",
            category="test",
            domain="test",
            platforms=[Platform.windows],
            discovery_methods=[discovery],
        )
        assert len(cap.discovery_methods) == 1

    def test_capability_with_verification_methods(self) -> None:
        verify = VerificationMethod(
            method_id="verify.test",
            type="safe_execute",
            description="Test verification",
        )
        cap = Capability(
            capability_id="test.capability.create",
            stable_id="OSCO-TEST-001",
            name="Test Capability",
            description="A test capability",
            category="test",
            domain="test",
            platforms=[Platform.windows],
            verification_methods=[verify],
        )
        assert len(cap.verification_methods) == 1

    def test_capability_with_all_fields(self) -> None:
        cap = Capability(
            capability_id="test.capability.create",
            stable_id="OSCO-TEST-001",
            name="Test Capability",
            description="A test capability",
            category="test",
            domain="test",
            platforms=[Platform.windows, Platform.linux],
            providers=["provider1", "provider2"],
            status="active",
            confidence=0.95,
            safety=SafetyClassification.safe,
            mappings=[
                CapabilityMapping(
                    framework=MappingFramework.mitre_attack,
                    external_id="T1234",
                    external_name="Test",
                )
            ],
        )
        assert cap.providers == ["provider1", "provider2"]
        assert cap.status == "active"
        assert cap.confidence == 0.95
        assert cap.safety == SafetyClassification.safe
        assert len(cap.mappings) == 1
