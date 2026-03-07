# 🔵 Run and Check

Run and verify your code frequently as you work.

## Step 1. Run Code

Run Python scripts or notebooks for your project.

See:
- [Run Python](../run-python.md)
- [Run Notebooks](../run-notebook.md)

## Step 2. Add or Update Dependencies (as needed)

If your project needs additional packages, add them to the `dependencies` section in `pyproject.toml`.

Example: you might add `matplotlib` to create charts.

After updating dependencies, run:


```shell
uv cache clean
uv sync --extra dev --extra docs --upgrade
```

All commands should be run from the **project root folder** in the VS Code terminal.


## Step 3. Run Checks and Tests

Run the following commands to format code, fix common issues, and run tests if available.

```shell
uv run ruff format .
uv run ruff check . --fix
uv run pytest --cov=src --cov-report=term-missing
```

## Step 4. Build Documentation

Build and preview the project documentation locally.

```shell
uv run zensical build
uv run zensical serve
```

A local URL will appear in the terminal.
Ctrl+Click the link to open the documentation or try <localhost:8000>.

Press **Ctrl+C** in the terminal to **stop** the server.

## Professional Reminders

- Turn on **Auto Save** in VS Code (**File / Auto Save**), or save frequently.
- Comment out code as needed to keep a working version.
- If something fails, use debugging tools, logging, or `print()` to inspect values.
