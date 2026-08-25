# 🔵 Delete the Original Git History

> Now working in your terminal:
> disconnect this project from the example repository.

<details markdown>
<summary>WHY?</summary>

The project you cloned still carries the **example's**
Git history and points at the **example's** repository.

To make this project yours, first remove that
history, then start a fresh one that belongs to you.

Deleting the **.git/** folder does **not** delete your code, notebooks, or data.
It only removes the hidden record of past commits and the link to the example.
All your actual project files stay exactly as they are.

</details>

## 1-Step Instruction

Delete the project **.git/** folder.

You can't see it in VS Code, so open your File Explorer
and find this **exact project**.
Delete the hidden **.git/** folder.
After Workflow A, you should be able to view hidden folders.

For a safer way, using a terminal command see the detailed instructions.

<details markdown>

<summary>Detailed Instructions</summary>

## Before You Start

Start with only the project open in VS Code.
Use the VS Code menu **Terminal / New Terminal** to
open a VS Code terminal in the project root (the default location).

## Step 1. Confirm You Are in the Right Folder

In the VS Code terminal, list the files:

```shell
ls
```

You should see project files such as **pyproject.toml** and **README.md**.

**IMPORTANT:** Only continue if you see these files.
Deleting **.git/** from the
wrong folder could remove history you meant to keep.

## Step 2. Delete the .git/ Folder

The **.git/** folder is hidden,
and even after following the steps in Workflow A,
it probably remains hidden in VS Code.
You can delete it using File Explorer or Explorer,
but it is probably a bit safer to
remove it using the terminal.

### On Windows (PowerShell)

```powershell
Remove-Item -Recurse -Force .git
```

### On Mac/Linux

```shell
rm -rf .git
```

The command produces no output when it succeeds.
That is normal.

## Step 3. Verify

```shell
git status
```

You should see a message like **"not a git repository"**.
That is exactly what you want.
It confirms the example's history is removed.
Your files are still present; only the Git history was removed.

## Success

- [ ] The `.git/** folder in the example project is gone.
- [ ] **git status** reports this is **not** a git repository.
- [ ] Your project files (**src/**, **pyproject.toml**, **README.md**) are still present.

</details>

---

[◄ Back to 🔵 Phase 3](index.md)
