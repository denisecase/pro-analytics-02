# 🟡 Customize The Project

> Inspect the project template and customize it for your new project.

The template provides a working professional Python project structure,
configuration, and development tools.

Before adding your own project code,
review the files provided by the template
and update the project-specific information.

## 1. Update Project Information

Review the project files and replace template-specific information with
information for your project.

Typical updates may include:

- project name
- project description
- author or ownership information
- README content
- example links or repository URLs
- package or module names, if applicable

Do not remove configuration files even if they appear unfamiliar.
The template may include files required for testing, linting, type checking,
documentation, CI, or other project tools.

## 2. Review `pyproject.toml`

Open `pyproject.toml` and review the project configuration.

Update project-specific values such as:

```toml
[project]
name = "your-project-name"
description = "Brief description of your project"
```

Review the dependencies included with the template.

- Keep dependencies needed by the project.
- Remove dependencies that clearly do not apply.
- Add dependencies required for your own work.
- Keep development tools and configuration provided by the template unless
  there is a reason to change them.

After changing dependencies, update the environment:

```bash
uv lock --upgrade
uv sync
```

## 3. Review the Project Structure

Inspect the folders and files supplied by the template.

A project may include items such as:

```text
.github/
.vscode/
docs/
notebooks/
src/
tests/
.python-version
.pre-commit-config.yaml
pyproject.toml
README.md
uv.lock
zensical.toml
```

Use the structure supplied by the template as the starting point for your project.
Not every template includes every item.

## 4. Update the README

Update `README.md` so it describes **your project**, not the original template.
Add additional details as the project develops.
At minimum, make sure the README clearly identifies:

- the project purpose
- the problem or question being addressed
- the primary tools or techniques used
- how to run or explore the project

## 5. Update Project Code and Examples

Review the existing source files, tests, notebooks, and example content.
Make small changes, run the project, and verify that it still works.
Depending on the template, you may need to:

- rename example modules or packages
- replace example analysis with your own work
- update tests
- replace sample datasets
- update notebook content
- update documentation pages

## OPTION: Change the Project Python Version

Template projects should include a `.python-version` file
that specifies the project Python version.

Only change this version when you intentionally want to update
or test the project with a different Python version.

New Python releases may not yet be supported by every project dependency,
especially packages that require compiled binary wheels.
For example, some projects using `scikit-learn`, Spark, Kafka-related tools,
or other compiled or platform-dependent packages may need to remain on
Python 3.14 until their dependencies support a newer version.

You can test with a new version by pinning it while setting up the environment:

```bash
uv python pin 3.15
uv python install
uv lock --upgrade
uv sync
```

After changing the Python version, verify that the project code,
tests, and checks still work correctly.

## Confirm Customizations

Before continuing:

- confirm `README.md` describes your project
- confirm `pyproject.toml` contains the correct project information
- confirm required project files and folders are still present
- run `uv sync`
- run the project
- run the tests and project checks

Continue once the template has been successfully customized
and the project runs without errors.
