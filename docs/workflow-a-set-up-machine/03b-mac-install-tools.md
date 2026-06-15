# 🟢 macOS: Install Tools

> Installation instructions for required tools on macOS.

Always follow the vendor-recommended installers.

These tools are essential for professional data analytics.

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

Git is often already installed on macOS.

To check, open **Terminal** and run:

```zsh
git --version
```

If Git is missing or outdated, install it from the official site:
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

After installation:

- Move **Visual Studio Code.app** to the **Applications** folder
- (Recommended) Enable the `code` command in Terminal by following:
  <https://code.visualstudio.com/docs/setup/mac>

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

Follow the official installation instructions from Astral:
<https://docs.astral.sh/uv/getting-started/installation/>

> Note: Python is **not** installed at this step.
> Python will be installed per-project using `uv`, which also manages versions

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
for macOS:
<https://nodejs.org/en/download>

<details>
<summary>WHY?</summary>

Node.js provides `npm` and `npx`.
Many helpful professional tools can be run with `npx`.

</details>

## Verify

After installation, open a new Terminal window and run:

```zsh
git --version
code --version
uv --version
npx --version
```

Each command should display a version number.
If any command fails, revisit the corresponding installer.
