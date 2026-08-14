# Guide to Professional Python

This repository provides a clear, concise guide for professional Python projects.

This version (**Pro Analytics 02**) uses the
newer, faster, Rust-based `uv` tool for managing
Python environments and projects.
(An earlier version, 01, of the guide used `pip` and `venv`.)

## New to Terminals, Git, or Repositories?

Start with
**[Applied Computing Foundations](https://denisecase.github.io/applied-computing-foundations/)**,
a short prerequisite covering files, folders, terminals, and Git.

## Common Workflows

Instructions are provided for common workflows.

- Go to 🟢 [A. Set Up Machine](workflow-a-set-up-machine/)
  to **set up a machine** for Python development.

- Go to 🔵 [B. Apply Example Project](workflow-b-apply-example-project/)
  to **learn skills** by running, modifying, and applying an example project.

- Go to 🟠 [C. Start Project From Nothing](workflow-c-start-new-project/)
  to **create and configure a new Python project** from scratch (e.g., Capstone projects).

- Go to 🟡 [D. Start Project From Template](workflow-d-start-project-from-template/)
  to **create from a template** (e.g. marimo notebooks).

## Consistent Foundation across Courses and Projects

Learning complex techniques is easier when the underlying project structure stays consistent.

Professional work does not follow a single starting pattern.
Sometimes we join and adapt an existing project,
sometimes we build a new project from scratch,
and often we begin from an established template.
These workflows develop different skills:
reading unfamiliar projects, understanding how project infrastructure is assembled,
and using proven scaffolding efficiently.

The goal is to become comfortable working with professional Python projects
regardless of how they begin.

## Recent Updates (August 2026)

- improved and standardized `uv` environment setup
- added support for `marimo` notebooks stored as plain `.py` files
- updated `pyproject.toml` conventions ([dependency-groups] and [tool.uv])
- replaced Pyright/Pylance with `ty` for type checking, affects:
  - `.vscode/extensions.json`
  - `pyproject.toml`
  - commands listed in `README.md`, `sit.ps1`, `.github/workflows/`

## OPTIONAL: Share Feedback

Feel free to ask questions in the
[GitHub Discussions](https://github.com/denisecase/pro-analytics-02/discussions)
or raise a
[GitHub Issue](https://github.com/denisecase/pro-analytics-02/issues)
if you have suggestions or need additional clarification.
