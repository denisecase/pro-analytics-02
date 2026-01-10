# 🟠 Set up Project Python Environment (managed by uv)

Each project uses its own local virtual environment stored inside the project.
This keeps dependencies isolated, prevents conflicts with system Python, and ensures the project can be reproduced on any machine.
If something breaks, you can safely delete the `.venv` folder and recreate it at any time.

## Before Starting

1. Open your project folder in **VS Code**.
2. Open a default **terminal** inside VS Code:
   - Windows: PowerShell
   - macOS: zsh
   - Linux / WSL: bash
3. Confirm your terminal is located in the **project root directory** (for example, `pro-analytics-02`).

## 1. Set Up the Environment

Run these commands in your VS Code terminal:

```bash
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

This will:

1. Update `uv`
2. Pin the Python version for this repo (and install that version if needed)
3. Install project dependencies listed in `pyproject.toml`.

### 2: Align VS Code with The Environment (.venv)

<mark> **IMPORTANT**:  DO NOT SKIP THIS (or any) STEP</mark>

1. In VS Code, select the project Python interpreter

- Open the Command Palette (View / Command Palette) or hit Ctrl + Shift + p.
- Type and choose: `Python: Select Interpreter`
- Important: Choose the interpreter inside **this project's `.venv` folder**

2. Restart the Python language server

- Open the Command Palette (View / Command Palette) or hit Ctrl + Shift + p.
- Type or choose: `Developer: Reload Window`



## Option: Pin Earlier Python Version (as Needed)

- If a tool like **Apache Kafka** or **Apache Spark** requires an older Python version, specify that version when you pin:

```bash
uv python pin 3.12
uv sync --extra dev --extra docs --upgrade
```
