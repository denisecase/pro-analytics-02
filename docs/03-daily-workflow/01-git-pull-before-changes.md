# 🔵 Git Pull Before Changes

Before making any changes to a project, ALWAYS pull the latest changes from the remote repository on GitHub.
Keep both locations up-to-date, and in sync.

Pulling ensures that:

- You work with the latest code.
- Merge conflicts are minimized.
- Collaboration stays smooth.

## Before Starting

Open your project repository in VS Code.

Open a new terminal in VS Code and run a single command.

## Git Pull

Even if you are the only one working on a project, running `git pull` ensures your local work stays synchronized with GitHub and allows us to make minor changes to our README.md or other files directly in the web interface.
It's a good practice that pays off.

Run the following command from the project root directory.
The command works in PowerShell, bash, zsh, Git Bash, and more.

```shell
git pull origin main
```

Or just `git pull`.

After pulling, review the output for updates or conflicts.
If there are any merge conflicts, resolve them before proceeding.

The best solution to merge conflicts is to **avoid** conflicts through a good workflow - pull first, make changes, git add-commit-push frequently.
