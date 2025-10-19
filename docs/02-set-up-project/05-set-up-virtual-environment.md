# 🟠 Set Up Virtual Environment (.venv)

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

## Set Up the Virtual Environment (.venv)

Run these commands in your VS Code terminal:

```bash
# 1. Create an isolated virtual environment
uv venv

# 2. Pin a specific Python version (3.12 recommended)
uv python pin 3.12

# 3. Install all dependencies, including optional dev/docs tools
uv sync --extra dev --extra docs --upgrade

# 4. Enable pre-commit checks so they run automatically on each commit
uv run pre-commit install

# 5. Verify the Python version (should show 3.12.x)
uv run python --version
```

Next, activate the virtual environment. You will typically do this each time you open a new terminal (although with `uv`, VS Code often remembers automatically).

**Windows (PowerShell):**

```bash
.\.venv\Scripts\activate
```

**macOS / Linux / WSL:**

```bash
source .venv/bin/activate
```

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

Once created, a project-specific virtual environment provides a reliable, cross-platform base for running and sharing professional analytics code.
