# 🟢 Mac: Install Tools

This page provides instructions to install or verify **Python**, **Git**, and **Visual Studio Code** on a Mac using **official installers**.
These tools are essential for professional data analytics.

## 1. Use Official Installers (Recommended for Most Users)

Download and Install Each Tool:

- **Python**: <https://www.python.org/>. Run the downloaded `.pkg` file and follow the installer instructions.
  - IMPORTANT: Finalize your installation by installing certificates. An additional step is shown when installation completes (see the screenshot below). Look for the Python installation in Finder. Find the "Install Certificates" icon, and double-click to run it. This will be required when we add Git - do this now, while the links are available.
- **Git** is often already installed on macOS. You can check by typing `git --version` in the terminal. If it's missing or outdated, install it from: <https://git-scm.com/>.
- **VS Code** (Visual Studio Code): <https://code.visualstudio.com/>. Run the downloaded file, extracting it first if needed.
  - Move the VS Code app into the Applications directory, to make it available via Launchpad.
  - Recommended: Follow the instructions at <https://code.visualstudio.com/docs/setup/mac> to "Launch VS Code from the command line".

## 2. Restart Computer After Installation

Restart your computer after installation (optional but recommended).

## 3. Verify

After restarting, open a new Terminal and run the following commands to verify.

```zsh
python3 --version
pip3 --version
git --version
code --version
```

IMPORTANT: Each command should return a version number.
If any fail, revisit the installers and try again.

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Install Advanced Tooling (uv)</strong></summary>

These tools are modern, high-performance alternatives to traditional Python tools:

- `uv` replaces `pip` and `venv` with a much faster dependency and environment manager.
- `ruff` replaces `flake8`, `black`, and more with a single ultra-fast linter and formatter.

Install uv globally (once per machine):

```zsh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:

```zsh
uv --version
```

NOTE: These are **not required** for most users.
You'll need `uv` to try the advanced option in the project initialization workflow.
Install `ruff` with each project (later).

</details>

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Use Package Managers (Homebrew)</strong></summary>

We can use package managers to install VS Code.
Additional configuration may be need for these options.
To try them, open a terminal and run the following commands:

```zsh
brew update
brew install python
brew install git
brew install --cask visual-studio-code
brew install pyenv
brew install --cask powershell

pyenv --version
pwsh --version
```

Note: The `--cask` option is used for GUI applications like Visual Studio Code and PowerShell.
These apps will appear in Finder, Dock, and Spotlight search, just like other macOS applications.

Restart your machine and verify the installations using the same commands listed above.

</details>

---


<details>
<summary><strong>OPTIONAL/ADVANCED: Install Multiple Versions of Python with <code>pyenv</code></strong></summary>

If you need to add an earlier version of Python (e.g. to use with complex tools such as Kafka or Spark), use pyenv to install additional Python versions like so:

```zsh
pyenv install 3.11.11
```
We can specify the desired Python version when creating a project virtual environment in the next workflow.

</details>

---

## Screenshots

![Python Install Certificates Screenshot](images/mac-python-install-certs.png)

