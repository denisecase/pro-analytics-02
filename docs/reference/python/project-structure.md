# Project Structure

There is a relatively common, clear, repeatable layout for Python projects.
This consistent organization supports reuse, testing, and collaboration.
It scales from small scripts to professional projects.

## Common Project Layout

A typical Python project is organized into folders by purpose:

- **src/** - Python source code
- **data/** - data files used by the project
- **notebooks/** - exploratory analysis and experiments
- **docs/** - written documentation
- **pyproject.toml** - project configuration and dependencies

This separation keeps concerns clear and avoids mixing code, data, and notes.

## The src/ Directory

The **src/** directory contains Python packages.

Example:

- **src/project_name/**
  - ****init**.py**
  - **main.py**
  - additional modules as needed

Placing code under **src/** prevents accidental imports
from the project root and makes package boundaries explicit.

For very small or introductory projects,
code may temporarily live at the project root.
The **src/** layout becomes increasingly valuable as projects grow.

## The data/ Directory

The **data/** directory stores input files such as:

- CSV files
- JSON files
- SQLite databases

Data is not code.
Keeping data separate avoids confusion and accidental modification.

Small example datasets are often included directly in the repository.
Large or sensitive datasets are typically excluded.

## The notebooks/ Directory

The **notebooks/** directory is used for exploratory work.
Typical contents include:

- Jupyter notebooks
- temporary experiments
- visualizations and scratch analysis

Notebooks support exploration and learning
and are well suited for trying ideas before writing reusable code.

Notebooks are not required for every project.
Core logic should live in Python modules under `src/`.

## The docs/ Directory

The **docs/** directory contains written explanations and reference material.

Examples:

- concept explanations
- project structure references
- usage notes

Documentation supports understanding and reuse.
Documentation can be simple Markdown files.
A documentation site can be added later without restructuring content.

## pyproject.toml

The **pyproject.toml** file defines:

- project metadata
- Python version requirements
- dependencies
- development tools

Modern Python projects use **pyproject.toml** as a single source of truth.

## Choosing a Structure

For introductory projects:

- a single Python file at the root is acceptable
- **data/** and **docs/** are often the first additions

For multi-file or long-lived projects:

- use **src/** for code
- separate data and documentation

## Consistency Matters More Than Perfection

A consistent structure:

- reduces cognitive load
- makes projects easier to navigate
- supports professional habits

## Example

```text
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
