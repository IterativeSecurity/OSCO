from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_PARTS = {".git", ".pytest_cache", "__pycache__"}
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def should_skip(path: Path) -> bool:
    return any(part in EXCLUDED_PARTS for part in path.parts)


def normalize_target(target: str) -> str:
    normalized = target.strip()
    if normalized.startswith("<") and normalized.endswith(">"):
        normalized = normalized[1:-1]
    normalized = normalized.split("#", 1)[0]
    normalized = normalized.split("?", 1)[0]
    return normalized


def is_external_target(target: str) -> bool:
    prefixes = ("http://", "https://", "mailto:", "#")
    return target.startswith(prefixes)


def check_links() -> list[tuple[str, str]]:
    failures: list[tuple[str, str]] = []
    md_files = sorted(path for path in ROOT.rglob("*.md") if not should_skip(path))

    for md_file in md_files:
        text = md_file.read_text(errors="ignore")
        for match in LINK_PATTERN.finditer(text):
            raw_target = match.group(1).strip()
            if not raw_target:
                continue
            if is_external_target(raw_target):
                continue

            target = normalize_target(raw_target)
            if not target:
                continue

            resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                failures.append((str(md_file.relative_to(ROOT)), target))

    return failures


def main() -> None:
    failures = check_links()
    if failures:
        print(f"Broken markdown links detected: {len(failures)}")
        for source, target in failures:
            print(f"- {source} -> {target}")
        raise SystemExit(1)

    print("Markdown link check passed.")


if __name__ == "__main__":
    main()
