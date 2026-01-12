# 🟢 Open the Project in VS Code (and Install Recommended VS Code Extensions)

> How to Open the cloned project in VS Code and install the recommended extensions.

## Before Starting

This assumes you followed the earlier instruction to clone your repo into the Repos (non-synchronized) folder, e.g.,:
```shell
git clone https://github.com/YOURACCOUNT/pro-analytics-02
```

---

## 1. CD Into Project Folder and Use Code to Open the Project

Using that same terminal, change directory (cd) into the repo folder and run "code dot" as shown below:

```shell
cd pro-analytics-02
code .
```

## 2. Install Recommended Extensions

If you opened a project that already includes
a `.vscode/extensions.json` file
(for example, from this starter repository),
then VS Code will automatically recommend extensions for that project.

In that case:

1. Watch for the "Recommended Extensions" popup
2. Click "Install All"

If there are no recommendations (or if you are working in a brand new project), install extensions manually using the steps below.

## 3. Verify Installation

After installation:

1. Restart VS Code
2. Open the **Extensions** panel again.
3. Confirm the recommended extensions show as **Installed** and **Enabled**.
3. Confirm the extensions are installed and enabled

---

## Recommendations

- If VS Code recommends an extension, it is usually helpful to install it.
- Projects that include `.vscode/extensions.json` can guide extension selections.
- You can add more extensions as needed.

---

## Adding Extensions

### 1. Open the Extensions Marketplace

With the project open in VS Code, from the Menu choose: View / Extensions.
Or Use Keyboard shortcuts:
  - Windows/Linux: `Ctrl+Shift+X`
  - macOS: `Cmd+Shift+X`

This opens the Extensions panel.

### 2. Install Extensions

Search for and install the extensions in the Extensions panel.

For example, you might search for and install the following extensions in the Extensions panel.

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

6. SQLite Tools - choose your favorites
    - SQLite Viewer (by Florian Klampfer)
    - SQLite (by alexcvzz)

### 3. Extensions intentionally not used

These tools are not needed because Ruff handles formatting and linting:

- ms-python.black-formatter
- ms-python.autopep8
