# Python Standard Library

> Free code when using Python for analytics.

REQ: Recognize tools that are already available.

WHY: Knowing these exist can save time.

OBS: Since they are built into Python they don't need to be added to `pyproject.toml` dependencies like we do with external libraries like `pandas`.

## Data Formats and Files

- json - For handling JSON data
- csv - For reading/writing CSV files
- sqlite3 - For working with SQLite databases (built into Python)
- pathlib - For working with filesystem paths
- os - For interacting with the OS (e.g., file paths, env vars)
- sys - For system-specific parameters and functions
- urllib - For basic URL handling and data fetching (useful with or without requests)

## Math and Analysis

- math - For mathematical functions (sqrt, log, etc.)
- statistics - For statistical analysis (mean, median, stdev, etc.)
- random - For generating random numbers
- time - For time-based functions
- datetime - For date and time manipulation

## Quality, Structure, and Maintenance

- collections - For specialized containers like Counter, defaultdict
- typing - For type hints and static type checking
- unittest - For writing and running unit tests
- logging - For structured logging in Python
- re - For regular expressions and pattern matching
- pprint - For pretty-printing complex or nested data structures
- collections - For specialized containers like Counter, defaultdict
- typing - For type hints and static type checking
- unittest - For writing and running unit tests

WHY: We are aware of what's out there, in case they might be helpful.
