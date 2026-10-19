# 🟠 Review and Customize Python Source Code

<!-- On a page that could be read aloud,
use two asterisks instead of backticks
for code. -->

> Understand the Python source code and identify what your project needs.

## Step 1. Review the Source Folder

In VS Code Explorer, open **src/**.

A typical Python project contains a package folder, for example:

```text
src/
    datafun/
        __init__.py
        ...
```

Your project may use a different package name and structure.

Important components include:

- **src/** - contains importable Python source code.
- **Package folder** - groups related Python modules.
- The inclusion of the specially named init file identifies a regular Python package.
- **Python modules** - contain functions, classes, and other program logic.

Some projects may include **app.py** for running an application.

### Repository Names and Python Package Names

GitHub repository names and Python package names follow different conventions.

- **GitHub repositories** may use dashes, such as `datafun-01-foundations-housing`.
- **Python package folders** must use valid Python identifiers, with underscores instead of dashes, such as `src/datafun/`.
- **Python imports** use the package name, such as `from datafun import ...`.

**IMPORTANT:** Keep the Python package name provided in the example.
Changing it requires coordinated updates to imports, tests,
and package configuration in `pyproject.toml`.

See [Project Structure](../reference/python/project-structure.md).

### Identify Your Work

Review the header or docstring in each Python source file.

- Update the author or adapted-by information with your name or alias.
- Retain appropriate credit for the original example code.
- Update descriptions and docstrings as you customize the code.

Your Git commit history will also document the changes you make
throughout the project.

## Step 2. Understand the Source Code

Review the important Python files.

Identify:

1. Where the program starts.
2. How modules import and use other modules.
3. Which functions perform the main work.
4. Where data enters the program.
5. How results are produced or displayed.

Use the working example to understand the program's structure.

## Step 3. Identify What to Customize

Consider your new problem and data.

- Which functions can be reused?
- Which data inputs need to change?
- Which calculations or techniques need to change?
- Which outputs should describe your custom problem?
- What additional functions might be needed?

**IMPORTANT:** Keep the existing Python package name and folder structure
unless you have a specific reason to change them.

Changing the GitHub repository name does not require renaming
Python packages, modules, or imports.

You will progressively implement your custom solution in Workflow D.

## Verification

- [ ] I can locate the Python source code.
- [ ] I can identify the main program entry point.
- [ ] I understand how the main modules and functions work together.
- [ ] I can identify source code that can be reused.
- [ ] I know which parts will need changes for my custom problem.
- [ ] Package names and imports remain consistent.
- [ ] The Python package name and imports remain consistent.
- [ ] Author or adapted-by information identifies my contributions.

---

[◄ Back to 🟠 Workflow C](index.md)
