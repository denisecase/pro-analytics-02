# 🏠 Guide to Professional Python

This repository provides a clear, concise guide for professional Python projects.

## ⚠️ New to Terminals, Git, or Repositories?

This guide assumes you can open a terminal and run a command.
If that is new to you (it often is), start with
**[Applied Computing Foundations](https://denisecase.github.io/applied-computing-foundations/)**,
a short prerequisite covering files, folders, terminals, and Git.

## Professional Python Management

This version (**Pro Analytics 02**) uses the
newer, faster, Rust-based `uv` tool for managing
Python environments and projects.
(An earlier version, 01, of the guide used `pip` and `venv`.)

## Common Workflows

Instructions are provided for common workflows.

- Go to 🟢 [A. Set Up Machine](workflow-a-set-up-machine/)
  to **set up a machine** for Python development.

- Go to 🔵 [B. Apply Example Project](workflow-b-apply-example-project/)
  to **learn skills** cloning and running a working example,
  taking ownership of it with a new Git history, modifying it,
  and applying the skills to a new problem.

- Go to 🟠 [C. Start Project From Nothing](workflow-c-start-new-project/)
  to **create and configure a new Python project** from scratch (e.g., Capstone projects).

## Consistent Foundation across Courses and Projects

Learning complex techniques is easier when the underlying project structure stays consistent.

Professional work does not follow a single starting pattern.
Sometimes we begin from a working example or existing codebase,
sometimes we build a new project from scratch, and
sometimes we begin from a template.
These workflows develop different skills:
reading unfamiliar projects,
understanding how project infrastructure is assembled,
adapting existing work, and using professional scaffolding efficiently.

The goal is to become comfortable working with professional Python projects
regardless of how they begin.

## For Returning Users: What Changed (August 2026)

- streamlined `uv` usage
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
