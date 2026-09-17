"""Load academic blocks and estimated enrollment from TOML files."""

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import date, datetime
from itertools import pairwise
from pathlib import Path
import tomllib
from zoneinfo import ZoneInfo


@dataclass(frozen=True, slots=True)
class AcademicBlock:
    """A named academic block with inclusive start and end dates."""

    id: str
    start: date
    end: date


def get_today(timezone: str) -> date:
    """Return today's date in the requested IANA time zone."""
    return datetime.now(ZoneInfo(timezone)).date()


def load_blocks(path: str | Path) -> list[AcademicBlock]:
    """Load, validate, and sort academic blocks from a TOML file."""
    data = _load_toml(path)
    raw_blocks = data.get("blocks")
    if not isinstance(raw_blocks, list):
        raise TypeError("The academic-block file must contain [[blocks]] entries.")

    blocks: list[AcademicBlock] = []
    block_ids: set[str] = set()

    for index, raw_block in enumerate(raw_blocks):
        if not isinstance(raw_block, dict):
            raise TypeError(f"blocks[{index}] must be a TOML table.")

        block_data: Mapping[object, object] = raw_block
        block_id = block_data.get("id")
        if not isinstance(block_id, str) or not block_id.strip():
            raise ValueError(f"blocks[{index}].id must be a nonempty string.")
        if block_id in block_ids:
            raise ValueError(f"Duplicate academic block id: {block_id!r}.")

        start = _require_date(block_data.get("start"), f"blocks[{index}].start")
        end = _require_date(block_data.get("end"), f"blocks[{index}].end")
        if start > end:
            raise ValueError(f"Academic block {block_id!r} starts after it ends.")

        blocks.append(AcademicBlock(id=block_id, start=start, end=end))
        block_ids.add(block_id)

    blocks.sort(key=lambda block: (block.start, block.end, block.id))
    _validate_no_overlaps(blocks)
    return blocks


def get_current_block(
    blocks: Iterable[AcademicBlock],
    today: date,
) -> AcademicBlock:
    """Return the single academic block containing today."""
    current_blocks = [block for block in blocks if block.start <= today <= block.end]

    if not current_blocks:
        raise LookupError(f"No academic block contains {today.isoformat()}.")
    if len(current_blocks) > 1:
        block_ids = ", ".join(block.id for block in current_blocks)
        raise ValueError(
            f"Multiple academic blocks contain {today.isoformat()}: {block_ids}."
        )

    return current_blocks[0]


def get_estimated_students(block_id: str, path: str | Path) -> int:
    """Return a block override or the default estimated-student count."""
    data = _load_toml(path)
    raw_overrides = data.get("blocks", {})
    if not isinstance(raw_overrides, dict):
        raise TypeError("The enrollment file's [blocks] value must be a TOML table.")

    overrides: Mapping[object, object] = raw_overrides
    if block_id in overrides:
        return _require_positive_int(overrides[block_id], f"blocks.{block_id}")

    if "default_students" not in data:
        raise KeyError(
            f"No enrollment estimate exists for {block_id!r}, and default_students "
            "is not configured."
        )

    return _require_positive_int(data["default_students"], "default_students")


def _load_toml(path: str | Path) -> dict[str, object]:
    with Path(path).open("rb") as file:
        return tomllib.load(file)


def _require_date(value: object, field_name: str) -> date:
    if not isinstance(value, date) or isinstance(value, datetime):
        raise TypeError(f"{field_name} must be a TOML local date in YYYY-MM-DD form.")
    return value


def _require_positive_int(value: object, field_name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(f"{field_name} must be a positive integer.")
    return value


def _validate_no_overlaps(blocks: list[AcademicBlock]) -> None:
    for previous, current in pairwise(blocks):
        if current.start <= previous.end:
            raise ValueError(
                f"Academic blocks {previous.id!r} and {current.id!r} overlap."
            )
