from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from osco.catalog.builder import build_catalog, catalog_stats, load_source, write_catalog
from osco.exporters import export_graph_cypher, export_graph_graphml, export_graph_json
from osco.graph_builder import build_graph
from osco.models.core import MappingFramework
from osco.registry import OSCORegistry

app = typer.Typer(help="OSCO command line interface")
capability_app = typer.Typer(help="Capability operations")
catalog_app = typer.Typer(help="Catalog build operations")
provider_app = typer.Typer(help="Provider operations")
mapping_app = typer.Typer(help="Mapping operations")
graph_app = typer.Typer(help="Graph operations")
schema_app = typer.Typer(help="Schema operations")

app.add_typer(capability_app, name="capability")
app.add_typer(catalog_app, name="catalog")
app.add_typer(provider_app, name="provider")
app.add_typer(mapping_app, name="mapping")
app.add_typer(graph_app, name="graph")
app.add_typer(schema_app, name="schema")

console = Console()

ROOT = Path(__file__).resolve().parents[2]


@catalog_app.command("build")
def catalog_build(
    source: Path = typer.Option(
        None,
        help="Source catalog JSON to build from. Defaults to capability/catalog.extended.json.",
    ),
    output: Path = typer.Option(
        None,
        help="Output path. Defaults to capability/catalog.json.",
    ),
    dry_run: bool = typer.Option(False, "--dry-run", help="Print stats without writing."),
    no_critical: bool = typer.Option(False, "--no-critical", help="Skip adding critical capabilities."),
    no_strip: bool = typer.Option(False, "--no-strip", help="Keep fake placeholder mapping IDs."),
) -> None:
    """Build the gold capability catalog from the extended corpus."""
    source_path = source or ROOT / "capability" / "catalog.extended.json"
    output_path = output or ROOT / "capability" / "catalog.json"

    raw = load_source(source_path)
    curated = build_catalog(
        raw,
        add_critical_capabilities=not no_critical,
        strip_fake_mappings=not no_strip,
    )

    stats = catalog_stats(curated)
    console.print(f"Source:           {source_path} ({len(raw)} capabilities)")
    console.print(f"Output:           {output_path}")
    console.print(f"Total:            {stats['total']} capabilities")
    console.print(f"With mappings:    {stats['with_mappings']}")
    console.print(f"Without mappings: {stats['without_mappings']}")
    console.print(f"Total references: {stats['total_mapping_references']}")

    if not dry_run:
        write_catalog(curated, output_path)
        console.print(f"\n[green]Wrote {output_path}[/green]")
    else:
        console.print("\n[yellow][dry-run] No files written.[/yellow]")


@catalog_app.command("stats")
def catalog_stats_cmd(
    catalog: Path = typer.Option(None, help="Catalog JSON path. Defaults to capability/catalog.json."),
) -> None:
    """Show mapping coverage statistics for a catalog."""
    catalog_path = catalog or ROOT / "capability" / "catalog.json"
    caps = load_source(catalog_path)
    stats = catalog_stats(caps)

    table = Table(title=f"Catalog Stats: {catalog_path.name}")
    table.add_column("Metric")
    table.add_column("Value")
    table.add_row("Total capabilities", str(stats["total"]))
    table.add_row("With mappings", str(stats["with_mappings"]))
    table.add_row("Without mappings", str(stats["without_mappings"]))
    table.add_row("Total mapping references", str(stats["total_mapping_references"]))
    console.print(table)

    # Framework breakdown
    frameworks: dict[str, int] = {}
    for cap in caps:
        for m in cap.get("mappings", []):
            fw = m.get("framework", "unknown")
            frameworks[fw] = frameworks.get(fw, 0) + 1

    if frameworks:
        fw_table = Table(title="Mappings by Framework")
        fw_table.add_column("Framework")
        fw_table.add_column("References")
        for fw, count in sorted(frameworks.items(), key=lambda x: -x[1]):
            fw_table.add_row(fw, str(count))
        console.print(fw_table)



def capability_search(query: str) -> None:
    registry = OSCORegistry()
    rows = registry.search_capabilities(query)
    table = Table(title=f"Capabilities matching: {query}")
    table.add_column("Capability ID")
    table.add_column("Name")
    table.add_column("Domain")
    table.add_column("Safety")
    for item in rows:
        table.add_row(item.capability_id, item.name, item.domain, item.safety.value)
    console.print(table)


@capability_app.command("list")
def capability_list() -> None:
    registry = OSCORegistry()
    table = Table(title="All Capabilities")
    table.add_column("Stable ID")
    table.add_column("Capability ID")
    table.add_column("Category")
    for item in registry.list_capabilities():
        table.add_row(item.stable_id, item.capability_id, item.category)
    console.print(table)


