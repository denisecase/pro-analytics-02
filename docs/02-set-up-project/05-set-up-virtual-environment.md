# 🟠 Set Up Environment (.venv)

Each project uses its own local virtual environment stored inside the repository.
This keeps your dependencies isolated, prevents conflicts with your system Python, and ensures the project can be reproduced on any machine.
If something breaks, you can safely delete the `.venv` folder and recreate it at any time.

## Before Starting

1. Open your project folder in **VS Code**.
2. Open a default **terminal** inside VS Code:
   - Windows: PowerShell
   - macOS: zsh
   - Linux / WSL: bash
3. Confirm your terminal is located in the **project root directory** (for example, `pro-analytics-02`).

## Set Up the Environment

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

### Step 2.4b: Align VS Code with The Environment (.venv)

<mark> **IMPORTANT**:  DO NOT SKIP THIS (or any) STEP</mark>

1. In VS Code, select the project Python interpreter

- Open the Command Palette (View / Command Palette) or hit Ctrl + Shift + p.
- Type and choose: `Python: Select Interpreter`
- Important: Choose the interpreter inside **this project's `.venv` folder**

2. Restart the Python language server

- Open the Command Palette (View / Command Palette) or hit Ctrl + Shift + p.
- Type or choose: `Developer: Reload Window`


## Why We Let `uv` Handle Python Installation

Instead of installing Python globally, we install Python **per project** using `uv`. This approach provides:

| Goal                      | Benefit                                                                            |
| ------------------------- | ---------------------------------------------------------------------------------- |
| **Consistency**           | `uv` manages the environment and the Python version with no OS-specific conflicts. |
| **Reproducibility**       | Pinning Python ensures everyone runs the exact same interpreter version.           |
| **Simplicity**            | Only one tool to install (`uv`), it manages everything else.                       |
| **Isolation**             | Each project has its own `.venv`, avoiding cross-project conflicts.                |
| **Professional Practice** | Matches modern analytics and software-engineering workflows.                       |

## Notes

- Most analytics projects should use the **latest long-term support (LTS)** Python (3.12).
- If a tool like **Apache Kafka** or **Apache Spark** requires an older version, install that version first and update your pin:
  ```bash
  uv python pin 3.11
  ```
- You can always rebuild from scratch by deleting `.venv` and rerunning these commands.

Once created, a project-specific environment provides a reliable, cross-platform base for running and sharing professional analytics code.
