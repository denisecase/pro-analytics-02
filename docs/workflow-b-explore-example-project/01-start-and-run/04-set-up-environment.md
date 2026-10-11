# 🔵 Set up Project Environment (managed by uv)

Each project uses its own Python environment in a **.venv** folder.

The same uv commands work on Windows, macOS, and Linux.

If something breaks, the **.venv** folder can be deleted and recreated.

## Before Starting

Open the project in VS Code using **code .**.

## 1. Open a VS Code Terminal

In VS Code, select **Terminal / New Terminal**.
Verify that the terminal is open in the project root:

```shell
ls
```

You should see files such as:

```text
pyproject.toml
README.md
```

<details markdown>
<summary>If you do NOT see those files (click here)</summary>

Follow the earlier steps carefully.
Continue once you see both `pyproject.toml` and `README.md`.

</details>

## 2. Create or Update the Project Environment

Run the following commands in the VS Code terminal.
Copy and paste one command at a time and hit Enter or Return after pasting to run it.

```shell
uv self update
uv python install
uv lock --upgrade
uv sync
uv audit
```

These commands:

1. Keep `uv` updated. This may not work if uv was installed with a package manager
   such as Homebrew; in that case, update uv with that package manager.
2. Install the Python version pinned by the project (see `.python-version`).
3. Update the project dependency versions allowed by pyproject.toml and
   record the resolved versions in `uv.lock`.
4. Create or update the project `.venv` and install the project dependencies recorded in `uv.lock`.
5. Audit all dependencies for known vulnerabilities and adverse package statuses.

If prompted: "We noticed a new environment has been created.
Do you want to select it for the workspace folder?", click **Yes**.

NOTE: If uv sync completes successfully but reports that it could not hardlink files
and is falling back to copying them, you may continue.
This is a performance warning, not an installation failure.

<details markdown>
<summary>WHY?</summary>

Keeping tools updated is critical for security.
Each powerful tool may pull in many dependency packages.
When a vulnerability is found in a dependency,
a patched version is usually released quickly,
so we teach continuous update habits at school,
where working on the edge is allowed.
In production, updates may need to be more controlled.

</details>

## Important: Environment Verification

Run:

```shell
uv run python --version
uv run python -c "import sys; print(sys.executable)"
```

Verify:

- **.venv/** appears in the project root.
- The commands complete without errors.
- The reported Python executable is inside this project's **.venv** folder.

<details markdown="1">
<summary>If this step fails (click here)</summary>

### If uv command not found

- Close and reopen VS Code.
- Verify **uv** was installed during **Workflow A. Set Up Machine**.

### If Dependency install error

- Delete the **.venv/** folder.
- Rerun: **uv lock --upgrade** and **uv sync**

### If Windows "Smart" Application Control error

If Windows reports: **An Application Control policy has blocked this file.**
or reports that **python.exe** was blocked, see:
[Windows: Smart App Control Blocks python.exe](../../help/04-windows-smart-app-control-python.md)
This is a Windows security-policy issue that happens on some machines.

</details>

## 3. Align VS Code with the Project Environment

### Ensure VS Code uses the project .venv/

1. Open the **Command Palette** (menu: **View** / **Command Palette**, or **Ctrl+Shift+P**)
2. Type and choose: **Python: Select Interpreter**
3. Choose the interpreter inside **this project's **.venv** folder**

![Choose Python: Select Interpreter](./images/Python-Select-Interpreter.png)

![Choose recommended local .venv](./images/Python-Recommended-Local-Dot-venv.png)

### Reload VS Code

1. Open the **Command Palette** (same as before).
2. Type or choose: **Developer: Reload Window**

## Verification

- VS Code uses the Python interpreter inside this project's **.venv/** folder.
- VS Code reloads without warnings about a missing Python environment.

---

[◄ Back to 🔵 Phase 1](index.md)
