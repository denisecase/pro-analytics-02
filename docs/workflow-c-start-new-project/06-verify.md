# 🟠 Verify Workflow 02: Set Up Project

> This page verifies that your **Python Project** is correctly set up and aligned with VS Code.

---

## 1. Use Machine Terminal to Open Project with `code .`

On your machine:

1. Open a **machine terminal**.
2. Navigate to your `Repos` folder.
3. Change directory (`cd`) into your project repository folder.
4. Close VS Code if it is open.
5. Open the project using:

```bash
code .
```

## 2. Verify uv and Python Environment

Open the VS Code terminal and run the following commands one at a time:

```bash
uv --version
uv run python --version
```

### Verify

- `uv --version` prints a version number
- `uv run python --version` prints the Python version pinned for this project
- No error messages appear

## 3. Verify Virtual Environment

Look at the VS Code Explorer (left panel).

Verify a `.venv/` folder exists in the project root

Click on a Python file (look in the `src` folder)

Verify VS Code shows `.venv` as the selected Python interpreter.

<details><summary>If the interpreter is not correct:</summary>

- Open the Command Palette (with "View" / "Command Palette")
- Select **Python: Select Interpreter**
- Choose the interpreter inside this project's `.venv` folder
- Reload VS Code (**Developer: Reload Window**)
</details>

## Final Checklist

Your project setup is complete when all are true:

- [ ] VS Code was opened using `code .`
- [ ] VS Code Terminal opens in the project root folder
- [ ] `.venv/` exists in the project
- [ ] `uv run python --version` works
- [ ] the project `venv` appears in the bottom status bar when a Python file is selected

Congratulations - your project environment is ready for work!
