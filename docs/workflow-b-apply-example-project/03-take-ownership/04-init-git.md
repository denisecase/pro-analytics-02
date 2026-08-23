# 🔵 Initialize Git

Create a new Git history for your project and connect it to your new GitHub repository.

## Initialize and Connect Git

Open a web browser and view the **empty** GitHub repository you just created.

NOTE: If not completely empty, you will get merge conflicts.
Recommendation: delete any initial repo if you added default files and
recreate it **with no default files**.

Copy the HTTPS URL for **your new (empty) GitHub repository**.

In the VS Code terminal, from the project root folder, run:

```shell
git init
git branch -M main
git remote add origin YOUR-NEW-REPOSITORY-URL

git remote -v
```

Replace `YOUR-NEW-REPOSITORY-URL` with the HTTPS URL you copied from GitHub.
Verify that `origin` points to **your new GitHub repository**.

<details markdown>

<summary>Command Explanation</summary>

1. **git init** - creates a new Git history for this project.
2. **git branch -M main** - sets `main` as the primary branch.
3. **git remote add origin URL** - sets **origin** to work as an alias
   for your remote GitHub repository.

## </details>

[◄ Back to 🔵 Phase 2](index.md)
