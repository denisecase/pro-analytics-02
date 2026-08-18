# 🔵 Start & Run

> Phase 1. Clone the example project and run it.

<details markdown>
<summary>WHY?</summary>

Start with a working example.

Before changing anything, confirm that the example project works on your machine.
This is a huge milestone.
Many things have to work together on the machine before getting a Python project to run.

Once the example runs, everything else opens up.

</details>

## Goal

Clone the example repository to your machine,
set up its Python environment,
and run the example successfully.

## Step Summary

1. Open the Example Repository in GitHub
2. Clone the Example Repository To Your Machine
3. [Open the Project in VS Code (and Install Recommended VS Code Extensions and, if Streaming Data, Install Kafka)](03-open-vscode-extensions-maybe-kafka.md)
4. [Set up Project Python Environment (managed by uv)](04-set-up-environment.md)
5. [Run the Project Code](05-run-project.md)

## Step 1. Open the Example Repository in GitHub

Open the example project.
Inspect the example project repository before cloning it
(that is, copying it to your machine).

You should see areas including:

- `src/` - Python source code
- `pyproject.toml` - Python project configuration

## Step 2. Clone the Example Repository to Your Machine

Cloning a repo to a local machine involves the following steps (shown below).

1. Copy the web address (URL) of the GitHub repository
2. Clone the repository down to the local machine
3. Verify

### 2.1. Copy the Web Address (URL) of the GitHub Repository

In your browser, view the example GitHub repository.

Use `CTRL a` to select all and `CTRL c` to copy the URL to your clipboard.
On Mac/Linux, use `CMD a` and `CMD c`.

### 2.2. Clone the Repository to Your Local Machine

Open a **machine terminal** in the folder where you keep your GitHub repositories
(for example `C:\Repos` on Windows or `~/Repos` on Mac/Linux).
If you don't have this `Repos` folder, see the instructions in "Workflow A: Set Up a Machine".

- On Mac/Linux, use the default **Terminal** (zsh or bash).
- On Windows, use **PowerShell** or **PowerShell Core**.
  Do NOT use the older Command Prompt for these instructions.

In the terminal:

1. Type `git clone`
2. Press the **space bar once**
3. Use `CTRL v` (or `CMD v`) to paste the URL to your GitHub repository
4. Press **Enter** (or **Return**) to run the command

**IMPORTANT:** The command below is just an example.
The exact command you need will be shown in the **project README.md**.

```shell
git clone https://github.com/denisecase/datafun-01-foundations
```

### 2.3. Verify

After running the command verify:

- A new folder (with the repository name) appears in your current directory
- The terminal shows no error messages about authentication or repository not found

## Step 2.3. Open the Project in VS Code

Follow:
[Open the Project in VS Code (and Install Recommended VS Code Extensions and maybe Kafka)].

This step includes any course-specific setup for:

- Kafka in Streaming Data projects
- Spark in Business Intelligence projects

Return here when the project is open correctly in VS Code.

## Step 2.4. Set Up the Python Environment

Follow:
[Set up Project Python Environment (managed by uv)](04-set-up-environment.md).

This creates the project's `.venv` and aligns VS Code with the
Python environment required by the example project.

Return here when the environment is ready.

## Step 5. Run the Example

Follow:
[Run the Project Code](05-run-project.md)

Use the exact run command provided in the example project's `README.md`.
The example should run from beginning to end without an error.

## Success

Before continuing, verify:

- [ ] You cloned the correct example repository.
- [ ] You opened only the example project in VS Code.
- [ ] The Python environment (`.venv`) appears.
- [ ] The example runs successfully.
- [ ] The expected output and `project.log` appears.

---

[◄ Back to 🔵 Workflow B](../index.md)
