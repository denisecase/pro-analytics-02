# 🔵 Open the Project in VS Code (and Install Recommended VS Code Extensions)

> Open the project in VS Code and install recommended extensions.

## Strong Recommendation

Using **code dot** (`code .`) as shown below is the strongly recommended professional pattern because it guarantees:

- the terminal is in the correct directory
- VS Code opens the correct project root
- environment discovery happens relative to that root
- Git commands run in the right repository

**IMPORTANT:** Any deviations from this process (especially the first time you open it) will not necessarily work later when we need to execute Python files.

## Previously

This assumes you followed the earlier instructions to clone your repo into the **Repos** (non-synchronized) folder, for example:

```shell
git clone https://github.com/youraccount/your-repo
```

## Step 1. Open the Project Workspace

Using that same terminal (or a machine terminal open in **Repos**),
change directory (`cd`) into the repository folder and run **code dot** (`code .`).


**IMPORTANT:** The command below is just an example.
You must use **your exact repository name**.

```shell
cd your-repo
code .
```

The `code .` command opens the **current folder** as the project workspace in VS Code.

When VS Code opens, it may make extension recommendations.

- If VS Code recommends an extension, it is usually helpful to install it.
- Projects that include `.vscode/extensions.json` can guide extension selections.
- You can add additional extensions later as needed.

## Step 2. Install Recommended Extensions

If the project includes a `.vscode/extensions.json` file,
VS Code will automatically recommend extensions for the project.
In that case:

1. Watch for the **Recommended Extensions** popup
2. Click **Install All**

If there are no recommendations (or if you are working in a brand new project),
install extensions manually using the steps below.

## Extensions NOT Recommended

These extensions are not needed because Ruff handles formatting and linting:

- ms-python.black-formatter
- ms-python.autopep8

## Adding Extensions Manually

### 1. Open the Extensions Panel

With the project open in VS Code, choose:

**View / Extensions**

Or use the keyboard shortcut:

- Windows/Linux: `Ctrl + Shift + X`
- macOS: `Cmd + Shift + X`

### 2. Install Extensions

Search for and install extensions in the Extensions panel.

For example:

#### Core Python Extensions

- **Python (ms-python.python)**  run, debug, and test Python code
- **Pylance (ms-python.vscode-pylance)**  fast IntelliSense and type checking
- **Ruff (charliermarsh.ruff)**  linting, formatting, and import cleanup

#### Notebook Support

- **Jupyter (ms-toolsai.jupyter)**  edit and run Jupyter notebooks
- **Jupyter Keymap (ms-toolsai.jupyter-keymap)**  Jupyter keyboard shortcuts
- **Jupyter Notebook Renderers (ms-toolsai.jupyter-renderers)**  rich output rendering

#### Documentation and Markdown

- **Markdown All in One (yzhang.markdown-all-in-one)**  Markdown shortcuts and formatting

#### CSV and Data Files

- **Rainbow CSV (mechatroner.rainbow-csv)**  colorized CSV/TSV columns for inspection

#### Configuration and Workflow Files

- **YAML (redhat.vscode-yaml)**  YAML schema validation
- **GitHub Actions (github.vscode-github-actions)**  syntax highlighting for `.github/workflows`
