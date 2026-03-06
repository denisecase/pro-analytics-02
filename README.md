# Pro Analytics 02

[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://denisecase.github.io/pro-analytics-02/)
[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](#)
[![CI Status](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci-python-zensical.yml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project starter and guide.

<!--
REQ: Title, badges, and positioning statement appear before anything else.
WHY: README opens with exactly one page title, credibility signals, then a concise scope statement.
-->

## Overview and Scope

This repository serves two purposes:

1. A **ready-to-use starter repository** for professional Python projects
2. A **reference guide** for modern Python workflows

It demonstrates a professional Python project structure, tooling configuration, and documentation practices.

## Documentation Site

This repository includes an associated
[**documentation site**](https://denisecase.github.io/pro-analytics-02/).

## Developers and Maintainers

This is a reference site. Most people do not need to get this running on their machine.
For developers and maintainers (or if you want to fork your own copy).

### Set Up Machine

- Complete 🟢 [Workflow A. Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/) to **set up a machine** for Python development.

### Copy & Open this Project in VS Code

1. Sign in to GitHub, open this repository in your browser, and click **Copy this template** to get a copy in **YOURACCOUNT**.
2. Enable GitHub Pages.

Open a terminal on your machine (not VS Code) in your Repos folder and run:

```shell
git clone https://github.com/YOURACCOUNT/pro-analytics-02

cd pro-analytics-02
code .
```

When VS Code opens, accept the Extension Recommendations (click **`Install All`** or similar when asked).

### Create and Manage the Project Environment

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal** in the root project folder.

To set up a project Python environment (managed by `uv`) and align VS Code with it,
run the following commands, one at a time, hitting ENTER after each:

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

If asked: "We noticed a new environment has been created. Do you want to select it for the workspace folder?" Click **"Yes"**.

If successful, you'll see a new `.venv` folder appear in the root project folder.

Install and run pre-commit checks (twice if necessary as shown below):

```shell
uvx pre-commit install
git add -A
uvx pre-commit run --all-files
```

## Daily Workflow (Working With Python Project Code)

VS Code should have only this project open.
Open a VS Code terminal (menu: `Terminal` / `New Terminal`) and run:

```shell
git pull

uv run python src/pro_analytics_02/demo_module_basics.py
uv run python -m pro_analytics_02.demo_module_basics

uv run ruff format .
uv run ruff check . --fix

uv run pytest --cov=src --cov-report=term-missing

uv run zensical build
uv run zensical serve
```

Hit **CTRL+c** in the VS Code terminal to quit serving.

While editing project code and docs, repeat the commands above to run files, check them, and rebuild docs as needed.

Save progress frequently.
Some tools may make changes;
you may need to **re-run git `add` and `commit`** to ensure everything gets committed before pushing.

```shell
git add -A
git commit -m "update"
git push -u origin main
```

## Tools

Core tools:

- `uv` for dependency management and command execution
- `ruff` for formatting and linting
- `pytest` for test execution
- `zensical` for documentation

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
