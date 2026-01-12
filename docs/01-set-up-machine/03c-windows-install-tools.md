# 🟢 Windows: Install Tools

This page provides instructions to install or verify **Git**, **Visual Studio Code**, and **uv** on a Windows machine using official installers. These tools are essential for professional data analytics.

## 1. Use Official Installers (Recommended for Most Users)

Download and install:

- **Git**: https://git-scm.com/
- **VS Code** (Visual Studio Code): https://code.visualstudio.com/
- **uv** (high-performance Python environment and package manager):
  ```powershell
  winget install --id Astral.uv -e
  ```

> Note: We **do not install Python at this step**.
Python will be installed per-project in Workflow 2 using `uv`, which also manages versions.

## 2. Restart Computer After Installation

Restart your computer after installation (optional but recommended).

## 3. Verify

After restarting, open a new PowerShell terminal and run:

```powershell
git --version
code --version
uv --version
```

Each command should display a version.
If any fail, revisit the installers and try again.

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Set up WSL (for Kafka, Spark, or Linux tooling)</strong></summary>

This section is **only for advanced users** who need tools like **Apache Kafka** or **Apache Spark** or want a Linux environment.

### Step 1 - Enable WSL and install Ubuntu

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

Restart if prompted.

### Step 2 - Update Ubuntu

In the Ubuntu terminal:

```bash
sudo apt update && sudo apt upgrade -y
```

You now have a full Linux environment for advanced use cases. Use WSL when running Kafka/Spark, and Windows normally for Python projects.

</details>

---
