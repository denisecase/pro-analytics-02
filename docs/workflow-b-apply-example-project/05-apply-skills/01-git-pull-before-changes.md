# 🔵 Git Pull Before Changes

Before making any changes to a project, ALWAYS pull the latest changes from the remote repository on GitHub.
Keep both locations up to date and in sync.

Pulling ensures we:

- Work with the latest code
- Minimize merge conflicts
- Keep collaboration smooth

## Before Starting

Open your project repository in VS Code.

Open a new terminal in VS Code and run a single command.

## Git Pull

Even if you are the only one working on a project, running ```shell
git pull
``` ensures your local work stays synchronized with GitHub and allows minor changes to files (such as `README.md`) made in the GitHub web interface to be retrieved.
It's a good practice that pays off.

Run the following command from the **root project folder**.
The command works in PowerShell, bash, zsh, Git Bash, and more.

```shell
git pull origin main
```

Or simply run:

```shell
git pull
```

After pulling, review the output for updates or conflicts.
If there are any merge conflicts, resolve them before proceeding.

The best way to handle merge conflicts is to **avoid them** through good workflow: pull first, make changes, and git add-commit-push frequently.
