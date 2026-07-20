from __future__ import annotations

import json
from pathlib import Path

import networkx as nx


def export_graph_json(graph: nx.MultiDiGraph, output: Path) -> None:
    payload = {
        "nodes": [
            {"id": node_id, **attrs}
            for node_id, attrs in graph.nodes(data=True)
        ],
        "edges": [
            {"source": source, "target": target, **attrs}
            for source, target, attrs in graph.edges(data=True)
        ],
    }
    output.write_text(json.dumps(payload, indent=2))


def export_graph_graphml(graph: nx.MultiDiGraph, output: Path) -> None:
    nx.write_graphml(graph, output)


def export_graph_cypher(graph: nx.MultiDiGraph, output: Path) -> None:
    lines: list[str] = []

    for node_id, attrs in graph.nodes(data=True):
        label = attrs.get("kind", "Node").capitalize()
        props = {"id": node_id, **attrs}
        prop_parts = []
        for key, value in props.items():
            if isinstance(value, str):
                escaped = value.replace("'", "\\'")
                prop_parts.append(f"{key}: '{escaped}'")
            else:
                prop_parts.append(f"{key}: {json.dumps(value)}")
        lines.append(f"MERGE (n:{label} {{id: '{node_id}'}}) SET n += {{{', '.join(prop_parts)}}};")

    for source, target, attrs in graph.edges(data=True):
        relation = attrs.get("relation", "related_to").upper()
        safe_relation = relation.replace("-", "_")
        lines.append(
            "MATCH (a {id: '"
            + source
            + "'}), (b {id: '"
            + target
            + "'}) MERGE (a)-[:"
            + safe_relation
            + "]->(b);"
        )

    output.write_text("\n".join(lines) + "\n")
