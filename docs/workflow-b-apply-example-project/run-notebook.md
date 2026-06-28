# 🔵 Run Jupyter Notebooks

This page explains how to run Jupyter notebooks in VS Code.

When we execute code in a Jupyter notebook,
the kernel runs the code interactively,
allowing us to test, visualize,
and document our analysis step by step.

A notebook is a web-based interactive environment commonly
used for exploratory data analysis (EDA) and more.

<details>
<summary>WHY?</summary>

Jupyter notebooks are commonly used for exploratory data analysis because
code, results, charts, and notes can **appear together** in one document.

Notebooks are useful when analysis is being explored step by step, when
intermediate results need to be inspected, or when charts and explanations
are part of the work.

Use notebooks when the project includes `.ipynb` files and the work benefits
from combined presentation, calculation, visualization, and notes.

</details>

## Important Note

Use this only when your project uses **Jupyter notebook (`.ipynb`)** files.

## Before Starting

Open your project repository folder in VS Code.
Ensure the `.venv` is activated. If it is already active, you don't need to reactivate it.

We must have installed all the external dependencies into the environment first.

### Install the Jupyter Extension for VS Code

- Open the Extensions view in VS Code by pressing Ctrl+Shift+X (Windows/Linux) or Cmd+Shift+X (Mac).
- Search for "Jupyter" and install the official extension.

### Open the Notebook in VS Code

Open the notebook in VS Code. The file will have a .ipynb extension.

## Task 1. Select Notebook Kernel

1. Open the notebook (`.ipynb`) file in VS Code.
2. If prompted, select a **Python interpreter** that corresponds to your project’s `.venv`.
3. If not prompted:
   - Click the **Kernel Selector** in the top-right corner.
   - Choose the interpreter labeled with your project name and path.
   - Or open the Command Palette (`Ctrl Shift P` / `Cmd Shift P`)
     and run: **Python: Select Interpreter**, then pick your `.venv`.

## Task 2. Start and Run the Notebook

Run notebooks directly in VS Code.

- Click on a cell and press:
  - **Shift Enter** to run cell and move to next
  - **Ctrl Enter** to run cell and stay in place
- Save often or enable **File / Auto Save**.

## Tips: Working with Notebooks

### How to Copy a Notebook

1. In the VS Code Explorer panel, right-click the notebook file (`.ipynb`) and select **Copy**.
2. Right-click the `notebooks/` folder and select **Paste**.
3. Right-click the pasted file and select **Rename**.
4. Replace `_case` with your alias, for example `ml_stellar_analytics.ipynb`.
5. Open your renamed notebook and select your kernel before running.

### If a Notebook Gets Stuck

If Run All disappears and only Interrupt is available:

1. Wait briefly. Some cells (package imports, dataset downloads) take a few seconds on first run.
2. Click **Interrupt** to stop execution, then **Run All** again.
3. Restart the Kernel (Kernel menu or Command Palette).
4. View / Command Palette / **Developer: Reload Window**.

### If You Can't Delete project.log

The notebook kernel may hold a log file open.
Open the notebook in VS Code and click **Restart** on the kernel,
then try again to delete the log file.

### AS-NEEDED: Restart the Kernel

You may need to exit the notebook and
restart the kernel periodically for best results.
As needed, reopen, and restart the kernel.
Run all again to verify.

### AS-NEEDED: Add New External Dependencies

If you want to add any new external packages,
add them to pyproject.toml and follow the steps
to install and upgrade the full set of dependencies.

### AS-NEEDED: If `.venv` packages (e.g., `pandas`) are not recognized

1. Create a `.vscode` folder in the new project (if it doesn't exist).
2. Add a `settings.json` file.
3. Copy the full content from an example `.vscode/settings.json`
4. Close and reopen the notebook.
5. Verify or set the kernel as needed.

## ALWAYS: Fully Execute Notebooks before add-commit-push

Keep your notebooks organized and execute them fully before running git add-commit-push to GitHub.

## Experience

- Understand the role of a Jupyter kernel.
- Understand how to select and verify that the kernel
  and environment match to ensure all dependencies are correctly available.
- Learn Markdown to make professional notebooks.
- Use exactly one top-level title.
- Use numbered second-level headings to organize your work.
- Document your process and steps in the notebook and tell a story with data.
