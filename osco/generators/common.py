"""Shared utilities for OSCO generators."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

GENERATED_WARNING = (
    "<!-- AUTO-GENERATED — do not edit manually. "
    "Regenerate with: {command} -->\n\n"
)


def write_generated_file(path: Path, content: str, command: str) -> None:
    """Write content to a file with an auto-generated header warning."""
    header = GENERATED_WARNING.format(command=command)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(header + content)
    print(f"✓ Written {path.relative_to(ROOT)}")
