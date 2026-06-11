# 🟢 Linux: Install Tools

> Installation instructions for required tools on Linux systems.

Linux distributions vary, so follow the
vendor-recommended steps for your system.

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

### 2. Visual Studio Code

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

### 3. uv (Python environment and dependency manager)

Follow the official installation instructions from Astral:
<https://docs.astral.sh/uv/getting-started/installation/>

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
for your Linux distribution:
<https://nodejs.org/en/download>

<details>
<summary>WHY?</summary>

Node.js provides `npm` and `npx`.
Many helpful professional tools can be run with `npx`.

</details>

## Verify

After installation, open a terminal and run:

```bash
git --version
code --version
uv --version
npx --version
```
