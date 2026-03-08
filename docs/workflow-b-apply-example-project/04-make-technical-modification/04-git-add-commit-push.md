# 🔵 Git Add-Commit-Push to GitHub

> Save progress regularly

Use a VS Code terminal (PowerShell, zsh, or bash) opened in the root project folder.

**IMPORTANT:** Replace the commit message
with a clear description of what you added or changed.
Wrap the commit message in double quotes.
See: [How to Write a Good Commit Message](https://chris.beams.io/git-commit)

Save progress frequently.
Some tools may modify files,
so you may need to **re-run** `git add` and `git commit`
to ensure everything is committed before pushing.

```shell
git add -A
git commit -m "update"

git add -A
git commit -m "update"

git push -u origin main
```

The `-u` option tells Git to remember `origin main`
as the upstream branch for future commands.
After running the longer `push` command once,
you can use the shorter version:

```shell
git push
```

<details>

<summary>If pre-commit modifies files or blocks the commit</summary>

This project uses **pre-commit hooks**
that run automatically when you run `git commit`.

Case 1. If pre-commit **modifies files** (for example, formatting),
the commit may stop so you can review the changes.
This is common. Just run the commands again as shown above.

```shell
git add -A
git commit -m "update"
```

Case 2. If pre-commit **reports errors**,
read the messages in the terminal, fix the issue, and try again.

Case 3. If you cannot resolve the issue after reviewing the messages,
you can bypass the checks for that commit using the `--no-verify` flag.

```shell
git commit -m "update" --no-verify
```

</details>
