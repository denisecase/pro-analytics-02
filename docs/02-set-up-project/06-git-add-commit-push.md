# 🔵 Git Add, Commit, and Push to GitHub

This page provides instructions to add files to version control, commit changes, and push them to your remote repository.

- git add - stages changes, adds files to source control
- git commit - creates a labeled snapshot of staged changes.
- git push - updates the remote repository

## Before Starting

Ensure your project repository is open in VS Code, and you have made useful changes.

## Task 1. Git add-commit-push

Using a terminal in VS Code (PowerShell, zsh, or bash).

IMPORTANT:
Replace the commit message with a clear and descriptive note about what you added or changed.
Wrap the commit message in double quotes.

```shell
git add -A
git commit -m "Initial commit"
git push -u origin main
```

After subsequent changes, you may be able to use a simpler version of the last command:

```shell
git push
```
