"""Demonstrate Python basics for professional analytics.

This module demonstrates fundamental Python concepts essential for data analysts,
including imports, variables, functions, and function calls.

Module Information:
    - Filename: demo_module_basics.py
    - Module: demo_module_basics
    - Location: src/pro_analytics_02/

Key Concepts:
    - Module imports and code organization
    - Variable declaration and scope
    - Function definition (reusable logic)
    - Function invocation and returns

Professional Applications:
    - Building maintainable analytics pipelines
    - Creating reusable analysis functions
    - Organizing code for team collaboration
    - Setting up logging for production debugging
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

# Python standard library
import logging  # only needed so we can type hint the logger variable

# External (must be listed in pyproject.toml)
# logging helps track program execution and is preferred over print statements
# We'll use a pre-configured logger that respects privacy.
from datafun_toolkit.logger import (
    get_logger,
    log_header,
)

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

# Call the get_logger() function, pass in a phrase and the logging level we want.
# The phrase helps identify the source of log messages.
# The level could be "DEBUG", "INFO", "WARNING", "ERROR", or "CRITICAL".
# Use DEBUG for development, INFO for production.
logger: logging.Logger = get_logger("P01", level="INFO")

# === Define Functions ===


def show_naming_and_comments() -> None:
    """Show Python naming and comments.

    Arguments: None - nothing is passed in via the parentheses.
    Returns: None
    """
    logger.info("Name Python files with lowercase and underscores.")
    logger.info("In Python, comments start with a '#' symbol and are not executed.")
    logger.info(
        "Comments can also be wrapped in triple single quotes or triple backticks."
    )


def show_variables_and_types() -> None:
    """Show Python variables and variable types.

    Arguments: None - nothing is passed in via the parentheses.
    Returns: None
    """
    logger.info("Variables are used to store values.")
    logger.info("Type hints are optional but recommended for clarity.")
    logger.info("  example_number = 42")
    logger.info("  count: int = 42")
    logger.info("  temp_F: float = 42.2")
    logger.info('  user_name: str = "Data Analyst"')

    example_number = 42
    count: int = 42
    temp_f: float = 42.2
    user_name: str = "Data Analyst"
    logger.info(f"Result: {example_number=}, {count=}, {temp_f=}, {user_name=}.")


def show_functions_and_fstrings() -> None:
    """Show Python functions and f-strings (formatted strings).

    Arguments: None - nothing is passed in via the parentheses.
    Returns: None
    """
    logger.info("Functions in Python are blocks of reusable code.")
    logger.info("You can call a function by using its name followed by parentheses.")
    logger.info("We use f-strings to combine text and values in Python.")
    logger.info(
        "  Put the 'f' immediately before the opening quote of the string text."
    )


def show_builtins_example() -> None:
    """Show some Python built-in functions.

    Arguments: None - nothing is passed in via the parentheses.
    Returns: None
    """
    logger.info("Python has many built-in functions, like min(), max(), and len().")
    numbers = [1, 2, 3]
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    logger.info(f"For the list of numbers: {numbers}")
    logger.info(f"  The minimum value is min(numbers): {minimum}")
    logger.info(f"  The maximum value is max(numbers): {maximum}")
    logger.info(f"  The length of the list is len(numbers): {count}")


def show_truths() -> None:
    """Show that Python is case-sensitive and indentation matters.

    Arguments: None - nothing is passed in via the parentheses.
    Returns: None
    """
    is_important: bool = True
    logger.info(f"In Python, indentation matters = {is_important}!")
    logger.info(f"In Python, spelling matters = {is_important}!")
    logger.info(f"In Python, uppercase/lowercase matters = {is_important}!")


# === DECLARE A FUNCTION TO DEMONSTRATE PYTHON ===


def demo_basics() -> None:
    """Demonstrate Python basics."""
    logger.info("Starting demo_python() function.")
    show_naming_and_comments()
    show_variables_and_types()
    show_functions_and_fstrings()
    show_builtins_example()
    show_truths()
    logger.info("Experiment with this demo script to learn the basics quickly.")
    logger.info("Exiting demo_python() function.")


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None (nothing is passed in the parentheses after the `main`).

    Returns: None (nothing is returned when this function runs).

    This function creates what we call `side effects` -
    it just logs output to the console and a file.

    Use the logger variable to call info() methods to log messages.
    Call the log_header() function once to log some key details that can help with debugging.
    Call the get_summary() function to get the formatted summary string,
    Log the summary string we get back from get_summary().
    """
    logger.info("=================")
    log_header(logger, "Professional Python")
    logger.info("=================")

    logger.info("START main()")

    demo_basics()

    logger.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is just standard Python boilerplate.
# OBS: Just copy and paste it - do not bother to memorize it.

if __name__ == "__main__":
    main()