@provider_app.command("list")
def provider_list() -> None:
    registry = OSCORegistry()
    table = Table(title="Providers")
    table.add_column("Provider ID")
    table.add_column("Name")
    table.add_column("Category")
    for provider in registry.list_providers():
        table.add_row(provider.provider_id, provider.name, provider.category)
    console.print(table)


@mapping_app.command("list")
def mapping_list(framework: MappingFramework | None = None) -> None:
    registry = OSCORegistry()
    table = Table(title="Capability Mappings")
    table.add_column("Capability")
    table.add_column("Framework")
    table.add_column("External ID")
    table.add_column("Relation")

    for capability in registry.list_capabilities():
        for mapping in capability.mappings:
            if framework is not None and mapping.framework != framework:
                continue
            table.add_row(
                capability.capability_id,
                mapping.framework.value,
                mapping.external_id,
                mapping.relation,
            )

    console.print(table)


@mapping_app.command("unmapped")
def mapping_unmapped() -> None:
    registry = OSCORegistry()
    unmapped = [cap for cap in registry.list_capabilities() if not cap.mappings]
    if not unmapped:
        console.print("All capabilities have at least one mapping.")
        return
    for item in unmapped:
        console.print(item.capability_id)


@graph_app.command("export")
def graph_export(
    output: Path = typer.Option(..., help="Path to graph output file"),
    format: str = typer.Option("json", help="json, graphml, or cypher"),
) -> None:
    registry = OSCORegistry()
    graph = build_graph(registry.bundle)
    output.parent.mkdir(parents=True, exist_ok=True)
    if format == "json":
        export_graph_json(graph, output)
    elif format == "graphml":
        export_graph_graphml(graph, output)
    elif format == "cypher":
        export_graph_cypher(graph, output)
    else:
        raise typer.BadParameter("format must be one of: json, graphml, cypher")
    console.print(f"Graph exported to {output}")


@graph_app.command("relationships")
def graph_relationships(capability_id: str) -> None:
    registry = OSCORegistry()
    graph = build_graph(registry.bundle)

    if capability_id not in graph.nodes:
        raise typer.BadParameter("Unknown capability id")

    table = Table(title=f"Relationships for {capability_id}")
    table.add_column("Direction")
    table.add_column("Relation")
    table.add_column("Node")

    for source, target, attrs in graph.in_edges(capability_id, data=True):
        table.add_row("in", attrs.get("relation", "related_to"), source)
    for source, target, attrs in graph.out_edges(capability_id, data=True):
        table.add_row("out", attrs.get("relation", "related_to"), target)

    console.print(table)


@schema_app.command("validate")
def schema_validate() -> None:
    from jsonschema import validate

    registry = OSCORegistry()
    schema_path = Path("jsonschema/capability.schema.json")
    schema = json.loads(schema_path.read_text())

    for capability in registry.list_capabilities():
        validate(instance=capability.model_dump(mode="json"), schema=schema)

    console.print("Capability schema validation successful.")


@mapping_app.command("compare")
def mapping_compare(framework_a: MappingFramework, framework_b: MappingFramework) -> None:
    registry = OSCORegistry()
    a_set = set()
    b_set = set()

    for capability in registry.list_capabilities():
        for mapping in capability.mappings:
            if mapping.framework == framework_a:
                a_set.add(capability.capability_id)
            if mapping.framework == framework_b:
                b_set.add(capability.capability_id)

    only_a = sorted(a_set - b_set)
    only_b = sorted(b_set - a_set)
    overlap = sorted(a_set & b_set)

    console.print(f"Only in {framework_a.value}: {len(only_a)}")
    console.print(f"Only in {framework_b.value}: {len(only_b)}")
    console.print(f"Overlap: {len(overlap)}")


@mapping_app.command("convert")
def mapping_convert(framework: MappingFramework, external_id: str) -> None:
    registry = OSCORegistry()
    table = Table(title=f"OSCO capabilities for {framework.value}:{external_id}")
    table.add_column("Capability")
    table.add_column("Name")
    table.add_column("Confidence")

    found = False
    for capability in registry.list_capabilities():
        for mapping in capability.mappings:
            if mapping.framework == framework and mapping.external_id == external_id:
                table.add_row(capability.capability_id, capability.name, str(mapping.confidence))
                found = True

    if not found:
        console.print("No mapped capabilities found for that framework identifier.")
        return

    console.print(table)


if __name__ == "__main__":
    app()
