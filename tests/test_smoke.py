"""test_app.py - Tests for demo_module_basics.py.

REQ: Test pure functions that return values.

WHY: Pure functions are easy to test; ensures code works as expected.
"""

from pro_analytics_02 import demo_module_basics


def test_imports_work():
    """Test all modules can be imported."""
    # If we get here without ImportError, imports work
    assert demo_module_basics is not None


def test_individual_demos_run():
    """Test each demo module can run independently."""

    # Each should run without exceptions (errors)
    demo_module_basics.demo_basics()
