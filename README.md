# Pro Analytics 02

[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://denisecase.github.io/pro-analytics-02/)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![CI Status](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci-python-mkdocs.yml/badge.svg?branch=main)](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci-python-mkdocs.yml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project starter and guide.

<!--
REQ: Title, badges, and positioning statement appear before anything else.
WHY: README opens with exactly one page title, credibility signals, then a concise scope statement.
-->

## Overview and Scope

This repository serves **two purposes**:

1. A **ready-to-use starter repository** for professional Python projects
2. A **worked example and reference guide** for modern Python workflows

It demonstrates how to structure a project, configure tooling, and document decisions
in a way that scales from small projects to large, collaborative codebases.

<!--
REQ: Clarify what the repo is and is not before giving instructions.
WHY: Explicit scope reduces confusion and misapplication.
-->

## Installation and Setup

This project requires **two kinds of setup**:

- **Machine setup** (once per machine): install tools and configure Git
- **Project setup** (once per project): customize identity, install dependencies, and verify the environment

If you copied or cloned this repository to start a new project:

- Open `REPO_FIRST_STEP.md`
- Follow the instructions exactly

This step updates repository identity so links, documentation, and packaging metadata
reflect the new project.

Authoritative, step-by-step instructions are provided in the documentation:

- **Workflow 1: Set Up Machine** (once per machine)
- **Workflow 2: Set Up Project** (per project)

These workflows are intentionally detailed and OS-specific.
They serve both as instructions and as an example of professional project documentation.

<!--
WHY: Identity must be correct before any setup output is generated.
REQ: README points to authoritative setup instructions without duplicating them.
WHY: Detailed, OS-specific steps belong in docs, not the README.
-->

## Usage and Customization

After setup, work proceeds inside a consistent project layout.

You may:

- Add or remove dependencies in `pyproject.toml`
- Enable or disable tooling rules intentionally
- Modify or remove documentation by editing `mkdocs.yml`
- Organize code using the provided `src/` layout

Customization decisions are documented inline using annotations.

<!--
WHY: Emphasize intentional customization over ad-hoc changes.
-->

## Examples

This repository itself serves as a working example.

Additional examples may be added or removed depending on project needs.

<!--
WHY: Avoid duplicating examples already embodied by the repository.
-->

## Documentation

This repository includes an associated
[**documentation site**](https://denisecase.github.io/pro-analytics-02/).

- The site provides both a **reference** and a **worked example**
- Source files live in the `docs/` directory
- Navigation and visibility are controlled by `mkdocs.yml`
- Documentation may be edited, reorganized, or removed

If documentation is not needed, you may delete `docs/` and `mkdocs.yml`
without affecting the rest of the project.

<!--
REQ: Make documentation optional and safe to remove.
WHY: Documentation is an instrument, not a requirement.
-->

## Three Workflows

There are three workflows for analytics projects.
Complete the first two - and then use the third to complete the project.
Details provided below.

- 01: Set Up Machine (Once Per Machine)
- 02: Set Up Project (Once Per Project)
- 03: Daily Workflow (Working With Python Project Code)

## 01: Set Up Machine (Once Per Machine)

Follow the detailed instructions at:
[**01. Set Up Your Machine**](./docs/01-set-up-machine/index.md).

🛑 Do not continue until all these steps are complete and verified.

## 02: Set Up Project (Once Per Project)

Follow the detailed instructions at:
[**02. Set Up Your Project**](./docs/02-set-up-project/index.md).

Detailed instructions are provided to:

1. Sign in to GitHub, open this repository in your browser, and click **Copy this template** to get a copy in **YOURACCOUNT**.
2. Enable GitHub Pages.
3. Open a machine terminal in your `Repos` folder and clone your new repo.
4. Change directory into the repo, open the project in VS Code, and install recommended extensions.
5. Set up a project Python environment (managed by `uv`) and align VS Code with it.

Use the instructions above to get it ALL set up correctly.
Most people open a terminal on their machine (not VS Code), open in their Repos folder and run:

```shell
git clone https://github.com/YOURACCOUNT/pro-analytics-02

cd pro-analytics-02
code .
```

When VS Code opens, accept the Extension Recommendations (click **`Install All`** or similar when asked).

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal** in the root project folder.
Run the following commands, one at a time, hitting ENTER after each:

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

If asked: "We noticed a new environment has been created. Do you want to select it for the workspace folder?" Click **"Yes"**.

If successful, you'll see a new `.venv` folder appear in the root project folder.

Optional (recommended): install and run pre-commit checks (repeat the git `add` and `commit` twice if needed):

```shell
uvx pre-commit install
git add -A
uvx pre-commit run --all-files
git add -A
uvx pre-commit run --all-files
```

🛑 Do not continue until all REQUIRED steps are complete and verified.

## 03: Daily Workflow (Working With Python Project Code)

We follow the detailed instructions at:
[**03. Daily Workflow**](./docs/03-daily-workflow/index.md).

Commands are provided below to:

1. Git pull
2. Run and check the Python files
3. Build and serve docs
4. Save progress with Git add-commit-push
5. Update project files

VS Code should have only this project (datafun-01-foundations) open.
Use VS Code menu option `Terminal` / `New Terminal` and run the following commands:

```shell
git pull
```

In the same VS Code terminal, run the files:

```shell
uv run python src/pro_analytics_02/demo_module_basics.py
```

Run checks and tests (as available):

```shell
uv run ruff format .
uv run ruff check . --fix
uv run pytest --cov=src --cov-report=term-missing
```

Build and serve docs (hit **CTRL+c** in the VS Code terminal to quit serving):

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

While editing project code and docs, repeat the commands above to run files, check them, and rebuild docs as needed.

Save progress frequently (some tools may make changes; **re-running add and commit** ensures everything gets committed):

```shell
git add -A
git commit -m "update"
git push -u origin main
```

## Tools

This professional Python project uses:

- `uv` for dependency management and command execution
- `ruff` for formatting and linting
- `pytest` for test execution
- `mkdocs` for documentation

Alternative tools and stricter configurations are documented inline
and may be enabled intentionally.


## Annotations

[ANNOTATIONS.md](./ANNOTATIONS.md)

<!--
WHY: Keep decision rationale close to code and configuration.
-->

## Citation

[CITATION.cff](./CITATION.cff)

<!--
WHY: Support correct citation and attribution.
-->

## License

[MIT](./LICENSE)

<!--
WHY: Provide terms of reuse and limits of liability.
-->

## SE Manifest

[SE_MANIFEST.toml](./SE_MANIFEST.toml)

<!--
WHY: Make explicit the intent, boundaries, and scope of this repository.
-->
