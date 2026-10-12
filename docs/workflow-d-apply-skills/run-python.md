# 🟣 Run and Check

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
**Set Up Project Environment** from Workflow C.

## Step 5. Update Project README.md

Record your process and exact project commands in the project README.md.

## Professional Recommendations and Reminders

- Enable **File / Auto Save** in VS Code or save changes regularly.
- Run the project and checks after making changes.
- Use logging and debugging statements to investigate errors.
- Review results and resolve unexpected errors before committing changes.

---

[◄ Back to 🟣 Workflow D](index.md)
