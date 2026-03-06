# Common Standard Library Modules (No Install Required)

These modules are built into Python and **do not need to be installed**.
They are available automatically in every Python environment.

> Note: These modules are part of the Python Standard Library.
> Do **not** add them to  `pyproject.toml` or `requirements.txt`.

---

## Data Handling

| Module | Purpose |
|---------|----------|
| [`json`](https://docs.python.org/3/library/json.html) | Handle JSON data (read, write, serialize). |
| [`csv`](https://docs.python.org/3/library/csv.html) | Read and write CSV files. |
| [`sqlite3`](https://docs.python.org/3/library/sqlite3.html) | Work with SQLite databases (included with Python). |

---

## Filesystem and System Access

| Module | Purpose |
|---------|----------|
| [`pathlib`](https://docs.python.org/3/library/pathlib.html) | Work with filesystem paths using object-oriented syntax. |
| [`os`](https://docs.python.org/3/library/os.html) | Interact with the operating system (file paths, environment variables). |
| [`sys`](https://docs.python.org/3/library/sys.html) | Access system-specific parameters and functions. |
| [`urllib`](https://docs.python.org/3/library/urllib.html) | Basic URL handling and data fetching (useful with or without `requests`). |

---

## Mathematics and Randomness

| Module | Purpose |
|---------|----------|
| [`math`](https://docs.python.org/3/library/math.html) | Mathematical functions (`sqrt`, `log`, etc.). |
| [`statistics`](https://docs.python.org/3/library/statistics.html) | Basic statistics (mean, median, stdev). |
| [`random`](https://docs.python.org/3/library/random.html) | Generate random numbers. |
| [`time`](https://docs.python.org/3/library/time.html) | Time-based functions (sleep, timing). |
| [`datetime`](https://docs.python.org/3/library/datetime.html) | Date and time manipulation. |

---

## Logging and Pattern Matching

| Module | Purpose |
|---------|----------|
| [`logging`](https://docs.python.org/3/library/logging.html) | Structured and configurable logging. |
| [`re`](https://docs.python.org/3/library/re.html) | Regular expressions and pattern matching. |
| [`pprint`](https://docs.python.org/3/library/pprint.html) | Pretty-print complex or nested data structures. |

---

## Advanced Containers and Typing

| Module | Purpose |
|---------|----------|
| [`collections`](https://docs.python.org/3/library/collections.html) | Specialized containers (`Counter`, `defaultdict`, etc.). |
| [`typing`](https://docs.python.org/3/library/typing.html) | Type hints and static type checking. |

---

## Testing (Modern Context)

While Python includes [`unittest`](https://docs.python.org/3/library/unittest.html) by default,
most modern projects use **pytest** (a third-party tool) for its simplicity and better reporting.
`pytest` is *not* part of the standard library and must be installed separately.

---

**Summary**

All modules listed above are **available automatically** with any standard Python 3 installation.
They require **no installation**, **no network access**, and are safe to import in all environments.
