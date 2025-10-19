# 🟢 Install Recommended VS Code Extensions

This page provides instructions to install common Visual Studio Code (VS Code) extensions for Python development.

## Before You Install

If you opened a project that already includes a `.vscode/extensions.json` file (for example, from a starter repository), then VS Code will automatically recommend extensions for that project.

In that case:

1. Open the project folder in VS Code
2. Look for the "Recommended Extensions" popup
3. Click "Install All"

If there are no recommendations (or if you are working in a brand new project), install extensions manually using the steps below.


## Step 1: Open VS Code

Launch VS Code on your machine.

## Step 2: Open the Extensions Marketplace

Menu path: View > Extensions  
Keyboard shortcuts:  
- Windows/Linux: `Ctrl+Shift+X`  
- macOS: `Cmd+Shift+X`

This opens the Extensions panel.

## Install the Following Extensions

Search for and install the following extensions in the Extensions panel.

## Step 3: Install These Extensions (Manual Method)

Search for and install the following extensions in the Extensions panel.

1. Core Python Extensions
    - Python (ms-python.python) – Run, debug, and test Python code
    - Pylance (ms-python.vscode-pylance) – Fast IntelliSense and type checking
    - Ruff (charliermarsh.ruff) – Linting, formatting, and import cleanup in one tool

2. Notebook Support
    - Jupyter (ms-toolsai.jupyter) – Edit and run Jupyter notebooks in VS Code
    - Jupyter Keymap (ms-toolsai.jupyter-keymap) – Familiar Jupyter keyboard shortcuts
    - Jupyter Notebook Renderers (ms-toolsai.jupyter-renderers) – Rich rendering for plots, HTML, and outputs

3. Documentation and Markdown
    - Markdown All in One (yzhang.markdown-all-in-one) – Shortcuts, formatting, and table of contents

4. CSV and Data Files
    - Rainbow CSV (mechatroner.rainbow-csv) – Colorized CSV/TSV columns for quick inspection

5. Configuration and Workflow Files
    - YAML (redhat.vscode-yaml) – YAML schema validation (useful for configs and CI files)
    - GitHub Actions (github.vscode-github-actions) – Syntax highlighting and validation for `.github/workflows`

6. Formatting and Style (Markdown, JSON, HTML, and general)
    - Prettier (by Prettier)
    - Note: We prefer Ruff formatting for Python files.

7. SQLite Tools
    - SQLite Viewer (by Florian Klampfer)
    - SQLite (by alexcvzz)
  
### Extensions intentionally not used

These tools are not needed because Ruff handles formatting and linting:

- ms-python.black-formatter
- ms-python.autopep8

## Step 4: Verify Installation

After installation:

1. Restart VS Code
2. Open the Extensions panel again
3. Confirm the extensions are installed and enabled

## Notes

- If VS Code recommends an extension, it is usually helpful to install it.
- Projects that include `.vscode/extensions.json` will guide extension selection for you.
- You may add more extensions later based on your needs.
