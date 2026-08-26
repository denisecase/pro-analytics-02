# 🔵  Run and Check

This mirrors professional practice: run and check code as you work.

## Step 1. Run the Project Code

Ensure only the **project repository folder** is open in VS Code.

Open a new VS Code terminal using the VS Code menu
**Terminal / New Terminal**.
The terminal should open in the root project folder.

Find the exact command to run the project in the **project README.md**.
In the VS Code terminal, copy and paste that command and hit ENTER or RETURN.
For example, a project command might look like:

```shell
uv run python -m datafun.app
```

The exact command and package name may be different for your project.

## Step 2. (As Needed) Add / Update Dependencies

As you modify the project,
you may need to add or update dependencies in pyproject.toml.

Periodically (to keep dependencies current)
or after changing project dependencies,
run these commands
(copy and paste one at a time and hit ENTER or RETURN after each)
in the VS Code terminal:

```shell
uv python install
uv lock --upgrade
uv sync
```

These commands ensure the required Python version is available,
update project dependencies to the latest compatible versions,
and install the locked dependencies in the local project environment (.venv/).

## Step 3. Run Checks and Tests (as available)

Run the following commands in a VS Code terminal to:

1. Format all project Python files using **Ruff**.
2. Check and fix all project Python files (automatically "lint" or fix basic issues).
3. Check Python types using **ty**.
4. Run **pytest** if you have working tests in the **tests/** folder.

```shell
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
```

## Step 4. Build Documentation

Make sure the documentation dependencies in **pyproject.toml** are installed.
Then build the project docs, fix any errors, and serve them locally to test.

```shell
uv run python -m zensical build
uv run python -m zensical serve
```

- After running the **serve** command,
  a local URL for the documentation will be displayed.
- To open the site, press **Ctrl and click**
  the provided link (at the same time) to view the documentation.
  Use **Cmd and click** on Mac.
- To stop the server, click in the terminal, and
  press **Ctrl c** to terminate the local hosting process.

<details markdown>
<summary>Why we include python -m</summary>

In a command like this: **uv run python -m zensical build**,
the **python -m** is sometimes optional.
The longer form is safer for heterogeneous environments.
It:

- explicitly uses the Python interpreter selected by **uv**
- avoids relying on a separate console-script wrapper
- behaves consistently across Windows, macOS, and Linux
- is officially supported by the Zensical package
- provides one standard command form for all users and machines wherever possible

</details>

## Professional Reminders

- Use the VS Code menu to turn on Auto Save
  (**File / Auto Save**), or remember to save your changes as you work.
- Comment out code as needed to get a version that runs without errors.
- If you encounter errors, use debugging tools,
  strategically placed **logging statements**,
  or **print()** calls to reveal where execution
  is occurring and what values are stored in variables.

---

[◄ Back to 🔵 Workflow B](index.md)
