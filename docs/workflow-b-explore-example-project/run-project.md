# 🔵  Run and Check

Professional practice is to run, check, and test code regularly as changes are made.

Ensure only the **project repository folder** is open in VS Code.

Open a new VS Code terminal using the VS Code menu
**Terminal / New Terminal**.
The terminal should open in the root project folder.

## Step 1. Run the Project Code

Find the exact command to run the project in the **project README.md**.
In the VS Code terminal,
copy and paste that command, then hit ENTER or RETURN.

For example:

```shell
uv run python -m datafun.app
```

The package and module names may differ by project.
For more information, see
[Running Python Projects Reliably](../reference/python/running-python.md).

## Step 2. Update Dependencies (As Needed)

As you modify the project,
you may need to add or update dependencies in pyproject.toml.

After changing dependencies in `pyproject.toml`,
and periodically to keep dependencies current,
run these commands
(copy and paste one at a time and hit ENTER or RETURN after each)
in the VS Code terminal:

```shell
uv python install
uv lock --upgrade
uv sync
```

These commands install the required Python version,
update the dependency lockfile, and
synchronize the project's `.venv` environment.

For additional instructions and troubleshooting, see
[Set Up Project Environment](01-start-and-run/04-set-up-environment.md).

## Step 3. Run Checks and Tests (as available)

Use the project's configured development tools to format,
check, and test the code:

```shell
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
```

- **Ruff:** Formats code and identifies common programming problems.
- **ty:** Checks Python types.
- **pytest:** Runs automated tests, when available.
  Skip the `pytest` command in projects with no `tests` folder.

Review and address reported issues before continuing.

## Step 4. Build Documentation (If Applicable)

For projects using Zensical to build an associated project
documentation site, run:

```shell
uv run python -m zensical build
uv run python -m zensical serve
```

Open the local URL displayed in the terminal to review the documentation.

Press **Ctrl+C** in the terminal to stop the local server.

## Professional Reminders

- Enable **File / Auto Save** in VS Code or save changes regularly.
- Run the project and checks after making changes.
- Use logging, debugging tools, or `print()` statements to investigate errors.
- Review results and resolve unexpected errors before committing changes.

---

[◄ Back to 🔵 Workflow B](index.md)
