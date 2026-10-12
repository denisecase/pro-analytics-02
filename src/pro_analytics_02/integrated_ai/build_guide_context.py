# ============================================================
# src/pro_analytics_02/integrated_ai/build_guide_context.py
# ============================================================
# WHAT: Build documentation context for the guide assistant.
# WHY: Make guide content available to the browser as static JSON.
#
# Run from the repository root:
#   uv run python -m pro_analytics_02.integrated_ai.build_guide_context

"""Build the guide assistant's documentation context."""

import json
from pathlib import Path
import re
import tomllib
from typing import Any, TypedDict


class GuidePage(TypedDict):
    """Documentation page available to the assistant."""

    path: str
    section: str
    title: str
    content: str


class GuideContext(TypedDict):
    """Collection of documentation pages."""

    pages: list[GuidePage]


def remove_front_matter(content: str) -> str:
    """Remove leading YAML front matter from Markdown."""
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        return content.strip()

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() in {"---", "..."}:
            return "\n".join(lines[index + 1 :]).strip()

    return content.strip()


def get_page_title(content: str, source_path: Path) -> str:
    """Read the first level-one heading, with a filename fallback."""
    match = re.search(r"^#\s+(.+?)\s*#*\s*$", content, flags=re.MULTILINE)

    if match:
        return match.group(1).strip()

    if source_path.stem.lower() == "index":
        return source_path.parent.name.replace("-", " ").replace("_", " ")

    return source_path.stem.replace("-", " ").replace("_", " ")


def find_nav(config: Any) -> Any:
    """Find the first `nav` entry anywhere in the parsed zensical.toml."""
    if isinstance(config, dict):
        if "nav" in config:
            return config["nav"]
        for value in config.values():
            found = find_nav(value)
            if found is not None:
                return found
    return None


def collect_nav_paths(nav: Any) -> set[str]:
    """Collect every Markdown path listed in a nested nav structure."""
    if isinstance(nav, str):
        return {nav}
    if isinstance(nav, list):
        return set().union(*(collect_nav_paths(item) for item in nav))
    if isinstance(nav, dict):
        return set().union(*(collect_nav_paths(item) for item in nav.values()))
    return set()


def load_nav_paths(config_path: Path) -> set[str]:
    """Return the Markdown paths in the site nav, or an empty set if none."""
    if not config_path.is_file():
        return set()
    config = tomllib.loads(config_path.read_text(encoding="utf-8"))
    return collect_nav_paths(find_nav(config))


def get_section(relative_path: Path) -> str:
    """Use the top-level docs folder as the section (for example, workflow-c-...)."""
    return relative_path.parts[0] if len(relative_path.parts) > 1 else "home"


def build_guide_context(
    docs_dir: Path, nav_paths: set[str] | None = None
) -> GuideContext:
    """Collect Markdown pages with paths relative to the docs directory.

    When nav_paths is given, only pages listed in the site nav are included.
    """
    if not docs_dir.is_dir():
        raise FileNotFoundError(f"Documentation directory not found: {docs_dir}")

    pages: list[GuidePage] = []

    sources = sorted(
        (
            path
            for path in docs_dir.rglob("*")
            if path.is_file() and path.suffix.lower() == ".md"
        ),
        key=lambda path: path.relative_to(docs_dir).as_posix(),
    )

    for source_path in sources:
        relative_path = source_path.relative_to(docs_dir)

        if any(part.startswith(".") for part in relative_path.parts):
            continue

        if any(part.startswith(".") for part in relative_path.parts):
            continue

        if nav_paths and relative_path.as_posix() not in nav_paths:
            continue

        content = remove_front_matter(source_path.read_text(encoding="utf-8-sig"))

        if not content:
            continue

        pages.append(
            {
                "path": relative_path.as_posix(),
                "section": get_section(relative_path),
                "title": get_page_title(content, source_path),
                "content": content,
            }
        )

    if not pages:
        raise ValueError(f"No nonempty Markdown pages found in: {docs_dir}")

    return {"pages": pages}


def write_guide_context(context: GuideContext, output_path: Path) -> None:
    """Write deterministic UTF-8 JSON without a build timestamp."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(context, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    """Build and save context using repository-relative locations."""
    repo_root = Path(__file__).resolve().parents[3]
    docs_dir = repo_root / "docs"
    output_path = docs_dir / "assets" / "data" / "guide-context.json"

    nav_paths = load_nav_paths(repo_root / "zensical.toml")
    context = build_guide_context(docs_dir, nav_paths)

    write_guide_context(context, output_path)

    print(
        f"Wrote {len(context['pages'])} pages to "
        f"{output_path.relative_to(repo_root).as_posix()}"
    )


if __name__ == "__main__":
    main()
