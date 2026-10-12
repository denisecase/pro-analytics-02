# Pro Analytics 02: GUIDE to Professional Python

<!-- README opening order

1. Title
2. Project-specific resource badges (NotebookLM, etc.)
3. Standard badges: Docs Site / Python / uv / CI / License / Links / Dependabot
4. One-line positioning statement
5. Hosted documentation link
6. Requirements
7. Developer / Updating the Documentation
8. Resources
9. Citation
10. License
-->

[![NotebookLM: Set Up Machine](https://img.shields.io/badge/NotebookLM-Set%20Up%20Machine-blue?logo=google)](https://notebooklm.google.com/notebook/7a2a6711-9cd0-4f3b-a39a-13f7a361d072)
[![NotebookLM: Explore Example Project](https://img.shields.io/badge/NotebookLM-Explore%20Example%20Project-blue?logo=google)](https://notebook.google.com/notebook/c2de21ca-e973-4a44-9de6-be7ac501eb5d)

[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://denisecase.github.io/pro-analytics-02/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](https://github.com/denisecase/pro-analytics-02/blob/main/pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

[![CI Status](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci-python-zensical.yml)
[![Deploy Docs](https://github.com/denisecase/pro-analytics-02/actions/workflows/deploy-zensical-ga-ai.yml/badge.svg?branch=main)](https://github.com/denisecase/pro-analytics-02/actions/workflows/deploy-zensical-ga-ai.yml)
[![Check Links](https://github.com/denisecase/pro-analytics-02/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/denisecase/pro-analytics-02/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/denisecase/pro-analytics-02/security)

> Reusable professional Python workflows,
> setup guidance, and troubleshooting
> for course and project repositories.

<!--
REQ: Title, badges, and positioning statement appear before anything else.
WHY: README opens with exactly one page title, credibility signals,
then a concise scope statement.
-->

## Professional Python Guide

For best results, consult the detailed instructions in this
[**guide**](https://denisecase.github.io/pro-analytics-02/).
Instructions are provided for all major operating systems and assume no prior experience.

## Overview and Scope

This repository is a
**central reference guide for reusable professional Python workflows**.
Setup instructions, routine development processes, troubleshooting,
rationale, and supporting details are provided here so
individual project repositories can focus on project-specific work.

A professional environment enables more time for the work that matters.

## Requirements

No setup is required to view or use the
[guide](https://denisecase.github.io/pro-analytics-02/).

## Key Files

- `docs/` (folder with Markdown files)
- `zensical.toml` (in the root project folder): scroll to end for the `nav` section.

If curious about the supporting files, see
[this explainer site](https://pup-pack.github.io/professional-python-project-explainer/).

## Developers and Maintainers

This is a reference site.
Most people do not need this running on their machine.
The following steps are for developers and maintainers of this guide.

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.
Follow the guide for the **full instructions**.

### Set Up Machine

- Complete [Workflow A. Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
  to **set up a machine** and create a non-cloud-synced
  `Repos` folder for development.

### Clone and Open in VS Code

Open a machine terminal in your `Repos` folder,
change directory (cd) into the new folder,
and run `code .` to open only this project in VS Code:

```shell
git clone https://github.com/denisecase/pro-analytics-02

cd pro-analytics-02
code .
```

When VS Code opens, accept the Extension Recommendations
(click **`Install All`** or similar when asked).

### Manage Environment

Set up a local project Python environment (managed by `uv`)
and align VS Code with it.

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal**
in the root project folder.
Copy each command, paste into your terminal, and hit ENTER,
to run each command one at a time.

```shell
uv self update
uv python install
uv lock --upgrade
uv sync
uv audit
```

If asked: "We noticed a new environment has been created.
Do you want to select it for the workspace folder?" Click **"Yes"**.
If successful, you'll see a new `.venv` folder appear in the root project folder.

### Install and Run Git Hooks (Automated Checks)

Install and run git hooks (twice if necessary as shown below):

```shell
# set up and run git hooks
uvx prek install --force
uvx prek update

git add -A
uvx prek run --all-files
# repeat if changes were made (UP ARROW)
uvx prek run --all-files
```

### Run Common Chores (Automated Helpers)

Use modern tools to format code, lint code (check for common improvements),
verify correct typing, run tests that verify functions are still
behaving as expected, and build the project docs.

```shell
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Daily Workflow (Working With Python Project Code)

Have only one project open in a VS Code window.
Open a VS Code terminal (menu: `Terminal` / `New Terminal`) and run:

```shell
git pull
```

While editing project code and docs, repeat the commands above to
run files, check them, and rebuild docs as needed.

Save progress frequently.
Some tools may make changes;
you may need to **re-run git `add` and `commit`**
to ensure everything gets committed before pushing.

```shell
git add -A
git commit -m "your message here"

# repeat if changes were made (try the UP ARROW)
git add -A
git commit -m "your message here"

git push -u origin main
```

### Adding Google Analytics Page Views

```text
src/pro_analytics_02/build_analytics.py
    reads the current academic block
    reads the estimated enrollment
    requests all /pro-analytics-02/ page metrics
    writes docs/assets/data/view-analytics.json

docs/javascript/view-analytics.js (added to zensical.toml)
    reads window.location.pathname
    finds that path in view-analytics.json
    inserts the counts at the bottom of the current page
```

[View Current Stats](https://denisecase.github.io/pro-analytics-02/assets/data/view-analytics.json?x=1)

## Optional: Add Google Analytics (Page View Data)

To add page view data, see [SET-UP-GOOGLE-ANALYTICS](./SET-UP-GOOGLE-ANALYTICS.md).

To view generated data, see the published
[view-analytics.json](https://denisecase.github.io/pro-analytics-02/assets/data/view-analytics.json).

## Optional: Add Integrated AI Assistant

To add an integrated AI assistant,
see [SET-UP-INTEGRATED-AI](./SET-UP-INTEGRATED-AI.md).

## Documentation

- [Documentation](https://denisecase.github.io/pro-analytics-02/)

## Annotations

[.annotations/annotations.md](./.annotations/annotations.md)

<!--
WHY: Keep decision rationale close to code and configuration.
-->

## Authority Manifest

[.accountability/surfaces.toml](./.accountability/surfaces.toml)

<!--
WHY: Define the accountable surfaces.
-->

## Citation

[CITATION.cff](./CITATION.cff)

<!--
WHY: Support correct citation and attribution.
-->

## Documentation

[Documentation (The Guide)](https://denisecase.github.io/pro-analytics-02/)

## License

[MIT](./LICENSE)

<!--
WHY: Provide terms of reuse and limits of liability.
-->
