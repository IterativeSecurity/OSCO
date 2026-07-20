"""Tests for the catalog build pipeline."""
import json
import tempfile
from pathlib import Path

import pytest

from osco.catalog.builder import (
    build_catalog,
    catalog_stats,
    load_source,
    write_catalog,
)
from osco.catalog.critical_capabilities import CRITICAL_CAPABILITIES
from osco.catalog.curated_mappings import CURATED_MAPPINGS, CURATED_DESCRIPTIONS


class TestBuildCatalog:
    """Test the catalog build pipeline."""

    def _sample_source(self) -> list[dict]:
        return [
            {
                "capability_id": "powershell.command.execute",
                "stable_id": "OSCO-CAP-0001",
                "name": "Execute PowerShell Command",
                "description": "Perform execute operation on command in the powershell domain.",
                "category": "execution",
                "domain": "powershell",
                "platforms": ["windows"],
                "providers": ["provider.windows"],
                "mappings": [
                    {"framework": "sigma", "external_id": "sigma-9999", "external_name": "Fake", "relation": "maps_to", "confidence": 0.72},
                ],
            },
            {
                "capability_id": "filesystem.file.create",
                "stable_id": "OSCO-CAP-0002",
                "name": "Create File",
                "description": "Create a file object at a target path.",
                "category": "execution",
                "domain": "filesystem",
                "platforms": ["windows"],
                "providers": ["provider.windows"],
                "mappings": [
                    {"framework": "mitre_attack", "external_id": "T1105", "external_name": "Ingress Tool Transfer", "relation": "maps_to", "confidence": 0.95},
                ],
            },
        ]

    def test_strips_fake_mappings(self) -> None:
        source = self._sample_source()
        result = build_catalog(source, add_critical_capabilities=False)

        ps = next(c for c in result if c["capability_id"] == "powershell.command.execute")
        # Fake sigma-9999 should be stripped, but real ATT&CK from CURATED_MAPPINGS added
        for m in ps["mappings"]:
            assert not m["external_id"].startswith("sigma-") or m["external_id"] == "win_susp_powershell_encode"

    def test_preserves_real_mappings(self) -> None:
        source = self._sample_source()
        result = build_catalog(source, add_critical_capabilities=False)

        fs = next(c for c in result if c["capability_id"] == "filesystem.file.create")
        assert any(m["external_id"] == "T1105" for m in fs["mappings"])

    def test_injects_curated_mappings(self) -> None:
        source = self._sample_source()
        result = build_catalog(source, add_critical_capabilities=False)

        ps = next(c for c in result if c["capability_id"] == "powershell.command.execute")
        mapping_ids = [m["external_id"] for m in ps["mappings"]]
        assert "T1059.001" in mapping_ids

    def test_updates_description(self) -> None:
        source = self._sample_source()
        result = build_catalog(source, add_critical_capabilities=False)

        ps = next(c for c in result if c["capability_id"] == "powershell.command.execute")
        assert "PowerShell" in ps["description"]
        assert "Perform execute operation" not in ps["description"]

    def test_adds_critical_capabilities(self) -> None:
        source = self._sample_source()
        result = build_catalog(source, add_critical_capabilities=True)

        result_ids = {c["capability_id"] for c in result}
        for cap in CRITICAL_CAPABILITIES:
            assert cap["capability_id"] in result_ids

    def test_no_duplicate_critical_capabilities(self) -> None:
        # If a critical cap is already in source, it should not be duplicated
        source = self._sample_source() + [dict(CRITICAL_CAPABILITIES[0])]
        result = build_catalog(source, add_critical_capabilities=True)

        target_id = CRITICAL_CAPABILITIES[0]["capability_id"]
        matches = [c for c in result if c["capability_id"] == target_id]
        assert len(matches) == 1

    def test_dry_run_no_strip(self) -> None:
        source = self._sample_source()
        result = build_catalog(source, add_critical_capabilities=False, strip_fake_mappings=False)

        ps = next(c for c in result if c["capability_id"] == "powershell.command.execute")
        # Fake mapping should still be present when strip is disabled
        # (curated ones get merged in, but fake ones are not stripped)
        fake = [m for m in ps["mappings"] if m["external_id"] == "sigma-9999"]
        assert len(fake) == 1


