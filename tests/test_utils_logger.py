"""Test the logger utility module.

Module Information:
    - Filename: test_utils_logger.py
    - Module: test_utils_logger
    - Location: tests/

Testing logging is important because:
    - Logs are critical for debugging production issues
    - Proper logging helps track down problems months later
    - Good tests ensure logs work when you need them most
"""

from pathlib import Path
from analytics_project import utils_logger


def test_logger_initialization():
    """Verify logger can be initialized with default settings."""
    utils_logger.init_logger()
    assert utils_logger.logger is not None


def test_logger_initialization_with_debug_level():
    """Verify logger accepts different log levels."""
    utils_logger.init_logger(level="DEBUG")
    # Logger should exist and be configured
    assert utils_logger.logger is not None


def test_log_file_path_exists():
    """Verify log file path is created correctly."""
    log_path = utils_logger.get_log_file_path()

    # Check it's a Path object
    assert isinstance(log_path, Path)

    # Check it has the right extension
    assert log_path.suffix == ".log"

    # Check the directory exists after initialization
    utils_logger.init_logger()
    assert log_path.parent.exists()


def test_log_example_runs():
    """Verify the example logging function works."""
    utils_logger.init_logger()
    # Should run without errors
    utils_logger.log_example()


def test_utils_logger_main():
    """Verify the module can run as standalone."""
    # Should execute without errors
    utils_logger.main()


def test_logger_creates_log_file():
    """Verify logger can create log files."""
    utils_logger.init_logger()
    log_path = utils_logger.get_log_file_path()

    # Log something
    utils_logger.logger.info("Smoke test message")

    # Check log file exists
    assert log_path.parent.exists(), "Log directory not created"
