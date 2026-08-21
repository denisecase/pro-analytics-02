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

[![NotebookLM: Set Up Machine](https://img.shields.io/badge/NotebookLM-Set%20Up%20Machine-blue?logo=google)](https://notebooklm.google.com/notebook/cb972adf-b31e-455a-804e-76ba39783dc4)
[![NotebookLM: Apply Example Project](https://img.shields.io/badge/NotebookLM-Set%20Up%20Machine-blue?logo=google)](https://notebook.google.com/notebook/c2de21ca-e973-4a44-9de6-be7ac501eb5d)

[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://denisecase.github.io/pro-analytics-02/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](https://github.com/denisecase/pro-analytics-02/blob/main/pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[![CI](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci-python-zensical.yml)
[![Docs](https://github.com/denisecase/pro-analytics-02/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/denisecase/pro-analytics-02/actions/workflows/deploy-zensical.yml)
[![Links](https://github.com/denisecase/pro-analytics-02/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/denisecase/pro-analytics-02/actions/workflows/links.yml)
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

## Audio Guides

Additional interactive materials are provided.
You can listen to **audio summaries**, watch videos, chat with a
specially trained bot, and more.

Note: I found the AI-generated audio podcast to be pretty good.

[![NotebookLM: Set Up Machine](https://img.shields.io/badge/NotebookLM-Set%20Up%20Machine-blue?logo=google)](https://notebooklm.google.com/notebook/cb972adf-b31e-455a-804e-76ba39783dc4)

## Overview and Scope

This repository is a
**central reference guide for reusable professional Python workflows**.
Setup instructions, routine development processes, troubleshooting,
rationale, and supporting details are concentrated here so
individual project repositories can stay focused on project-specific work.
This site is updated somewhat frequently to take advantage of new
advances in tools and practices.
A professional environment enables more time for the work that matters.

## Developers and Maintainers

This is a reference site.
Most people do not need this running on their machine.
The following steps are for developers and maintainers of this guide.

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.
Follow the guide for the **full instructions**.

<details markdown>
<summary>Show command reference</summary>

### Set Up Machine

- Complete [Workflow A. Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
  to **set up a machine** for Python development.

### In a machine terminal (open in your `Repos` folder)

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

### In a VS Code terminal

This project uses `scikit-learn`, so we must stay with Python 3.14.

To set up a local project Python environment (managed by `uv`)
and align VS Code with it, run the following commands.

These are listed for convenience.
For best results, follow the detailed instructions in this guide.

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal**
in the root project folder.
Copy each command, paste into your terminal, and hit ENTER,
to run each command one at a time.

```shell
uv self update
uv python pin 3.14

uv python install
uv lock --upgrade
uv sync
```

If asked: "We noticed a new environment has been created.
Do you want to select it for the workspace folder?" Click **"Yes"**.
If successful, you'll see a new `.venv` folder appear in the root project folder.

Install and run pre-commit checks (twice if necessary as shown below):

```shell
uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made
uv run pre-commit run --all-files
```

### Daily Workflow (Working With Python Project Code)

VS Code should have only this project open.
Open a VS Code terminal (menu: `Terminal` / `New Terminal`) and run:

```shell
git pull

# run the module
uv run python -m pro_analytics_02.demo_module_basics
uv run python -m pro_analytics_02.ml_example

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build
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

</details>

## Helpful Tips

- Use the **UP ARROW** and **DOWN ARROW** in the terminal
  to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Much Can Be Ignored

- You do not need to add to or modify `tests/`.
  Tests are recommended and provided for example only.
- Many files are silent helpers.
  [Explore](https://denisecase.github.io/professional-python-project-explainer/)
  as you like, but most files are never touched.
- You do NOT need to understand everything;
- understanding builds naturally over time.

## As Needed

If VS Code does not automatically use the new `.venv` environment:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Python: Select Interpreter**.
3. Select the interpreter from this project's `.venv` folder.

If VS Code still does not recognize the environment or newly installed tools:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Developer: Reload Window**.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

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

## License

[MIT](./LICENSE)

<!--
WHY: Provide terms of reuse and limits of liability.
-->
