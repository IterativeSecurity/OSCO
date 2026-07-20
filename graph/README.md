# Graph

This component contains graph-oriented artifacts and interfaces for OSCO.

## Purpose

OSCO represents capabilities and their relationships as a graph so users can:

- query relationship context (`implements`, `maps_to`, `detects`, `validates`, `related_to`)
- export graph views for integration and analysis
- reason across capability, provider, detection, and validation objects

## Current Implementation

Graph construction and export logic is implemented in:

- [osco/graph_builder.py](../osco/graph_builder.py)
- [osco/exporters.py](../osco/exporters.py)

Sample graph outputs are available in:

- [examples/osco_graph.json](../examples/osco_graph.json)
- [examples/osco_graph.cypher](../examples/osco_graph.cypher)

## Status

This folder is currently documentation-only. Runtime code lives in the Python package
under [osco/](../osco/).
