# Windows: "Smart" App Control Blocks `python.exe`

## Issue

On some Windows 11 systems, **"Smart" App Control**
may block a Python interpreter managed by `uv`.
The error may include:

```text
An Application Control policy has blocked this file.
```

Windows may display a security notification identifying `python.exe` as the blocked application.
The error occurs when Windows attempts to run the Python interpreter or when:

- creating or updating the project environment
- running `uv sync`
- running a Python script or module
- running a project again after making code changes

## Explanation

`uv` can download and manage the Python version required by a project.
On affected systems, Windows Smart App Control may allow `uv.exe`
to run but block the separate managed `python.exe` executable.
**This is a Windows application-control issue.**

## Solution

Until Microsoft catches up and allows the `uv`-managed Python on all machines,
getting this error requires first **installing Python from Python.org**,
and recreating the project environment with that interpreter.

### Step 1. Install Python

Install the compatible 64-bit Python version from the [official Python website](https://www.python.org/downloads/windows/).
The installed version must satisfy the version required by the project.
The required project version of Python is normally identified in README.md commands and:

```text
.python-version
pyproject.toml
```

IMPORTANT: Close and reopen VS Code after installation.

### Step 2. Find the Installed Python Interpreter

Open a new PowerShell terminal and run:

```powershell
py -0p
```

This lists Python installations registered with the Windows Python launcher.
Locate the path for the required Python version.
Example:

```text
C:\Users\username\AppData\Local\Programs\Python\Python314\python.exe
```

### Step 3. Delete the Existing Project Environment

The existing `.venv` must be removed because it may still reference the blocked interpreter.
From the project repository folder, delete any existing `.venv` either manually or run:

```powershell
if (Test-Path .venv) {
    Remove-Item -Recurse -Force .venv
}
```

### Step 4. Recreate `.venv` with the Installed Python

Replace the example path with the path reported by `py -0p`.

```powershell
uv venv --python "C:\path\to\python.exe"
```

Example:

```powershell
uv venv --python "C:\Users\username\AppData\Local\Programs\Python\Python314\python.exe"
```

### Step 5. Install Dependencies and Verify

Install dependencies using the commands provided and verify
For example:

```powershell
uv lock --upgrade
uv sync --extra dev --extra docs

uv run python --version
uv run python -c "import sys; print(sys.executable)"
```

The reported executable should be located inside the project `.venv` folder.

Example:

```text
C:\path\to\project\.venv\Scripts\python.exe
```

### Step 6. Run Modules As Usual

Run the project using the commands provided in the project instructions.
For example:

```powershell
uv run python -m datafun.app
```

---

## Troubleshooting: If `py -0p` Does Not Work

Run:

```powershell
where.exe python
```

Use the path for the compatible Python installation from `python.org`.
Do not select:

- a Python executable inside the existing project `.venv`
- a Python executable inside the `uv` managed-Python directory
- the Windows Store application alias

## Tell Us When This Occurs

This procedure is only needed when Windows explicitly blocks the `uv`-managed Python interpreter.
A separate Python installation is not required unless Windows Smart App Control blocks the managed interpreter.
Report in your course discussion when you encounter this issue.

## Organization-Managed Computers

On an organization-managed computer,
application installation or execution may be controlled by institutional security policy.
Assistance from the organization’s information technology or security team may be required.

## Python: Kind of Cross-Platform, Kind of Not

The statement that `Python is cross-platform` is true only at the language semantics level.
It is often false at the installation, tooling, and operations level.
Being able to deal with Python environment issues is NOT easy, but it is a valuable skill.
