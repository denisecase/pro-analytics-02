# Running Python Projects Reliably

Running a Python project requires the correct Python interpreter,
project dependencies, and import paths.

A project may run successfully in one environment but fail in another
if these are configured differently.

Professional Python project conventions help make execution
consistent across Windows, macOS, and Linux.

---

## 1. Python Run Requirements

When running a Python project:

1. Run commands from the root project folder containing `pyproject.toml`.
2. Use the local `.venv` with the Python version and dependencies managed by `uv`.
3. Resolve local imports (e.g. from a util.py file) correctly.

If these are incorrect, you may see:

- `ModuleNotFoundError` or other import errors
- missing-import diagnostics in VS Code
- different results depending on how the program is launched

Using a consistent project structure and `uv run` commands
helps prevent these problems.

## 2. Recommended Project Structure (Use `src/`)

A widely used and recommended layout is the **src layout**, which separates:

- project configuration
- importable Python code
- data and generated artifacts

Example:

```text
project-name/
├─ pyproject.toml        # Project definition (root)
├─ .venv/                # Project-specific Python environment
├─ src/
│  └─ project_package/   # custom package name (see note)
│     ├─ __init__.py
│     ├─ app_main.py
│     └─ other_module.py
├─ data/
│  ├─ raw/
│  └─ processed/
```

### Custom Package Names (Must Use Underscores)

Python import rules do not allow dashes.
Use **underscores** in Python folder and file names.

- Underscores used on the Python side (imports, modules, folders).
- Dashes used on the packaging side (repo name, PyPI, metadata).

### Benefits

- Separates importable project code from configuration and other files.
- Reduces accidental imports from the project root.
- Supports consistent packaging, testing, and deployment.
- Follows a widely used professional Python project convention.

## 3. Import Local Modules Using Package Names

Inside `src/project_package/`:

- `project_package/` is the Python package for that project (e.g., `datafun`).
- Each `.py` file can be imported as a module.
- `__init__.py` identifies the directory as a regular Python package.
- Absolute imports use the package name.

Example:

```python
from project_package.other_module import some_function
```

Package-based imports make dependencies between modules explicit
and help Python, VS Code, and automated tools resolve them consistently.

## 4. Option 1: Run a File as a Script

From the project root:

```shell
uv run python src/project_package/app_main.py
```

Python executes the file directly and places the script's directory
at the beginning of its import search path.

This can cause problems when the script imports other modules
using the full project package name.

Direct script execution is useful for standalone scripts,
but is generally **not recommended** for applications organized
as Python packages.

## 5. Option 2: Run a File as a Module (Preferred)

From the project root:

```shell
uv run python -m project_package.app_main
```

Python locates the module through its import system
and executes it within its package context.

This approach:

- Supports package-based imports.
- Works consistently with a properly installed project package.
- Matches common Python testing and automation practices.
- Uses the project's Python environment through `uv run`.

For `src/` projects, **run code as a module**
unless the project README specifies otherwise.

## 6. Editor: Open One Project at a Time

Editors such as VS Code:

- cache interpreter selections
- remember import resolution **per workspace**
- infer project boundaries from the opened folder

Opening multiple projects at once can cause:

- the wrong environment to be selected
- imports to resolve from another project
- misleading diagnostics

Recommended practice:

- **open one project at a time**
- ensure the project root is the folder opened in the editor and the default terminal

---

## More Information

### Behind the Scenes (How Python Resolves Imports)

When Python starts, it builds a list called `sys.path`.

What affects it:

- where Python is launched
- whether code is run as a script or as a module
- how the project is structured

Two commands that look similar can behave differently
because they produce different import paths.

### How to Inspect

We may want to know what interpreter path Python is using,
regardless of editor UI or labels.

If you use `uv`, this command reports the interpreter
used for the current project environment:

```shell
uv run python -c "import sys; print(sys.executable)"
```

---

[◄ Back to 🏠 Guide Home](https://denisecase.github.io/pro-analytics-02/)
