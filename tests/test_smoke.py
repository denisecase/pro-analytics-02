"""Test that the project structure works correctly.

Module Information:
    - Filename: test_smoke.py
    - Module: test_smoke
    - Location: tests/

This smoke test verifies that:
    - All modules can be imported
    - Basic project structure is intact
"""

from analytics_project import main
from analytics_project import demo_module_basics
from analytics_project import utils_logger


def test_imports_work():
    """Verify all modules can be imported."""
    # If we get here without ImportError, imports work
    assert demo_module_basics is not None
    assert utils_logger is not None
    assert main is not None


def test_individual_demos_run():
    """Verify each demo module can run independently."""
    # Initialize logger once for all tests
    utils_logger.init_logger()

    # Each should run without exceptions
    demo_module_basics.demo_basics()