class TestLoadWriteCatalog:
    """Test catalog I/O utilities."""

    def test_load_source(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "catalog.json"
            data = [{"capability_id": "test.cap", "name": "Test"}]
            path.write_text(json.dumps(data))

            loaded = load_source(path)
            assert loaded == data

    def test_load_source_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "catalog.json"
            path.write_text(json.dumps({"not": "a list"}))

            with pytest.raises(ValueError, match="Expected a JSON list"):
                load_source(path)

    def test_write_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "out.json"
            data = [{"capability_id": "test.cap"}]

            write_catalog(data, path)
            assert path.exists()
            loaded = json.loads(path.read_text())
            assert loaded == data

    def test_write_creates_parent_dirs(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "nested" / "dir" / "catalog.json"
            write_catalog([], path)
            assert path.exists()


class TestCatalogStats:
    """Test catalog statistics."""

    def test_stats_empty(self) -> None:
        stats = catalog_stats([])
        assert stats["total"] == 0
        assert stats["with_mappings"] == 0
        assert stats["without_mappings"] == 0
        assert stats["total_mapping_references"] == 0

    def test_stats_mixed(self) -> None:
        catalog = [
            {"capability_id": "a", "mappings": [{"framework": "mitre_attack", "external_id": "T1234"}]},
            {"capability_id": "b", "mappings": []},
            {"capability_id": "c", "mappings": [{"framework": "sigma", "external_id": "rule1"}, {"framework": "mitre_attack", "external_id": "T1235"}]},
        ]
        stats = catalog_stats(catalog)
        assert stats["total"] == 3
        assert stats["with_mappings"] == 2
        assert stats["without_mappings"] == 1
        assert stats["total_mapping_references"] == 3


class TestCuratedData:
    """Validate the curated knowledge base itself."""

    def test_curated_mappings_have_required_fields(self) -> None:
        for cid, mappings in CURATED_MAPPINGS.items():
            for m in mappings:
                assert "framework" in m, f"{cid}: missing framework"
                assert "external_id" in m, f"{cid}: missing external_id"
                assert "external_name" in m, f"{cid}: missing external_name"
                assert "confidence" in m, f"{cid}: missing confidence"
                assert 0.0 <= m["confidence"] <= 1.0, f"{cid}: confidence out of range"

    def test_curated_mappings_no_fake_ids(self) -> None:
        import re
        fake_pattern = re.compile(r"^[a-z_]+-\d{3,6}$")
        for cid, mappings in CURATED_MAPPINGS.items():
            for m in mappings:
                assert not fake_pattern.match(m["external_id"]), (
                    f"{cid}: external_id '{m['external_id']}' looks fake"
                )

    def test_critical_capabilities_have_required_fields(self) -> None:
        for cap in CRITICAL_CAPABILITIES:
            assert "capability_id" in cap
            assert "stable_id" in cap
            assert "name" in cap
            assert "description" in cap
            assert "mappings" in cap
            assert len(cap["mappings"]) > 0, f"{cap['capability_id']}: no mappings"

    def test_critical_capabilities_no_fake_ids(self) -> None:
        import re
        fake_pattern = re.compile(r"^[a-z_]+-\d{3,6}$")
        for cap in CRITICAL_CAPABILITIES:
            for m in cap.get("mappings", []):
                assert not fake_pattern.match(m["external_id"]), (
                    f"{cap['capability_id']}: fake mapping ID '{m['external_id']}'"
                )

    def test_critical_capabilities_stable_ids_unique(self) -> None:
        stable_ids = [c["stable_id"] for c in CRITICAL_CAPABILITIES]
        assert len(stable_ids) == len(set(stable_ids)), "Duplicate stable_ids in CRITICAL_CAPABILITIES"

    def test_critical_capabilities_ids_unique(self) -> None:
        ids = [c["capability_id"] for c in CRITICAL_CAPABILITIES]
        assert len(ids) == len(set(ids)), "Duplicate capability_ids in CRITICAL_CAPABILITIES"
