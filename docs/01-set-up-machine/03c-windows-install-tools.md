# 🟢 Windows: Install Tools

This page links to official installation instructions for required tools
on Windows. Always follow the vendor-recommended installers.

These tools are essential for professional data analytics.

## Required Tools

### Git

Download and install Git from the official site:
<https://git-scm.com/>

### Visual Studio Code

Download and install Visual Studio Code from:
<https://code.visualstudio.com/>

(Recommended) Enable the `code` command in PowerShell by following:
<https://code.visualstudio.com/docs/setup/windows>

### uv (Python environment and dependency manager)

Install `uv` using the official Windows method:
<https://docs.astral.sh/uv/getting-started/installation/>

Note: Python is **not** installed at this step.
Python will be installed per-project using `uv`, which also manages versions.

## Verify

After installation, open **PowerShell** and run:

```powershell
git --version
code --version
uv --version
```

Each command should display a version number.
If any command fails, revisit the corresponding installer.

<details>
<summary><strong>OPTIONAL/ADVANCED: Windows Subsystem for Linux (WSL) - ONLY AS DIRECTED</strong></summary>

This is only for advanced users who need Linux-only tools
(e.g., Kafka or Spark).

To install WSL, follow Microsoft’s official instructions:
<https://learn.microsoft.com/windows/wsl/install>

Use WSL only when required; it is NOT normally needed
for Python projects managed with `uv`.

</details>
