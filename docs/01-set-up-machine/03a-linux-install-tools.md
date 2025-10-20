# 🟢 Linux: Install Tools

This page provides instructions to install or verify **Git**, **Visual Studio Code**, and **uv** on a **Linux** machine. These tools are essential for professional data analytics.

## 1. Use Built-in Package Manager

Open a terminal and run the following commands:

```bash
sudo apt update
sudo apt install -y git
```

To install VS Code, follow the official instructions to add the Microsoft repository:
https://code.visualstudio.com/docs/setup/linux

Once set up, install VS Code with:

```bash
sudo apt install code
```

Install `uv` (high-performance Python environment and dependency manager):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 2. Restart Computer After Installation

Restart your computer after installation (optional but recommended).

## 3. Verify

After restarting, open a new Terminal and run the following commands to verify.

```bash
git --version
code --version
uv --version
```

IMPORTANT: Each command should return a version number. If any fail, revisit the installers and try again.
