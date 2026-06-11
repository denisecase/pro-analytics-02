# 🟢 Windows: Install Tools

This page links to official installation instructions for required tools
on Windows. Always follow the vendor-recommended installers.

These tools are essential for professional data analytics.

![slide](https://lh3.googleusercontent.com/notebooklm/AKXwDQE6RFO6UNLwv_KS_JMYeJtRJn6K7LOQj_SrcJ9qgN7bj2M_bm9-tmXD-Cd-m-yJA2yrq0A0U4gVGi1b6FjiqzwY4klAunSWFYTcwFakzH_O1pX_N-oISiatPI7iENw1dmwBzpT2Cpw-H62G-4iXlvIOMjLuOglWv_Hz9a8=w1376-h768?authuser=0)

<details>
<summary>WHY?</summary>

Professional analytics projects depend on local tools for running code,
managing packages, checking quality, and working with GitHub repositories.

Installing the required tools creates a consistent project environment
across machines and operating systems.

Correct tool installation reduces setup errors and makes later
commands predictable.

</details>

## Required Tools

### 1. Git

Download and install Git from the official site:
<https://git-scm.com/>

<details>
<summary>WHY?</summary>

Git **tracks changes** in project files over time.

It records what changed, when it changed, and who made the change.

Git is used with GitHub, but they are different.

- **Git is version control software** that runs on a machine.
- **GitHub is a cloud platform** that stores Git projects online.

</details>

### 2. Visual Studio Code

Download and install Visual Studio Code from:
<https://code.visualstudio.com/>

(Recommended) Enable the `code` command in PowerShell by following:
<https://code.visualstudio.com/docs/setup/windows>

<details>
<summary>WHY?</summary>

Visual Studio Code is a **code editor** used to
open, inspect, edit, and run project files.

It provides an integrated **terminal**,
which allows project commands to be run
from inside the same workspace.

The `code` command makes it possible to
open a project folder in VS Code
directly from the terminal.

</details>

### 3. uv (Python environment and dependency manager)

Install `uv` using the official Windows method:
<https://docs.astral.sh/uv/getting-started/installation/>

Note: Python is **not** installed at this step.
Python will be installed per-project using `uv`, which also manages versions.

![slide](https://lh3.googleusercontent.com/notebooklm/AKXwDQHrKLJMnzbHcw4ZN9yGHpfzm3YqJlUT-j6Sos7GQ-uPB9JVlBBYetRrM9OBy5A85L96fTvLJGgLz-vmyt4Sp6ZPOgNr3cabO5hHg5c7HVFCoq8IOvMSz8Yy0BMt43xYp79KDALXlXLDiHhJ1TIMpgUAGM9e0sHJXmW3mw=w1376-h768?authuser=0)

<details>
<summary>WHY?</summary>

`uv` manages the Python version and project packages used by a project.

Using `uv` helps each project install the correct Python version and
packages from the project configuration in `pyproject.toml`
and keeps project Python **separate** from any other Python being used
on the machine.

If you worked with older Python projects, you might have used `pip` to
manage required packages and `venv` to manage the virtual environment
kept in the local `.venv` folder.

We moved to `uv` because:

- it is fast
- it uses the same commands on Windows, macOS, and Linux
- it creates and updates the local `.venv` project environment
- it can install and manage the Python version for the project
- it reduces the number of separate Python setup tools needed

</details>

### 4. Node.js

Follow the official Node.js installation instructions
for Windows:
<https://nodejs.org/en/download>

<details>
<summary>WHY?</summary>

Node.js provides `npm` and `npx`.
Many helpful professional tools can be run with `npx`.

</details>

## Verify

After installation, open **PowerShell** and run:

```powershell
git --version
code --version
uv --version
npx --version
```

Each command should display a version number.
If any command fails, revisit the corresponding installer.

<details>
<summary>OPTIONAL/ADVANCED: Windows Subsystem for Linux (WSL) - ONLY AS DIRECTED</summary>

This is only for advanced users who need Linux-only tools
(e.g., Kafka or Spark).

To install WSL, follow Microsoft’s official instructions:
<https://learn.microsoft.com/en-us/windows/wsl/install>

Use WSL only when required; it is NOT normally needed
for Python projects managed with `uv`.

</details>

<details>
<summary>OPTIONAL/ADVANCED: WHY WSL?</summary>

WSL provides a Linux environment on Windows.

Some data tools are easier to install and run in Linux than directly in
Windows.

WSL is especially useful when a project requires Linux-based services
such as **Apache Kafka**, **Apache Spark**, or **Apache Flink**.

</details>
