# 🔵 Run and Check

This mirrors professional practice: run and check code as you work.

## Step 1. Run Code

Run Python and/or notebooks as needed for your project.

See [Run Python](../run-python.md) or [Run Notebooks](../run-notebook.md)

## Step 2. (As Needed) Add / Update Dependencies

As we work on the code, we may find we need additional dependencies listed in `pyproject.toml`.
For example, after generating interesting results we may add `matplotlib` to visualize charts.
Edit `pyproject.toml` and add packages to the **dependencies** section as needed.
You may occasionally need to clean the cache (delete downloaded dependency files stored locally).
Then re-run the `uv sync` command as shown below:

```shell
uv cache clean
uv sync --extra dev --extra docs --upgrade
```

When working on a project, open the project repository folder in VS Code.
In general, all terminal commands should be executed in the **root project folder**.

## Step 3. Run Checks and Tests (as available)

Run the following commands in a VS Code terminal to:

1. Format all project Python files using **Ruff**.
2. Check and fix all project Python files (automatically "lint" or fix basic issues).
3. Optional: Run pytest if you have working tests in the `tests/` folder.

```shell
uv run ruff format .
uv run ruff check . --fix
uv run pytest --cov=src --cov-report=term-missing
```

## Step 4. Build Documentation

Make sure the documentation dependencies in `pyproject.toml` are installed.
Then build the project docs, fix any errors, and serve them locally to test.

```shell
uv run zensical build
uv run zensical serve
```

- After running the `serve` command, a local URL for the documentation will be displayed.
- To open the site, press **Ctrl and click** the provided link (at the same time) to view the documentation. Use **Cmd and click** on Mac.
- To stop the server, click in the terminal, and press **Ctrl c** (or **Cmd c** on Mac) to terminate the local hosting process.


## Professional Reminders

- Use the VS Code menu to turn on Auto Save (**File / Auto Save**), or remember to save your changes as you work.
- Comment out code as needed to get a version that runs without errors.
- If you encounter errors, use debugging tools, strategically placed logging statements, or `print()` calls to reveal where execution is occurring and what values are stored in variables.
