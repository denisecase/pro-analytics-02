"""Provide centralized logging for professional analytics projects.

This module configures project-wide logging to track events, debug issues,
and maintain audit trails during data analysis workflows.

Module Information:
    - Filename: utils_logger.py
    - Module: utils_logger
    - Location: src/analytics_project/

Key Concepts:
    - Centralized logging configuration
    - Log levels (DEBUG, INFO, WARNING, ERROR)
    - File-based log persistence
    - Colorized console output with Loguru

Professional Applications:
    - Production debugging and troubleshooting
    - Audit trails for regulatory compliance
    - Performance monitoring and optimization
    - Error tracking in data pipelines
"""

import pathlib
import sys

from loguru import logger

_is_configured: bool = False
_log_file_path: pathlib.Path | None = None


def _project_root(start: pathlib.Path | None = None) -> pathlib.Path:
    """Find the project root by walking up until we see a pyproject.toml or .git.

    Falls back to the directory containing this file.
    """
    here = (start or pathlib.Path(__file__)).resolve()
    for p in [here, *here.parents]:
        if (p / "pyproject.toml").exists() or (p / ".git").exists():
            return p
    return here.parent  # fallback


project_root = _project_root()


def get_log_file_path() -> pathlib.Path:
    """Return the path to the active log file, or default path if not initialized."""
    if _log_file_path is not None:
        return _log_file_path
    # Fallback: predictable location even before init_logger() runs
    return project_root / "project.log"


def init_logger(
    level: str = "INFO",
    *,
    log_dir: str | pathlib.Path = project_root,
    log_file_name: str = "project.log",
) -> pathlib.Path:
    """Initialize the logger and return the log file path.

    Ensures the log folder exists and configures logging to write to a file.

    Args:
        level (str): Logging level (e.g., "INFO", "DEBUG").
        log_dir: Directory where the log file will be written.
        log_file_name: File name for the log file.

    Returns:
        pathlib.Path: The resolved path to the log file.
    """
    global _is_configured
    if _is_configured:
        # If already configured once for this process
        return pathlib.Path(log_dir) / log_file_name

    # print a visual separator before logs
    print("-----------------------")

    # Resolve and ensure log folder exists
    log_folder = pathlib.Path(log_dir).expanduser().resolve()
    log_folder.mkdir(parents=True, exist_ok=True)

    # Build log file path
    log_file = log_folder / log_file_name

    try:
        fmt = "{time:YYYY-MM-DD HH:mm}:{level:<7} AT {file}:{line}: {message}"
        # Remove any existing Loguru handlers to avoid duplicate output
        logger.remove()
        logger.add(sys.stderr, level=level, format=fmt)
        logger.add(
            log_file,
            level=level,
            enqueue=True,
            backtrace=True,
            diagnose=False,
            rotation="10 MB",
            retention="7 days",
            encoding="utf-8",
            format=fmt,
        )
        logger.info(f"Logging to file: {log_file.resolve()}")
        _is_configured = True
        _log_file_path = log_file  # cache for retrieval
    except Exception as e:
        logger.error(f"Error configuring logger to write to file: {e}")

    return log_file


def log_example() -> None:
    """Demonstrate logging behavior with example messages."""
    logger.info("This is an example info message.")
    logger.warning("This is an example warning message.")
    logger.error("This is an example error message.")


def main() -> None:
    """Execute logger setup and demonstrate its usage."""
    log_file = init_logger()
    log_example()
    logger.info(f"View the log output at {log_file}")


if __name__ == "__main__":
    main()

__all__ = ["get_log_file_path", "init_logger", "log_example", "logger"]
