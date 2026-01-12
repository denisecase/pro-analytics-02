# 🔵 Git Add, Commit, and Push to GitHub

> How to save progress

## 1. Git add-commit-push

Use a terminal in VS Code (PowerShell, zsh, or bash).

IMPORTANT:
Replace the commit message with a clear and descriptive note about what you added or changed.
Wrap the commit message in double quotes.

Save progress (some tools may make changes; re-running ensures everything is committed):

```shell
git add -A
git commit -m "update"
git add -A
git commit -m "update"
git push -u origin main
```

The `-u` tells git to use the `origin` remote and the `main` branch on upstream (future) commands.

After running the longer `push` command once, the following short version will work:

```shell
git push
```
