# 🔵 Open the Project in VS Code and Install Extensions

> Open the project in VS Code and install extensions (and additional tools as directed).

## 1. Open the Project Workspace

Using that same terminal (or a machine terminal open in **Repos**),
change directory (`cd`) into the repository folder and run **code dot** (`code .`).

The `code .` command opens the **current folder**
as the project workspace in VS Code.

**IMPORTANT:** The command below is just an example.

Use **your exact repository name**, e.g. `cd bintel-01-intro` or `cd datafun-01-intro`:

```shell
cd your-repo
code .
```

<details markdown>

<summary>WHY use **code .**?</summary>

Using **code .** is the strongly recommended professional pattern because it helps ensure:

- the terminal is in the correct directory
- VS Code opens the correct project root
- environment discovery happens relative to that root
- Git commands run in the right repository

Opening the correct project root is especially important
when we need to execute Python files.

</details>

<details markdown>
<summary>Help: `code .` didn't open VS Code</summary>

On Windows, try re-running the installer with `add to path` checked.
You must close and reopen your terminal for it to take effect.

Download the standard installer from the Official Visual Studio Code Download Page.
Run the executable setup file.
Advance through the prompt screens.
Look for the "Select Additional Tasks" screen.
**Check the box** labeled **Add to PATH (requires shell restart)**.
Click next and complete the installation.

</details>

When VS Code opens, it may make **extension recommendations**.

## 2. Install Recommended Extensions

If the project includes a **.vscode/extensions.json** file,
VS Code will automatically recommend extensions for the project.
In that case:

1. Watch for the **Recommended Extensions** popup
2. Click **Install All**

You can also [install extensions manually](../../tools/vscode/extensions.md)
or as VS Code recommends them based on the file types in your projects.

<details markdown>

<summary>Extensions NOT Recommended</summary>

Some extensions are not needed because Ruff handles formatting and linting:

- **ms-python.black-formatter**
- **ms-python.autopep8**

</details>

## 🏞️ ONLY FOR STREAMING DATA: Install Kafka

In the Streaming Data course:

- [Install Kafka](../../kafka/install-kafka.md)
- [Create a Topic for the Project](../../kafka/create-topic.md)

## 🏞️ ONLY FOR BUSINESS INTELLIGENCE: Install Spark

In the Business Intelligence course, Mac and Linux users install Spark.
It is optional (and nice to know) for Windows users.

- [Install Spark](../../spark/index.md)

## Verification

1. I opened the repository root folder as the project workspace in VS Code using **code .**
   and can take a screenshot showing VS Code with only my project open.

2. I installed the recommended VS Code extensions for the project.

3. If I am in Streaming Data, I completed the required Kafka setup.

4. If I am in Business Intelligence, I completed the required Spark setup.

---

[◄ Back to 🔵 Phase 1](index.md)
