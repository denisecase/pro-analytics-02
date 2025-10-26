# 🟢 Configure Git

After installing Git, configure Git to handle notebooks, and set your global `user.name` and `user.email`.

##  Open VS Code

Open your VS Code editor. We'll use the terminal available in VS Code.

## Open a New Terminal

Use the VS Code menu to select `Terminal` >  `New Terminal`.
Opening a new terminal ensures the terminal knows about recently installed git.

- If **Windows**, always use a terminal type of `PowerShell` (powershell) or `PowerShell Core` (pwsh).
Do NOT use Command Prompt, it is deprecated.
- If **Mac/Linux**, use your default terminal (typically `zsh` or `bash`).

## Configure Git

Change these commands to use YOUR name and the same email you used for GitHub.
School emails may be temporary - you may wish to use a more permanent email.
Run one command at a time and hit ENTER or RETURN after each line to execute it.

```shell
uvx nbdime
uvx nbdime --version
uvx nbdime config-git --enable

git config --global user.name "Your Name"
git config --global user.email youremail@example.com
git config --list
```

Verify that the last command correctly shows your user.name and user.email.
If not, repeat the installation and configuration until successful.
