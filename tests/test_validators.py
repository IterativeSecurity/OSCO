"""Test validation script functionality."""

import json
import tempfile
from pathlib import Path

import pytest
import yaml

from scripts.validate_mapping_frameworks import (
    extract_mapping_frameworks,
    load_frameworks_enum,
    load_frameworks_yaml,
)
from scripts.validate_ontology_taxonomy import (
    iter_allowed_paths,
    load_allowed_capabilities,
    load_capability_ids,
    validate_catalog,
)


class TestOntologyTaxonomy:
    """Test ontology taxonomy validation functions."""

    def test_iter_allowed_paths_simple_dict(self) -> None:
        node = {"persistence": {"evidence": ["collect"]}}
        paths = iter_allowed_paths(node, [])
        assert ("persistence", "evidence", "collect") in paths

    def test_iter_allowed_paths_with_actions(self) -> None:
        node = {"execution": {"_actions": ["code.execute", "script.execute"]}}
        paths = iter_allowed_paths(node, [])
        assert ("execution", "code", "execute") in paths
        assert ("execution", "script", "execute") in paths

    def test_iter_allowed_paths_nested(self) -> None:
        # Test nested structure with list values at the end
        node = {"domain": {"object": ["action1", "action2"]}}
        paths = iter_allowed_paths(node, [])
        assert ("domain", "object", "action1") in paths
        assert ("domain", "object", "action2") in paths

    def test_load_allowed_capabilities_valid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            taxonomy_path = Path(tmpdir) / "ontology.yaml"
            taxonomy_data = {
                "domains": {
                    "persistence": {"evidence": ["collect"]},
                    "execution": {"code": ["execute"]},
                }
            }
            taxonomy_path.write_text(yaml.dump(taxonomy_data))

            allowed = load_allowed_capabilities(taxonomy_path)
            assert ("persistence", "evidence", "collect") in allowed
            assert ("execution", "code", "execute") in allowed

    def test_load_allowed_capabilities_missing_domains(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            taxonomy_path = Path(tmpdir) / "ontology.yaml"
            taxonomy_path.write_text(yaml.dump({"notdomains": {}}))

            with pytest.raises(ValueError):
                load_allowed_capabilities(taxonomy_path)

    def test_load_capability_ids_valid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            catalog_path = Path(tmpdir) / "catalog.json"
            catalog = [
                {"capability_id": "persistence.evidence.collect", "name": "Collect"},
                {"capability_id": "execution.code.execute", "name": "Execute"},
            ]
            catalog_path.write_text(json.dumps(catalog))

            ids = load_capability_ids(catalog_path)
            assert "persistence.evidence.collect" in ids
            assert "execution.code.execute" in ids

    def test_load_capability_ids_missing_field(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            catalog_path = Path(tmpdir) / "catalog.json"
            catalog = [{"name": "Missing ID"}]
            catalog_path.write_text(json.dumps(catalog))

            with pytest.raises(ValueError, match="missing capability_id"):
                load_capability_ids(catalog_path)

    def test_validate_catalog_all_valid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            catalog_path = Path(tmpdir) / "catalog.json"
            catalog = [
                {"capability_id": "test.object.action", "name": "Test"},
            ]
            catalog_path.write_text(json.dumps(catalog))

            allowed = {("test", "object", "action")}
            missing = validate_catalog(catalog_path, allowed)
            assert len(missing) == 0

    def test_validate_catalog_missing_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            catalog_path = Path(tmpdir) / "catalog.json"
            catalog = [
                {"capability_id": "unknown.capability.id", "name": "Unknown"},
            ]
            catalog_path.write_text(json.dumps(catalog))

            allowed = {("test", "object", "action")}
            missing = validate_catalog(catalog_path, allowed)
            assert "unknown.capability.id" in missing


class TestMappingFrameworkValidation:
    """Test mapping framework validation functions."""

    def test_load_frameworks_enum(self) -> None:
        frameworks = load_frameworks_enum()
        assert "mitre_attack" in frameworks
        assert "atomic_red_team" in frameworks
        assert "sigma" in frameworks
        assert len(frameworks) == 26

    def test_load_frameworks_yaml_valid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            frameworks_path = Path(tmpdir) / "frameworks.yaml"
            frameworks_data = {
                "frameworks": ["mitre_attack", "sigma", "aws_security_hub"]
            }
            frameworks_path.write_text(yaml.dump(frameworks_data))

            frameworks = load_frameworks_yaml(frameworks_path)
            assert "mitre_attack" in frameworks
            assert "sigma" in frameworks
            assert len(frameworks) == 3

    def test_load_frameworks_yaml_invalid_structure(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            frameworks_path = Path(tmpdir) / "frameworks.yaml"
            frameworks_path.write_text(yaml.dump({"notframeworks": []}))

            with pytest.raises(ValueError, match="must contain top-level 'frameworks'"):
                load_frameworks_yaml(frameworks_path)

    def test_extract_mapping_frameworks_valid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            catalog_path = Path(tmpdir) / "catalog.json"
            catalog = [
                {
                    "capability_id": "test.capability",
                    "mappings": [
                        {
                            "framework": "mitre_attack",
                            "external_id": "T1234",
                        },
                        {
                            "framework": "sigma",
                            "external_id": "sigma-001",
                        },
                    ],
                },
            ]
            catalog_path.write_text(json.dumps(catalog))

            frameworks = extract_mapping_frameworks(catalog_path)
            assert "mitre_attack" in frameworks
            assert "sigma" in frameworks

    def test_extract_mapping_frameworks_missing_field(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            catalog_path = Path(tmpdir) / "catalog.json"
            catalog = [
                {
                    "capability_id": "test.capability",
                    "mappings": [{"external_id": "T1234"}],  # Missing framework
                },
            ]
            catalog_path.write_text(json.dumps(catalog))

            with pytest.raises(ValueError, match="missing 'framework'"):
                extract_mapping_frameworks(catalog_path)

