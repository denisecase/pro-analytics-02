# 🏠 Guide to Professional Python

<!-- On a page that could be read aloud,
use two asterisks instead of backticks
for code. -->

This repository provides a clear, concise guide for professional Python projects.

## ⚠️ New to Terminals, Git, or Repositories?

This guide assumes you can open a terminal and run a command.
If that is new to you (it often is), start with
**[Applied Computing Foundations](https://denisecase.github.io/applied-computing-foundations/)**,
a short prerequisite.

## For Returning Users: What Changed (August 2026)

If you have used this guide before, some tools and conventions have evolved.

- Updated **uv** Python manager process.
- NOTE: we never install Python directly, it is only installed via **uv**.
- Updated **pyproject.toml** conventions.
- Dropped Node and npx from the recommended workflow
- Replaced Pyright/Pylance with the new Rust-based **ty** for type checking. Affects:
  **.vscode/extensions.json** and **pyproject.toml**.
- Added support for **marimo** notebooks stored as plain **.py** files.

For best results, please do not assume an earlier setup is still current.
Follow the steps below to confirm the recommended setup is complete.

## First is the Worst

The first time through each step is the hardest.
New tools, new terms, and new steps all have to line up,
so **allow extra time when performing a workflow for the first time**.

It gets easier with experience.
The tools are installed just once and the project setup steps become routine.
The professional workflow enables every project that follows.

## First, Set Up Machine (One-Time)

This is done once, then revisited as needed.
Go to:

- 🟢 [Workflow A. Set Up Machine](workflow-a-set-up-machine/)
  to install a few professional tools and get the machine ready for development.
  A machine that is set up correctly makes everything that follows easier.

## Then, Start a Project

We have centralized the instructions for common workflows.
Most people start with:

- 🔵 [Workflow B. Apply Example Project](workflow-b-apply-example-project/)
  to start with an existing project and apply the skills to a new problem.

## Later, Start a Project From Nothing

For independent projects, the steps are similar.

- Go to 🟠 [Workflow C. Start Project From Nothing](workflow-c-start-new-project/)
  to **create and configure a new Python project** from scratch.

## OPTIONAL: Share Feedback

Feel free to ask questions in the
[GitHub Discussions](https://github.com/denisecase/pro-analytics-02/discussions)
or raise a
[GitHub Issue](https://github.com/denisecase/pro-analytics-02/issues)
if you have suggestions or need additional clarification.
