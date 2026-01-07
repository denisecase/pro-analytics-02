# 🟢 Mac: Install Tools

This page provides instructions to install or verify **Git**, **Visual Studio Code**, and **uv** on a Mac using official installers. These tools are essential for professional data analytics.

## 1. Use Official Installers (Recommended for Most Users)

Download and Install Each Tool:

- **Git** is often already installed. Check with `git --version` in Terminal.
  If it is missing or outdated, install it from: https://git-scm.com/

- **VS Code** (Visual Studio Code): https://code.visualstudio.com/
  After installing:
  - Move the app into the Applications folder
  - (Recommended) Follow instructions at https://code.visualstudio.com/docs/setup/mac to enable `code` from the command line

- **uv** (modern Python environment and dependency manager):
  ```zsh
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

> Note: We **do not install Python at this step**. Python will be installed per-project in Workflow 2 using `uv`, which also manages versions.

## 2. Restart Computer After Installation

Restart your computer after installation (optional but recommended).

## 3. Verify

After restarting, open a new Terminal and run:

```zsh
git --version
code --version
uv --version
```

Each command should display a version. If any fail, revisit the installers and try again.

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Use Package Manager (Homebrew)</strong></summary>

If you prefer Homebrew, open Terminal and run:

```zsh
brew update
brew install git
brew install --cask visual-studio-code
brew install uv
```

Verify installs using the commands in Step 3 above.

</details>
