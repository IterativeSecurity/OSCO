from osco.graph_builder import build_graph
from osco.registry import OSCORegistry


def test_graph_contains_edges() -> None:
    registry = OSCORegistry()
    graph = build_graph(registry.bundle)
    assert graph.number_of_nodes() > 0
    assert graph.number_of_edges() > 0
