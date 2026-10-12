"""Build the public JSON file containing anonymous page analytics."""

from collections.abc import Callable
from datetime import UTC, date, datetime
import json
import os
from pathlib import Path
from typing import TypedDict

from pro_analytics_02.view_analytics.base_academic_blocks import (
    get_display_block,
    get_estimated_students,
    get_today,
    load_blocks,
)
from pro_analytics_02.view_analytics.base_ga4_client import (
    PageMetrics,
    fetch_page_analytics,
)

PROJECT_ROOT = Path(__file__).resolve().parents[3]
ACADEMIC_BLOCKS_PATH = PROJECT_ROOT / "data" / "academic_blocks.toml"
ENROLLMENT_ESTIMATES_PATH = PROJECT_ROOT / "data" / "enrollment_estimates.toml"
OUTPUT_PATH = PROJECT_ROOT / "docs" / "assets" / "data" / "view-analytics.json"
SITE_PATH_PREFIX = "/pro-analytics-02/"
ACADEMIC_TIMEZONE = "America/Chicago"

type PageAnalyticsFetcher = Callable[
    [str, date, date, str],
    dict[str, PageMetrics],
]


class AnalyticsDocument(TypedDict):
    """Public, anonymous analytics generated for one academic block."""

    block_id: str
    period_start: str
    period_end: str
    estimated_students: int
    generated_at: str
    pages: dict[str, PageMetrics]


def build_analytics_document(
    property_id: str,
    academic_blocks_path: str | Path,
    enrollment_estimates_path: str | Path,
    today: date,
    generated_at: datetime,
    path_prefix: str = SITE_PATH_PREFIX,
    fetch_page_metrics: PageAnalyticsFetcher = fetch_page_analytics,
) -> AnalyticsDocument:
    """Collect the current block and its page-level GA4 metrics."""
    blocks = load_blocks(academic_blocks_path)

    # WHY: Views during a break still count toward the most recent block.
    # OBS: The block stays in effect until the next block starts.
    block = get_display_block(blocks, today)
    estimated_students = get_estimated_students(
        block.id,
        enrollment_estimates_path,
    )
    pages = fetch_page_metrics(
        property_id,
        block.start,
        today,
        path_prefix,
    )

    return AnalyticsDocument(
        block_id=block.id,
        period_start=block.start.isoformat(),
        period_end=today.isoformat(),
        estimated_students=estimated_students,
        generated_at=_format_utc(generated_at),
        pages=pages,
    )


def write_analytics_json(
    document: AnalyticsDocument,
    output_path: str | Path,
) -> None:
    """Write the analytics document as deterministic, formatted JSON."""
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(document, indent=2) + "\n"
    destination.write_text(content, encoding="utf-8")


def main() -> None:
    """Build guide analytics for the current or most recent academic block."""
    today = get_today(ACADEMIC_TIMEZONE)

    # WHY: During a break, keep reporting the most recent block.
    # OBS: Documentation deployment must continue even with no block started.
    try:
        get_display_block(load_blocks(ACADEMIC_BLOCKS_PATH), today)
    except LookupError:
        print(f"No academic block has started by {today}; skipping GA4 analytics.")
        return

    property_id = os.environ.get("GA4_PROPERTY_ID")
    if property_id is None:
        raise RuntimeError("GA4_PROPERTY_ID is required.")

    document = build_analytics_document(
        property_id=property_id,
        academic_blocks_path=ACADEMIC_BLOCKS_PATH,
        enrollment_estimates_path=ENROLLMENT_ESTIMATES_PATH,
        today=today,
        generated_at=datetime.now(UTC),
    )
    write_analytics_json(document, OUTPUT_PATH)


def _format_utc(timestamp: datetime) -> str:
    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise ValueError("generated_at must be timezone-aware.")
    return (
        timestamp.astimezone(UTC)
        .isoformat(timespec="seconds")
        .replace(
            "+00:00",
            "Z",
        )
    )


if __name__ == "__main__":
    main()
