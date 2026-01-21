# Running Python Projects Reliably

Python is an **interpreted language**, not a compiled one.
That means Python code always runs **inside an active runtime environment**,
much like an operating system is required to run programs on a machine.

Because of this, certain aspects of Python execution are inherently more complex
than in compiled languages such as Java, C#, Go, or Rust,
where the compiler resolves many decisions ahead of time.

In Python, those decisions are made **every time the program runs**.

---

## 1. Python Run Requirements

Every time Python runs, it must answer three questions:

1. **Where is the project root?**
2. **What code belongs to this project (the package)?**
3. **Which Python environment should be used?**

If any of these are unclear, you may see:
- import errors
- _unknown type_ or _missing import_ diagnostics
- code that behaves differently depending on how it is launched

Python project structure helps make these answers explicit.


## 2. Recommended Project Structure (Use `src/`)

A widely used and recommended layout is the **src layout**, which separates:

- project configuration
- importable Python code
- data and generated artifacts

Example:

```
project-name/
├─ pyproject.toml        # Project definition (root)
├─ .venv/                # Project-specific Python environment
├─ src/
│  └─ project_package/
│     ├─ __init__.py
│     ├─ app_main.py
│     └─ other_module.py
├─ data/
│  ├─ raw/
│  └─ processed/
```

### Benefits

- `src/` defines **exactly** which code is importable
- it prevents accidental imports from unrelated files
- it matches how Python packages are built, tested, and deployed
- `src/ is widely used in professional Python projects.

## 3. Import Local Modules Using Package

Inside the package directory (`src/project_package/`):

- each `.py` file is a **module**
- the directory itself is a **package**
- imports use the **full package path**

Example:

```python
from project_package.other_module import some_function
```

Absolute, **package-based local imports** are explicit help editors and tools.



## 4. Option 1: Run a File As a Script

```shell
python path/to/app_main.py
```

Python:
- treats the file as a standalone script
- resolves imports relative to the current working directory
- can behave differently depending on how and where it is launched

This often works, but can be sensitive to context and tooling.

## 5. Option 2: Run a File As a Module (Preferred)

```shell
python -m project_package.app_main
```

This tells Python:
- the code belongs to a package
- the package root should be added to the import path
- imports should be resolved using package rules

This matches:
- how test runners execute code
- how installed packages are invoked
- how automation and CI systems run Python projects

**Running as a module aligns with Python's packaging model and is more robust.**


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

Two commands that look similar can behave differently because they produce different import paths.


### How to Inspect

We may want to know what interpreter path Python is using,
regardless of editor UI or labels.

If you use `uv`, this command reports the interpreter used for the current project environment:

```shell
uv run python -c "import sys; print(sys.executable)"
```
