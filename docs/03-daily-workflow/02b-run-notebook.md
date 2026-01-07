# 🔵 Run Jupyter Notebooks

This page explains how to run Jupyter notebooks in VS Code. When we execute code in a Jupyter notebook, the kernel runs the code interactively, allowing us to test, visualize, and document our analysis step by step.

A notebook is a web-based interactive environment commonly used for exploratory data analysis (EDA) and more.

## Important Note

Use this only when your project uses **Jupyter notebook (`.ipynb`)** files.


## Before Starting

Open your project repository folder in VS Code.
Ensure the `.venv` is activated. If it is already active, you don't need to reactivate it.

We must have installed all the external dependencies needed for our project to run into the virtual environment first.

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

Alternative if you prefer JupyterLab to VS Code, open a terminal on your machine in the project folder and start JupyterLab:

```shell
uv run jupyter lab
```

## AS-NEEDED: If `.venv` packages (e.g., `pandas`) are not recognized

1. Create a `.vscode` folder in your project.
2. Add a `settings.json` file.
3. Copy the full content from your example `.vscode/settings.json`
4. Close and reopen your notebook.
5. Activate the `.venv` environment.
6. Verify or set the kernel as needed.

## AS-NEEDED: Restart

You may need to exit the notebook and restart the kernel periodically for best results. As needed, reopen, and restart the kernel.
Run all again to verify.

## AS-NEEDED: New External Dependencies

If any new external dependencies have been added to any Python files, follow steps to install dependencies again first.

## ALWAYS: Fully Execute Notebooks before add-commit-push

Keep your notebooks organized and execute them fully before running git add-commit-push to GitHub.

## Experience

- Understand the role of a Jupyter kernel.
- Understand how to select and verify that the kernel and environment match to ensure all dependencies are correctly available.
- Learn Markdown to make professional notebooks.
- Use exactly one top-level title.
- Use numbered second-level headings to organize your work.
- Document your process and steps in the notebook and tell a story with data.
