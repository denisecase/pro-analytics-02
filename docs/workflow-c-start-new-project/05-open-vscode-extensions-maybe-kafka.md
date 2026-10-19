# 🟠 Open Your Cloned Repository in VS Code (and Install Extensions and Maybe Kafka)

> Open the cloned project repository in VS Code and install extensions.
> 🏞️ ONLY IF STREAMING DATA: Also Install Kafka (Step 3 below)

## Step 1. Open the Project Workspace

Using that same terminal (or a machine terminal open in **Repos**),
change directory (`cd`) into the repository folder and run **code dot** (`code .`).

**IMPORTANT:** The command below is just an example.
You must use **your exact repository name**.

```shell
cd your-repo-name

code .
```

The `code .` command opens the **current folder** as the project workspace in VS Code.

If `code .` doesn't work, you can start VS Code and then use the menu **File** / **Open Folder**,
or use Explorer or File Manager and right-click the repository folder / **Open with VS Code**.

<details markdown>
<summary> Why use code . to open the project?</summary>

We recommend using **code dot** (`code .`) to open
your new repository in VS Code,
because it guarantees:

- the terminal is in the correct directory
- VS Code opens the correct project root
- environment discovery happens relative to that root
- Git commands run in the right repository

</details>

When VS Code opens, it may make extension recommendations.

- If VS Code recommends an extension, it is usually helpful to install it.
- Projects that include `.vscode/extensions.json` can guide extension selections.
- You can add additional extensions later as needed.

## Step 2. Install Recommended Extensions

If the project includes a `.vscode/extensions.json` file,
VS Code will automatically recommend extensions for the project as it opens.
In that case:

1. Watch for the **Recommended Extensions** popup
2. Click **Install All**

If there are no recommendations (or if you are working in a brand new project),
install extensions manually using the steps below.

## Extensions NOT Recommended

Some extensions are not recommended if the example project uses different tooling.

<details markdown>
<summary>OPTIONAL: Adding Extensions Manually</summary>

### 1. Open the Extensions Panel

With the project open in VS Code, choose: **View / Extensions**.
Or use the keyboard shortcut:

- Windows/Linux: `Ctrl + Shift + X`
- macOS: `Cmd + Shift + X`

### 2. Install Extensions

Search for and install extensions in the Extensions panel.
For example:

#### Core Python Extensions

- **Python (ms-python.python)** run, debug, and test Python code
- **Ruff (charliermarsh.ruff)** linting, formatting, and import cleanup
- **ty (astral-sh.ty)** fast type checking

#### Notebook Support

For projects using **marimo** (official name is lowercase):

- **marimo (marimo-team.vscode-marimo)** - edit and run marimo notebooks

For projects using traditional Jupyter notebooks (.ipynb):

- Jupyter (ms-toolsai.jupyter) - edit and run Jupyter notebooks
- Jupyter Keymap (ms-toolsai.jupyter-keymap) - Jupyter keyboard shortcuts
- Jupyter Notebook Renderers (ms-toolsai.jupyter-renderers) - rich output rendering

#### Documentation and Markdown

- **Markdown All in One (yzhang.markdown-all-in-one)** Markdown shortcuts and formatting

#### CSV and Data Files

- **Rainbow CSV (mechatroner.rainbow-csv)** colorized CSV/TSV columns for inspection

#### Configuration and Workflow Files

- **YAML (redhat.vscode-yaml)** YAML schema validation
- **GitHub Actions (github.vscode-github-actions)** syntax highlighting for `.github/workflows`

</details>

## 🏞️ Step 3. ONLY FOR STREAMING DATA: Install Kafka

In the Streaming Data course:

- [Install Kafka](../kafka/install-kafka.md)
- [Create Topic](../kafka/create-topic.md)

---

[◄ Back to 🟠 Workflow C](index.md)
