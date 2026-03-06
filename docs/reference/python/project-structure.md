# Project Structure

REQ: Introduce a clear, repeatable layout for Python projects.

WHY: Consistent organization supports reuse, testing, and collaboration.

OBS: This structure scales from small scripts to professional projects.
 Not every project uses every folder immediately.

---

## Common Project Layout

A typical Python project is organized into folders by purpose:

- `src/` - Python source code
- `data/` - data files used by the project
- `notebooks/` - exploratory analysis and experiments
- `docs/` - written documentation
- `pyproject.toml` - project configuration and dependencies

This separation keeps concerns clear and avoids mixing code, data, and notes.

## The `src/` Directory

The `src/` directory contains Python packages.

Example:

- `src/project_name/`
  - `__init__.py`
  - `main.py`
  - additional modules as needed

WHY:
Placing code under `src/` prevents accidental imports from the project root and makes package boundaries explicit.

OBS:
For very small or introductory projects, code may temporarily live at the project root.
The `src/` layout becomes increasingly valuable as projects grow.

## The `data/` Directory

The `data/` directory stores input files such as:

- CSV files
- JSON files
- SQLite databases

WHY:
Data is not code.
Keeping data separate avoids confusion and accidental modification.

OBS:
Small example datasets are often included directly in the repository.
Large or sensitive datasets are typically excluded.

## The `notebooks/` Directory

The `notebooks/` directory is used for exploratory work.

Typical contents:

- Jupyter notebooks
- temporary experiments
- visualizations and scratch analysis

WHY:
Notebooks support exploration and learning.
They are well suited for trying ideas before writing reusable code.

OBS:
Notebooks are not required for every project.
Core logic should eventually live in Python modules under `src/`.

## The `docs/` Directory

The `docs/` directory contains written explanations and reference material.

Examples:

- concept explanations
- project structure references
- usage notes

WHY: Documentation supports understanding and reuse.

OBS: Documentation can be simple Markdown files.
A documentation site can be added later without restructuring content.

## `pyproject.toml`

The `pyproject.toml` file defines:

- project metadata
- Python version requirements
- dependencies
- development tools

WHY: Modern Python projects use `pyproject.toml` as a single source of truth.

## Choosing a Structure

For introductory projects:

- a single Python file at the root is acceptable
- `data/` and `docs/` can still be introduced early

For multi-file or long-lived projects:

- use `src/` for code
- separate data and documentation

The goal is not complexity, but clarity.

## Consistency Matters More Than Perfection

A consistent structure:

- reduces cognitive load
- makes projects easier to navigate
- supports professional habits

Once a structure is chosen, it is reused across projects.

## Example

```
project-name/
  pyproject.toml
  README.md
  LICENSE
  .gitignore (and other config files)

  src/
    project_name/
      __init__.py
      __main__.py
      app.py
      py.typed   # if typed
  tests/
    test_smoke.py # logic in small functions and test each function carefully

  data/
    raw/
    processed/
    README.md

  docs/
    index.md
    other Markdown files supporting the project.
    use docs/en/ if working internationally

  notebooks/
    01-explore.ipynb
```
