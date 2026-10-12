# 🟠 Create pyproject.toml

<!-- On a page that could be read aloud,
use two asterisks instead of backticks
for code. -->

> Start with the example project's Python configuration file and
> adapt it for your own Python project.

The **pyproject.toml** file defines the project identity,
Python requirements, dependencies, and development tool settings.

Rather than creating this file from scratch,
use the working example as your starting point.

Do not edit the original example project.
Make changes only in your own repository.

## Previously

You should have:

- Created your own GitHub repository.
- Cloned it to your machine.
- Opened your project in VS Code.
- Drafted your README.md.
- Committed and pushed your initial work.

Keep the example project available for reference.

## Step 1. Copy the Configuration Files

From the example project's root, copy these into the root of **your own repository**
(use your file manager; the steps are the same on every operating system):

- **pyproject.toml** - configures the Python project
- **.python-version** - specifies the major Python version
- **prek.toml** - configures git hooks (automated checks)
- **.editorconfig** - configures the editor (so it works the same on all OS)
- **.gitattributes** - configures git file attributes (again for all OS)
- **.gitignore** - tells what not to keep in the project version history
- **.pytest.toml** - configures the test runner that tests project code
- **.ruff.toml** - configures project linting and formatting preferences

IMPORTANT: Do not copy the example's **.venv** folder.

What each file does is described in
[pyproject.toml](https://denisecase.github.io/pro-analytics-02/reference/python/pyproject/).

## Step 2. Create the Package Folder (Keep Same Name as Example)

Create a folder **src/your_package/** (underscores, not hyphens),
where your_package is the src folder name from the example.
Later, with experience, you can vary this folder name (use underscores),
but it will cause a cascading set of issues to debug if you choose to change it.
(Good experience; but we don't recommend you start that process unless you have a fair amount of time).

Inside the projects package folder (the one under src), create or copy
the file named: underscore, underscore init underscore underscore dot py:

```text
__init__.py
```

Add a simple docstring to this file:

```python
"""Project package."""
```

This folder must exist for uv sync to work.

## Step 3. Edit pyproject.toml

- [ ] `name`: your project's name (lowercase, hyphens).
- [ ] `description`: what your project does.
- [ ] `dependencies`: only what your code will use. Add more later with `uv add`.
- [ ] `packages = ["src/your_package"]` and `version-file = "src/your_package/_version.py"`
      both match your folder.
- [ ] `fallback-version`: `"0.1.0"`.

Search the file for the example's name to confirm no example references remain. Save.

## Verification

- [ ] **pyproject.toml**, **.python-version** and **prek.toml** are in the root of your repository.
- [ ] **src/your_package/ has the init file described above.
- [ ] The name, description, and both package paths describe your project.
- [ ] No example name remains in **pyproject.toml**.

## Verification

- [ ] Your own repository is open in VS Code.
- [ ] **pyproject.toml** exists in the root of your repository.
- [ ] The project name has been updated.
- [ ] The description identifies your project.
- [ ] The version has been updated.
- [ ] Author information and URLs are updated where applicable.
- [ ] Dependencies have been reviewed.
- [ ] Package paths and tool settings have been reviewed.
- [ ] No unintended example-specific information remains.
- [ ] Changes are saved.

---

[◄ Back to 🟠 Workflow C](index.md)
