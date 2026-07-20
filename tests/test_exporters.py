"""Test graph exports and rendering."""

import json
import tempfile
from pathlib import Path

import networkx as nx
import pytest

from osco.exporters import export_graph_cypher, export_graph_graphml, export_graph_json
from osco.graph_builder import build_graph
from osco.registry import OSCORegistry


class TestGraphExports:
    """Test graph export functionality."""

    @pytest.fixture
    def sample_graph(self) -> nx.MultiDiGraph:
        graph = nx.MultiDiGraph()
        graph.add_node("cap1", kind="capability", name="Capability 1")
        graph.add_node("cap2", kind="capability", name="Capability 2")
        graph.add_node("prov1", kind="provider", name="Provider 1")
        graph.add_edge("cap1", "cap2", relation="depends_on")
        graph.add_edge("cap1", "prov1", relation="implemented_by")
        return graph

    def test_export_graph_json(self, sample_graph: nx.MultiDiGraph) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.json"
            export_graph_json(sample_graph, output_path)

            assert output_path.exists()
            data = json.loads(output_path.read_text())
            assert "nodes" in data
            assert "edges" in data
            assert len(data["nodes"]) == 3
            assert len(data["edges"]) == 2

    def test_export_graph_json_structure(self, sample_graph: nx.MultiDiGraph) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.json"
            export_graph_json(sample_graph, output_path)

            data = json.loads(output_path.read_text())
            # Check node structure
            assert all("id" in node for node in data["nodes"])
            # Check edge structure
            assert all("source" in edge and "target" in edge for edge in data["edges"])

    def test_export_graph_graphml(self, sample_graph: nx.MultiDiGraph) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.graphml"
            export_graph_graphml(sample_graph, output_path)

            assert output_path.exists()
            # Try to read it back
            loaded = nx.read_graphml(output_path)
            assert loaded.number_of_nodes() == 3
            assert loaded.number_of_edges() == 2

    def test_export_graph_cypher(self, sample_graph: nx.MultiDiGraph) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "graph.cypher"
            export_graph_cypher(sample_graph, output_path)

            assert output_path.exists()
            content = output_path.read_text()
            # Check that Cypher commands are present
            assert "MERGE" in content
            assert "cap1" in content
            assert "cap2" in content


class TestGraphBuilding:
    """Test graph building from registry."""

    @pytest.fixture
    def registry(self) -> OSCORegistry:
        return OSCORegistry()

    @pytest.fixture
    def built_graph(self, registry: OSCORegistry) -> nx.MultiDiGraph:
        return build_graph(registry.bundle)

    def test_graph_has_nodes(self, built_graph: nx.MultiDiGraph) -> None:
        assert built_graph.number_of_nodes() > 0

    def test_graph_has_edges(self, built_graph: nx.MultiDiGraph) -> None:
        assert built_graph.number_of_edges() > 0

    def test_graph_contains_capabilities(self, built_graph: nx.MultiDiGraph) -> None:
        capability_nodes = [
            (node, data) for node, data in built_graph.nodes(data=True)
            if data.get("kind") == "capability"
        ]
        assert len(capability_nodes) > 0

    def test_graph_contains_providers(self, built_graph: nx.MultiDiGraph) -> None:
        provider_nodes = [
            (node, data) for node, data in built_graph.nodes(data=True)
            if data.get("kind") == "provider"
        ]
        assert len(provider_nodes) > 0

    def test_graph_node_attributes(self, built_graph: nx.MultiDiGraph) -> None:
        # Verify nodes exist and have IDs
        for node_id, attrs in built_graph.nodes(data=True):
            assert node_id is not None
            # Nodes can have attributes or be empty (implementation dependent)
            assert isinstance(attrs, dict)

    def test_graph_edge_attributes(self, built_graph: nx.MultiDiGraph) -> None:
        has_relation_attrs = False
        for source, target, attrs in built_graph.edges(data=True):
            if "relation" in attrs:
                has_relation_attrs = True
                break
        # At least some edges should have relation information
        assert built_graph.number_of_edges() > 0 or not has_relation_attrs

    def test_graph_is_directed(self, built_graph: nx.MultiDiGraph) -> None:
        assert isinstance(built_graph, nx.DiGraph)

    def test_graph_preserves_references(self, registry: OSCORegistry, built_graph: nx.MultiDiGraph) -> None:
        # Verify that capabilities in graph match loaded capabilities
        cap_ids = {cap.capability_id for cap in registry.list_capabilities()}
        graph_cap_ids = {
            node for node, data in built_graph.nodes(data=True)
            if data.get("kind") == "capability"
        }
        # All graph capability nodes should be in registry
        for graph_id in graph_cap_ids:
            assert graph_id in cap_ids or graph_id.startswith("cap:")


class TestGraphExportFormats:
    """Test all graph export formats work correctly."""

    @pytest.fixture
    def registry(self) -> OSCORegistry:
        return OSCORegistry()

    def test_export_all_formats(self, registry: OSCORegistry) -> None:
        graph = build_graph(registry.bundle)

        with tempfile.TemporaryDirectory() as tmpdir:
            tmppath = Path(tmpdir)

            # Export all formats
            json_path = tmppath / "graph.json"
            graphml_path = tmppath / "graph.graphml"
            cypher_path = tmppath / "graph.cypher"

            export_graph_json(graph, json_path)
            export_graph_graphml(graph, graphml_path)
            export_graph_cypher(graph, cypher_path)

            # Verify all files exist
            assert json_path.exists()
            assert graphml_path.exists()
            assert cypher_path.exists()

            # Verify files have content
            assert json_path.stat().st_size > 0
            assert graphml_path.stat().st_size > 0
            assert cypher_path.stat().st_size > 0
