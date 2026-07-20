from __future__ import annotations

import networkx as nx

from osco.models.core import Capability, OSCOBundle


def build_graph(bundle: OSCOBundle) -> nx.MultiDiGraph:
    graph = nx.MultiDiGraph()

    for provider in bundle.providers:
        graph.add_node(provider.provider_id, kind="provider", name=provider.name)

    for capability in bundle.capabilities:
        _add_capability_node(graph, capability)
        for provider_id in capability.providers:
            graph.add_edge(provider_id, capability.capability_id, relation="implements")
        for child_id in capability.child_capabilities:
            graph.add_edge(capability.capability_id, child_id, relation="enables")
        for related_id in capability.related_capabilities:
            graph.add_edge(capability.capability_id, related_id, relation="related_to")
        for mapping in capability.mappings:
            mapping_node = f"mapping::{mapping.framework.value}::{mapping.external_id}"
            graph.add_node(
                mapping_node,
                kind="mapping",
                framework=mapping.framework.value,
                external_id=mapping.external_id,
                external_name=mapping.external_name,
            )
            graph.add_edge(capability.capability_id, mapping_node, relation=mapping.relation)

    return graph


def _add_capability_node(graph: nx.MultiDiGraph, capability: Capability) -> None:
    graph.add_node(
        capability.capability_id,
        kind="capability",
        name=capability.name,
        domain=capability.domain,
        category=capability.category,
        safety=capability.safety.value,
        confidence=capability.confidence,
    )
