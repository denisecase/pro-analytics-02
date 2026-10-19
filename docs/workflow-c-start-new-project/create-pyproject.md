# 🟠 Take Ownership of pyproject.toml

<!-- On a page that could be read aloud,
use two asterisks instead of backticks
for code. -->

> The **pyproject.toml** file defines the project's identity,
> Python requirements, dependencies, and development tool settings.
> Update the description to reflect your planned project.

Your project repository should be open in VS Code.

## Step 1. Briefly Review the Configuration Files

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
These are mostly silent helpers and don't need to be altered.

For additional information, see
[pyproject.toml](https://denisecase.github.io/pro-analytics-02/reference/python/pyproject/).

## Step 2. Customize pyproject.toml Description and Version

Open **pyproject.toml** and review its sections.

### Update Project Identity Description and Version

- **description** - describe your project and what will make it unique.
- **version** - set this initial version of your project to something like 0.1.0.

### Briefly Confirm Project Identity that Doesn't Change

- **name** - confirm this still shows your repo name (it should not need changing).
- **requires-python** - this should retain the example's Python version

### Briefly Review Dependencies

- Review the packages listed in **dependencies**.
- Review the development and documentation dependency groups.
- Keep packages needed by the project.
- You can always add packages as you work.

### Briefly Review Tool Configuration

Optional: If you like, you can review the existing settings for:

- **pytest** - testing and coverage.
- **Ruff** - linting and formatting.
- **ty** - type checking, if configured.
- **marimo** - reactive Python applications, if used.
- **uv** - dependency and environment management.
- **Build system** - Python package discovery and packaging.

Most should not need to be changed from the example.

## Verification

- [ ] **pyproject.toml** exists in the project root.
- [ ] The project identity **description** and **version\*** reflects your custom project.
- [ ] Dependencies and Python requirements have been reviewed.
- [ ] Ensure your changes are saved.

---

[◄ Back to 🟠 Workflow C](index.md)
