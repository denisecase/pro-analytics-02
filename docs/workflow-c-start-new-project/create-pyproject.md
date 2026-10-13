# 🟠 Customize pyproject.toml

<!-- On a page that could be read aloud,
use two asterisks instead of backticks
for code. -->

> Review the Python project configuration and customize it for your project.

The **pyproject.toml** file defines the project's identity,
Python requirements, dependencies, and development tool settings.

## Previously

Your custom project should be open in VS Code.

## Step 1. Review the Configuration Files

In VS Code Explorer, review the configuration files in your project root.

Common files include:

- **pyproject.toml** - configures the Python project
- **.python-version** - specifies the major Python version
- **prek.toml** - configures git hooks (automated checks)
- **.editorconfig** - configures the editor (so it works the same on all OS)
- **.gitattributes** - configures git file attributes (again for all OS)
- **.gitignore** - tells what not to keep in the project version history
- **.pytest.toml** - configures the test runner that tests project code
- **.ruff.toml** - configures project linting and formatting preferences

Not every project requires every configuration file.

For additional information, see
[pyproject.toml](https://denisecase.github.io/pro-analytics-02/reference/python/pyproject/).

## Step 2. Customize pyproject.toml

Open **pyproject.toml** and review its sections.

### Project Identity

- **name** - update to your custom project name.
- **description** - describe your project, if this field is present.
- **version** - set this initial version of your project to something like 0.1.0.
- **requires-python** - retain the example's Python requirement unless instructed otherwise.

### Dependencies

- Review the packages listed in **dependencies**.
- Review the development and documentation dependency groups.
- Keep packages needed by the project.
- Add packages when needed using **uv add**.

### Tool Configuration

Review the existing settings for:

- **pytest** - testing and coverage.
- **Ruff** - linting and formatting.
- **ty** - type checking, if configured.
- **marimo** - reactive Python applications, if used.
- **uv** - dependency and environment management.
- **Build system** - Python package discovery and packaging.

**IMPORTANT:** The GitHub repository name and internal Python package
name do not need to match.

Keep the existing **src/** package name and its matching
build-system paths unless you intentionally change the package structure.

## Step 3. Review Other Configuration Files

Review the remaining configuration files.

- Keep settings that remain appropriate.
- Update project-specific names, descriptions, and paths.
- Retain existing security and quality checks.
- Do not copy or commit the **.venv/** folder.
- Do not manually edit **uv.lock**. The environment setup will update it.

Avoid changing working configuration without a reason.

## Verification

- [ ] **pyproject.toml** exists in the project root.
- [ ] The project identity reflects your custom project.
- [ ] Dependencies and Python requirements have been reviewed.
- [ ] Package paths match the actual source folders.
- [ ] Configuration files are present where needed.
- [ ] No unintended example-specific configuration remains.
- [ ] Changes are saved. We recommend using VS Code's File / Autosave.

---

[◄ Back to 🟠 Workflow C](index.md)
