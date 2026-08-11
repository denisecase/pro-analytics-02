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

Git <strong>tracks changes</strong> in project files over time.

It records what changed, when it changed, and who made the change.

Git is used with GitHub, but they are different.

- <strong>Git is version control software</strong> that runs on a machine.
- <strong>GitHub is a cloud platform</strong> that stores Git projects online.

</details>

### 2. Visual Studio Code

Task 2.1. REQUIRED. Download VS Code and follow all instructions in
**Install VS Code on macOS**:
<https://code.visualstudio.com/docs/setup/mac>.

Task 2.2 REQUIRED. Enable the `code` command in Terminal by following
all instructions to
**Launch VS Code from the command line** at:
<https://code.visualstudio.com/docs/setup/mac#_launch-vs-code-from-the-command-line>.

Task 2.3 OPTIONAL. Follow additional instructions including
**After installation** as desired.

<details>
<summary>WHY?</summary>

Visual Studio Code is a <strong>code editor</strong> used to
open, inspect, edit, and run project files.

It provides an integrated <strong>terminal</strong>,
which allows project commands to be run
from inside the same workspace.

The `code` command makes it possible to
open a project folder in VS Code
directly from the terminal.

</details>

### 3. uv (Python environment and dependency manager)

Follow the official installation instructions from Astral:
<https://docs.astral.sh/uv/getting-started/installation/>

> Do not install a project Python separately at this step.
> Python will be installed per-project using `uv`.

<details>
<summary>WHY?</summary>

`uv` manages the Python version and project packages used by a project.

Using `uv` helps each project install the correct Python version and
packages from the project configuration in `pyproject.toml`
and keeps project Python <strong>separate</strong>
from any other Python being used on the machine.

If you worked with older Python projects, you might have used `pip` to
manage required packages and `venv` to manage the virtual environment
kept in the local `.venv` folder.

We moved to `uv` because:

<ul>
  <li>it is fast</li>
  <li>it uses the same commands on Windows, macOS, and Linux</li>
  <li>it creates and updates the local `.venv` project environment</li>
  <li>it can install and manage the Python version for the project</li>
  <li>it reduces the number of separate Python setup tools needed</li>
</ul>

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

```shell
git --version
code --version
uv --version
npx --version
```

Each command should display a version number.
If any command fails, revisit the corresponding installer.
