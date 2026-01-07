# 🔵 Run and Check

This mirrors real work where we typically:

Run and check the code as we work. It may include:
   1. Running files or notebooks.
   2. Adding and/or updating dependencies (in `pyproject.toml`).
   3. Running automatic checks and tests on the code.


## Running Code

Run Python and/or notebooks as needed for your project.
See [Run Python](02a-run-python.md) or [Run Notebooks](02b-run-notebook.md)


## Adding / Updating Dependencies

As we work on the code,
we may need to add dependencies to `pyproject.toml`,
and re-run `uv sync ...`.

We may need to periodically clean the cache (files stored locally).

```shell
uv cache clean
uv sync --extra dev --extra docs --upgrade
```

Modify and Debug:

When working on a project, always open the project repository folder in VS Code.
In general, all terminal commands should be executed in the **root project folder**.
For example, when working in this project, all commands would be executed in the `pro-analytics-02` folder.


## Run Checks and Tests (as available)

```shell
uv run ruff format .
uv run ruff check . --fix
uv run pytest --cov=src --cov-report=term-missing
```

## Reminders

- Use the VS Code menu to turn on Auto Save (**File / Auto Save**), or remember to save your changes as you work.
- Comment out content as needed to get a version that runs without errors before doing git add-commit-push.
- If you encounter errors, use debugging tools or strategically placed print or logging statements to help identify issues.
