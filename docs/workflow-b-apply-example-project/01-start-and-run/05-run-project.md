# 🔵 Run the Project Code

> Run the example project exactly as provided.

## Step 1. Find the Run Command

Open the project `README.md`.

Use the exact run command shown there.

For example:

```shell
uv run python -m datafun.app
```

## Step 2. Run the Project

Open a VS Code terminal in the project root folder.

Copy the command from the README,
paste it into the terminal,
and press **Enter**.

## Step 3. Verify

The project should run from beginning to end without an unexpected error.

You may see terminal output and a new `project.log` file.

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

### Windows Smart Application Control

If Windows reports that `python.exe` was blocked, see:

[Windows: Smart App Control Blocks python.exe](../../help/04-windows-smart-app-control-python.md)

</details>

<details markdown>
<summary>More about the Python command</summary>

For professional projects that use a `src/` layout,
we usually run Python code as a module:

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

## Success

- [ ] The example runs without an unexpected error.
- [ ] Expected output appears.
- [ ] `project.log` appears if the project creates one.

---

[◄ Back to 🔵 Phase 1](index.md)
