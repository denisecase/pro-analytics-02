# 🔵 Run and Check the Project Code

> Run the example project exactly as provided,
> then practice its professional checks.

## FIRST: Find the Run Command

Open the project `README.md`.
Use the exact run command shown there.
For example:

```shell
uv run python -m datafun.app
```

## Step 1. Run the Project Code

Open a VS Code terminal in the project root folder.
Copy the command from the README,
paste it into the terminal,
and press **Enter** or **Return** to run the command.

If the command fails with an import error, see
[Running Python Projects Reliably](https://denisecase.github.io/pro-analytics-02/reference/python/running-python/).

## Step 2. Run Checks and Tests (as available)

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

## Step 3. Build Documentation (If Applicable)

For projects using Zensical to build an associated project
documentation site, run:

```shell
uv run python -m zensical build
uv run python -m zensical serve
```

Open the local URL displayed in the terminal to review the documentation.

Press **Ctrl+C** in the terminal to stop the local server.

## Verification

1. The project should run from beginning to end without an unexpected error.
2. You may see a success message indicating it executed successfully.
3. You may see terminal output and a new `project.log` file may appear.
4. The Git hooks should install, and `uvx prek run --all-files` should finish
   with all checks passing.
5. Ruff, ty, and pytest should complete without reported errors.
6. If the project has documentation, it should build and open locally.

## Success

- [ ] The project should run and end with a line
      like **"Executed successfully!"** in the terminal.
- [ ] You may see a new `project.log` file appear.
- [ ] You may see new generated artifacts appear.
- [ ] If you are running a marimo app, you'll see it open in your browser.
- [ ] The Git hooks are installed and the checks pass.
- [ ] Ruff, ty, and pytest complete without reported errors (as available).
- [ ] The project documentation builds and opens locally (if applicable).

## Troubleshooting

<details markdown>
<summary>If the terminal ran an `activate` command automatically</summary>

Some terminals may automatically activate the selected environment.
This is harmless. `uv run` manages the project environment,
so manual activation is not required.

</details>

<details markdown>
<summary>If the project does not run</summary>

First verify:

- You opened only the project folder in VS Code.
- Your terminal is in the project root folder.
- You completed the Python environment setup.
- You copied the exact command from the README.

The project root contains files such as:

```text
pyproject.toml
README.md
src/
```

If the environment is not ready, return to:

[Set Up the Project Python Environment](04-set-up-environment.md)

</details>

<details markdown>
<summary>If Windows reports that `python.exe` was blocked</summary>

See:
[Windows: Smart App Control Blocks python.exe](../../help/04-windows-smart-app-control-python.md)

</details>

## More About Python Execution Commands

<details markdown>
<summary>More about the uv run python command</summary>

For professional projects that use a `src/` layout,
we usually run Python code as a module
where package_name is specific to the project:

```shell
uv run python -m package_name.module_name
```

For example:

```shell
uv run python -m datafun.app
```

- `uv run` uses the project's managed environment.
- `python` runs Python.
- `-m` runs a Python module.
- `datafun.app` identifies the package and module.

Running as a module helps Python find local imports correctly.

</details>

## Professional Recommendations and Reminders

- Enable **File / Auto Save** in VS Code or save changes regularly.
- Run the project and checks after making changes.
- Use logging and debugging statements to investigate errors.
- Review results and resolve unexpected errors before committing changes.

---

[◄ Back to 🔵 Phase 1](index.md)
