# 🟢 Configure Git

After installing Git, configure Git by setting your global `user.name` and `user.email`.

<details markdown>
<summary>WHY?</summary>

Git records the name and email associated with each saved project change.

This information helps identify who made each change in a project history.

Configuring Git correctly makes local commits match the expected GitHub
identity and keeps project history clear.

</details>

## 1. Open VS Code

Open your VS Code editor. We'll use the terminal available in VS Code.

## 2. Configure Git

### First, Open a NEW VS Code Terminal

Use the VS Code menu to select **Terminal / New Terminal**.

NOTE: You may need to click the three dots to see all menu options.
The VS Code menu starts: File, Edit, Selection, View, and the rest may be hidden behind three dots.
Click the three dots (for more) as needed to expose and click on the **Terminal** menu option,
then click on the **New Terminal** menu option.

<details markdown>
<summary> WHY? </summary>

Opening a new terminal ensures the terminal knows about recently installed Git.

- If **Windows**, always use a terminal type of **PowerShell** (powershell)
  or **PowerShell Core** (pwsh).
  Do NOT use the older Command Prompt.
- If **Mac/Linux**, use your default terminal (typically **zsh** or **bash**).

</details>

### Then, Run the Two Git Configuration Commands

<!-- markdownlint-disable MD034 -->

In the terminal panel that opens at the bottom of VS Code,

- **type** the first command, changing "Your Name" to use YOUR name/alias in quotes,
  and hit ENTER or RETURN, then
- **type** the second command, changing youremail@example.com to the email
  you used for GitHub, and hit ENTER or RETURN.

> NOTE: The **name** (or alias) will be publicly associated with your contributions on GitHub.
> Since GitHub is part of my professional portfolio, I use "Denise Case".
> If anonymity is required (or preferred), choose differently.
> You are never required to use your real name.

```shell
git config --global user.name "Your Name"
git config --global user.email youremail@example.com
```

<!-- markdownlint-enable MD034 -->

## 3. Verify

In the same terminal,

- **copy-and-paste the first command** into the terminal and hit ENTER or RETURN to run it.
- **copy-and-paste the second command** into the terminal and hit ENTER or RETURN to run it.

Verify that they correctly show your user.name and user.email.
If not, repeat the configuration commands using the correct information.

```shell
git config --global user.name
git config --global user.email
```

---

[◄ Back to 🟢 Workflow A](index.md)
