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
from typing import TypedDict


class GuidePage(TypedDict):
    """Documentation page available to the assistant."""

    path: str
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


def build_guide_context(docs_dir: Path) -> GuideContext:
    """Collect Markdown pages with paths relative to the docs directory."""
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

        content = remove_front_matter(source_path.read_text(encoding="utf-8-sig"))

        if not content:
            continue

        pages.append(
            {
                "path": relative_path.as_posix(),
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

    context = build_guide_context(docs_dir)
    write_guide_context(context, output_path)

    print(
        f"Wrote {len(context['pages'])} pages to "
        f"{output_path.relative_to(repo_root).as_posix()}"
    )


if __name__ == "__main__":
    main()
