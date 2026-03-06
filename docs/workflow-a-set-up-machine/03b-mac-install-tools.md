# 🟢 macOS: Install Tools

> Installation instructions for required tools on macOS.

Always follow the vendor-recommended installers.

These tools are essential for professional data analytics.

## Required Tools

### Git

Git is often already installed on macOS.

To check, open **Terminal** and run:

```zsh
git --version
```

If Git is missing or outdated, install it from the official site:
<https://git-scm.com/>

### Visual Studio Code

Download and install Visual Studio Code from:
<https://code.visualstudio.com/>

After installation:

- Move **Visual Studio Code.app** to the **Applications** folder
- (Recommended) Enable the `code` command in Terminal by following:
  https://code.visualstudio.com/docs/setup/mac

### uv (Python environment and dependency manager)

Follow the official installation instructions from Astral:
<https://docs.astral.sh/uv/getting-started/installation/>

> Note: Python is **not** installed at this step.
> Python will be installed per-project using `uv`, which also manages versions.

## Verify

After installation, open a new Terminal window and run:

```zsh
git --version
code --version
uv --version
```

Each command should display a version number.
If any command fails, revisit the corresponding installer.
