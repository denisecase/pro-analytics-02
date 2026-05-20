# 🟢 Linux: Install Tools

> Installation instructions for required tools on Linux systems.

Linux distributions vary, so follow the
vendor-recommended steps for your system.

<details>
<summary>WHY?</summary>

Professional analytics projects depend on local tools for running code,
managing packages, checking quality, and working with GitHub repositories.

Installing the required tools creates a consistent project environment
across machines and operating systems.

Correct tool installation reduces setup errors and makes later project
commands more predictable.

</details>

## Required Tools

### Git

Most Linux distributions include Git in their package manager.

Official instructions:
<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>

<details>
<summary>WHY?</summary>

Git **tracks changes** in project files over time.

It records what changed, when it changed, and who made the change.

Git is used with GitHub, but they are different.

- **Git is version control software** that runs on a machine.
- **GitHub is a cloud platform** that stores Git projects online.

</details>

### Visual Studio Code

Follow Microsoft's official Linux setup instructions
for your distribution:
<https://code.visualstudio.com/docs/setup/linux>

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

### uv (Python environment and dependency manager)

Follow the official installation instructions from Astral:
<https://docs.astral.sh/uv/getting-started/installation/>

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

## Verify

After installation, open a terminal and run:

```bash
git --version
code --version
uv --version
```
