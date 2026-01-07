# 🟢 Configure Git with Name and Email

After installing Git, configure the global user.name and user.email.

##  Open VS Code

Open your VS Code editor. We'll use the terminal available in VS Code.

## Open a New Terminal

Use the VS Code menu to select `Terminal` >  `New Terminal`.
Opening a new terminal ensures the terminal knows about recently installed git.

## Important: Know Your Terminal Type

If Windows, always use a terminal type of `PowerShell` (powershell) or `PowerShell Core` (pwsh).
Do NOT use Command Prompt - it is deprecated.

If Mac/Linux, use the default terminal (typically `zsh` or `bash`).

Configure your git user.name and user.email.
Use YOUR name and email in the commands below.
Use the same email you used for GitHub.
School emails may be temporary - you may wish to use a more permanent email.
Change these commands to use your information instead.
Run one command at a time and hit ENTER or RETURN after each line to execute it.

```shell
git config --global user.name "Your Name"
git config --global user.email youremail@example.com
```

## Verify

Verify that the last command correctly shows your user.name and user.email.
If not, repeat the installation and configuration until successful.

```shell
git config --global user.name
git config --global user.email
```
