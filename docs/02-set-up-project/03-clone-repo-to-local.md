# 🟠 Clone Your Repo Down to Your Machine

This page provides instructions to copy a GitHub repository to a local machine.

## Task 1. Copy the Web Address (URL) of Your GitHub Repository

In your browser, view your GitHub repository.
You should see your account name and the repo name in the browser address bar.
For example, the URL to this repository (in my account) is <https://github.com/denisecase/pro-analytics-01>.

Verify you are working with a GitHub repository in YOUR account.
Use `CTRL a` to select all and `CTRL c` to copy the URL to your clipboard. On Mac/Linux, use `CMD a` and `CMD c`.

## Task 2. Git Clone the Repo to Your Local Machine

Open a terminal where you keep your GitHub repos (e.g. `C:\Repos` or `~/Repos`).
On Mac/Linux, use the default Terminal (e.g. zsh or bash), on Windows, use **PowerShell**. On Windows, do NOT use cmd, the older command Window.

In the terminal, type `git clone` leave a single space and use `CTRL v` (or `CMD v`) to paste the URL to your GitHub repository into the command. Hit Enter or Return to run the command.

The command works in PowerShell, bash, zsh, Git Bash, and more.
**IMPORTANT**: The command below is just an example - you must use **your** GitHub account name and **your exact repository name** for it to work.

```shell
git clone https://github.com/youraccount/yourrepo
```
