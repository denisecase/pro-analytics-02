"""Demonstrate Python basics for professional analytics.

This module demonstrates fundamental Python concepts essential for data analysts,
including imports, variables, functions, and function calls.

Module Information:
    - Filename: demo_module_basics.py
    - Module: demo_module_basics
    - Location: src/analytics_project/

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

#####################################
# Imports At the Top
#####################################

# Import the shared logger
from .utils_logger import init_logger, logger

#####################################
# Define Functions
#####################################


def show_naming_and_comments() -> None:
    logger.info("Name Python files with lowercase and underscores.")
    logger.info("In Python, comments start with a '#' symbol and are not executed.")
    logger.info("Comments can also be wrapped in triple single quotes or triple backticks.")


def show_variables_and_types() -> None:
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
    logger.info("Functions in Python are blocks of reusable code.")
    logger.info("You can call a function by using its name followed by parentheses.")
    logger.info("We use f-strings to combine text and values in Python.")
    logger.info("  Put the 'f' immediately before the opening quote of the string text.")


def show_builtins_example() -> None:
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
    is_important: bool = True
    logger.info(f"In Python, indentation matters = {is_important}!")
    logger.info(f"In Python, spelling matters = {is_important}!")
    logger.info(f"In Python, uppercase/lowercase matters = {is_important}!")


#####################################
# Combine all functions into one demo function
#####################################


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


#####################################
# Define main() for standalone testing
#####################################


def main() -> None:
    """Test demo locally."""
    try:
        init_logger()
    except Exception as exc:
        logger.exception(f"Exception occurred during logger initialization: {exc}")
    demo_basics()


#####################################
# Conditional Execution
# Run if this file is executed directly
#####################################


if __name__ == "__main__":
    main()


#####################################
# List all exports (things that other modules can use)
#####################################

__all__ = ["demo_basics"]
