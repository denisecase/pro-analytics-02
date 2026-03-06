# 🔵 Run Python Code

How to run a Python file (`.py`) in VS Code.

## Before Starting

- Open your project repository folder in VS Code.
- Open a terminal.
- If external dependencies have not been installed, see the prior step for instructions.



## Task 1. Confirm VS Code Interpreter

VS Code needs a populated `.venv` to interpret our files correctly.
Check the Python version shown in the lower-right status bar.
If you've activated your `.venv` with `uv` once during project initialization, you should be fine.


If not activated already, set the VS Code Interpreter:

1. Open the Command Palette: Press **Ctrl Shift P** (Windows/Linux) or **Cmd Shift P** (Mac).
2. Type **Python: Select Interpreter** in the Command Palette search bar.
3. Select it from the dropdown.
4. Choose the recommended local `.venv` interpreter.
5. Confirm the Python version in the lower-right status bar.


### Task 2. Set Auto Save Option (If you haven't already)

In VS Code, use the menu to enable the **File / Auto Save** option.



## Task 3. Run the Python File (Recommended)

If your code is part of a package inside `src/`, run it as a **module**.
Replace `demo_module_basics` with your actual script name.
Run from the **project root directory** (same level as `pyproject.toml`).

```shell
uv run python -m pro_analytics_02.demo_module_basics
```

This helps local imports get picked up correctly.


### Alternatively, Run as a Script

Replace `demo_module_basics.py` with your actual script name.
Run from the **project root directory** (same level as `pyproject.toml`).


```shell
uv run python src/pro_analytics_02/demo_module_basics.py
```

**IMPORTANT**
- Running as a script will fail if your file imports other local modules.
- If you are not using the `src` organization, and you don't have any local imports, then this will work to run your script.

## Task 4. Update Project README.md

Record your process and your project commands in your project README.md.

## Note on Underscores

Python import rules do not allow dashes. Use underscores in folder and file names.

- Underscores used on the Python side (imports, modules, folders).
- Dashes used on the packaging side (PyPI, metadata).
