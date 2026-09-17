"""Tests for academic-block and enrollment configuration."""

from datetime import date
from pathlib import Path

import pytest

from pro_analytics_02.view_analytics.base_academic_blocks import (
    AcademicBlock,
    get_current_block,
    get_estimated_students,
    get_today,
    load_blocks,
)


def write_toml(path: Path, content: str) -> Path:
    """Write a TOML fixture and return its path."""
    path.write_text(content, encoding="utf-8")
    return path


def test_get_today_returns_a_date_for_timezone() -> None:
    today = get_today("America/Chicago")

    assert isinstance(today, date)


def test_load_blocks_sorts_by_start_date(tmp_path: Path) -> None:
    path = write_toml(
        tmp_path / "academic_blocks.toml",
        """
[[blocks]]
id = "2026-fall-2"
start = 2026-10-19
end = 2026-12-06

[[blocks]]
id = "2026-fall-1"
start = 2026-08-24
end = 2026-10-11
""",
    )

    blocks = load_blocks(path)

    assert blocks == [
        AcademicBlock(
            id="2026-fall-1",
            start=date(2026, 8, 24),
            end=date(2026, 10, 11),
        ),
        AcademicBlock(
            id="2026-fall-2",
            start=date(2026, 10, 19),
            end=date(2026, 12, 6),
        ),
    ]


@pytest.mark.parametrize("today", [date(2026, 8, 24), date(2026, 10, 11)])
def test_get_current_block_includes_boundary_dates(today: date) -> None:
    block = AcademicBlock(
        id="2026-fall-1",
        start=date(2026, 8, 24),
        end=date(2026, 10, 11),
    )

    assert get_current_block([block], today) == block


def test_get_current_block_raises_when_no_block_is_active() -> None:
    block = AcademicBlock(
        id="2026-fall-1",
        start=date(2026, 8, 24),
        end=date(2026, 10, 11),
    )

    with pytest.raises(LookupError, match="No academic block contains"):
        get_current_block([block], date(2026, 10, 12))


def test_load_blocks_rejects_overlapping_blocks(tmp_path: Path) -> None:
    path = write_toml(
        tmp_path / "academic_blocks.toml",
        """
[[blocks]]
id = "first"
start = 2026-08-24
end = 2026-10-11

[[blocks]]
id = "second"
start = 2026-10-11
end = 2026-12-06
""",
    )

    with pytest.raises(ValueError, match="overlap"):
        load_blocks(path)


def test_get_estimated_students_uses_block_override(tmp_path: Path) -> None:
    path = write_toml(
        tmp_path / "enrollment_estimates.toml",
        """
default_students = 40

[blocks]
2026-fall-1 = 46
""",
    )

    assert get_estimated_students("2026-fall-1", path) == 46


def test_get_estimated_students_uses_default(tmp_path: Path) -> None:
    path = write_toml(
        tmp_path / "enrollment_estimates.toml",
        """
default_students = 40

[blocks]
2026-fall-1 = 46
""",
    )

    assert get_estimated_students("2026-fall-2", path) == 40


def test_get_estimated_students_requires_an_available_estimate(
    tmp_path: Path,
) -> None:
    path = write_toml(tmp_path / "enrollment_estimates.toml", "[blocks]\n")

    with pytest.raises(KeyError, match="No enrollment estimate exists"):
        get_estimated_students("2026-fall-1", path)
