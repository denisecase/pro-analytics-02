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
- 02: Set Up Project (once Per Project)
- 03: Daily Workflow (Working With Python Project Code)

## 01: Set Up Machine (Once Per Machine)

Follow the detailed instructions at:
[**01. Set Up Your Machine**](./docs/01-set-up-machine/index.md).

🛑 Do not continue until all steps are complete and verified.

## 02: Set Up Project (once Per Project)

Follow the detailed instructions at:
[**02. Set Up Your Project**](./docs/02-set-up-project/index.md).

🛑 Do not continue until all steps are complete and verified.

### Step 2.5. Set Up Local Environment

Read about [this step](./docs/02-set-up-project/05-set-up-virtual-environment.md).

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

## 03: Daily Workflow (Working With Python Project Code)

Read about [this workflow](./docs/03-daily-workflow/index.md).

### Step 3.1. Git Pull Before Starting Work

Read about [this step](./docs/03-daily-workflow/01-git-pull-before-changes.md).

```shell
git pull origin main
```

### Step 3.2 Run and Check

Read about [this step](./docs/03-daily-workflow/02-run-and-check.md).

Run Python and/or notebooks as needed for your project.
See [Run Python](02a-run-python.md) or [Run Notebooks](02b-run-notebook.md)


```shell
uv run ruff format .
uv run ruff check . --fix
uv run pytest --cov=src --cov-report=term-missing
```

### Step 3.3. Build and Serve Project Documentation:

Read about [this step](./docs/03-daily-workflow/03-build-serve-docs.md).

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

> To stop a running Python program, press `Ctrl + C` in the terminal

### Step 3.4: Save Progress (add-commit-push)

Read about [this step](./docs/03-daily-workflow/04-git-add-commit-push.md).

```shell
git add -A
git commit -m "update"
git push -u origin main
```


<!--
WHY: Describe the workflow conceptually in README.
-->

## Tooling Notes

This project uses:

- `uv` for dependency management and command execution
- `ruff` for formatting and linting
- `pyright` for static type checking
- `pytest` for test execution
- `mkdocs` for documentation

Alternative tools and stricter configurations are documented inline
and may be enabled intentionally.

<!--
WHY: List tools without turning README into a tutorial.
ALT: Tool choices are opinionated but replaceable.
-->

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


<!--
README STRUCTURE NOTE (HIDDEN)

Level 2 headings (##) define the analytical and operational focus
of a project repository and are often similar across repositories.
Omit sections that do not apply.
Project-specific variations are often expressed at Level 3 or lower.

- Front matter: Title, badges, one-line positioning

| Type    | Level 2 Section            | Questions Answered                  |
| ------- | -------------------------- | ----------------------------------- |
| Core    | Overview and Scope         | What is this analysis? What is it not? |
| Core    | Installation and Setup     | How do I make this analysis runnable? |
| Core    | Usage and Customization    | How do I run or adapt the analysis? |
| Core    | Results / Examples         | What does correct analysis look like? |
| Core    | Documentation              | Where are methods and explanations? |
| Core    | Workflow                   | How does analysis work progress over time? |
| Context | Related                    | What does this analysis connect to? |
| Context | Project Status             | How complete or stable is this work? |
| Context | Security                   | How is data handled responsibly? |
| Context | Annotations                | How were analytic decisions made? |
| Context | Citation                   | How should this work be referenced? |
| Context | License                    | Under what terms can this be reused? |
| Context | SE Manifest                | What is the intent, scope, and role of this project?|
| Context | Acknowledgements           | Who or what contributed? |

NOTE on: Security, Annotations, Citation, License, and SE Manifest:
This repository includes examples of how professional analytics projects
communicate intent, scope, and reuse information.
Students do NOT need to include or create these files in their own projects.

Key principles:
- Prefer pointers over duplication
- Keep sections short and scannable
- Put the most important information first
-->
