# 🟢 Windows: Install Tools

This page provides instructions to install or verify **Python**, **Git**, and **Visual Studio Code** on a Windows machine using **official installers**.
These tools are essential for professional data analytics.

## 1. Use Official Installers (Recommended for Most Users)

Download and Install Each Tool:

- **Python**: <https://www.python.org/> YOU MUST check **“Add Python to PATH”** during installation. If you forget, rerun installation with the box checked.
- **Git**: <https://git-scm.com/>
- **VS Code** (Visual Studio Code): <https://code.visualstudio.com/>

Important: Remember to check the box to add Python to your path during installation.
![Important: Add Python to Path](images/windows_add_python_to_path.png)

## 2. Restart Computer After Installation

Restart your computer after installation (optional but recommended).

## 3. Verify

After restarting, open a new PowerShell terminal and run the following commands to verify.

```powershell
py --version
pip --version
git --version
code --version
```

IMPORTANT: Each command should return a version number.
If any fail, revisit the installers and try again.

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Install Advanced Tooling (uv)</code></strong></summary>

These tools are modern, high-performance alternatives to traditional Python tools:

- `uv` replaces `pip` and `venv` with a much faster dependency and environment manager.
- `ruff` replaces `flake8`, `black`, and more with a single ultra-fast linter and formatter.

Install uv globally (once per machine):

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```powershell
uv --version
```

NOTE: These are **not required** for most users.
You'll need `uv` to try the advanced option in the project initialization workflow.
Install `ruff` with each project (later).

</details>

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Install Multiple Versions of Python</strong></summary>

This is not typically needed.
Only do this if you need to run an older version of Python (e.g., for Kafka or Spark).

Use `winget` to install an alternate version:

```powershell
winget install --id Python.Python.3.11.11
```

Note: py --version and python --version and python3 --version may or may not work and may return different versions depending on which order they were installed, system path settings, and more.

We can specify the desired Python version when creating a project virtual environment in the next workflow.

</details>

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Use Package Managers (winget)</strong></summary>

You can also install core tools with `winget`. Open a PowerShell terminal and run the following commands:

```powershell
winget install --id Python.Python.3
winget install --id Git.Git
winget install --id Microsoft.VisualStudioCode
```

Restart your machine and verify installations using the commands shown earlier.

</details>

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Set up WSL (better with tools like Apache Kafka or Apache Spark)</strong></summary>

This section is **required** only if you're using advanced tools like **Apache Kafka** or **Apache Spark**, which may not run reliably on base Windows.
For these tools, use **WSL** (Windows Subsystem for Linux 2) with **Ubuntu**.

You only need to do this setup once. After that, you’ll use WSL for all Kafka/Spark projects.

### Advanced WSL Step 1. Enable WSL and Install Ubuntu Operating System

In an **elevated PowerShell** terminal (right-click / Run as Administrator), run:

```powershell
wsl --install
```

Restart your machine if prompted.


<details> <summary> WSL Trouble? (Expand if needed)</summary>

<hr>

> If wsl does not install, try installing with:

```powershell
wsl --install -d Ubuntu
```

> **Restart** when prompted.

> If you get **virtualization errors**, you may need to reboot and enable virtualization in your BIOS/UEFI.
> On most PCs this is Intel VT-x or AMD-V.
> Look for "Virtualization Technology" and turn it ON.
> Work with your favorite AI assistant for additional help.
> After enabling, **restart** Windows and try again.

<hr>
</details>

### Advanced WSL Step 2. Launch Ubuntu

After reboot, open **Ubuntu** from the Start Menu.

The first time you launch it:

- It will complete installation.
- You'll be asked to create a **username** and **password**.
- This is separate from your Windows account.
- **IMPORTANT: Remember your username and password**.  You can always recreate your WSL, but it helps to be able to return to your WSL installation after some time has passed.


### Advanced WSL Step 3. Update Ubuntu

Run the following commands inside your Ubuntu terminal:

```bash
sudo apt update && sudo apt upgrade -y
```

### Celebrate: Your Advanced WSL Setup is Complete!

You now have:

- A full Linux environment (Ubuntu) inside Windows.

**Use WSL for Apache Kafka/Spark.**
You can still use normal Windows for VS Code, repos, Python, and Python virtual environments.
Just remember to move to WSL when needed, e.g. to run advanced services like Apache Kafka or Apache Spark.

</details>

