# 🔵 Copy The Example Project Repository

Copy and clone the example project down to your machine.

When using Git, the project typically lives in two places:

- **GitHub** - stores the project online with its version history.
- **Your machine** - provides a local copy for editing, running, and developing the project.

If the example repository has a **Use this template** button,
follow these instructions.

## (Recommended) Copy a Template & Clone Your Example Project

This option is fast and easy.

A GitHub template creates a new repository under your GitHub account
with the example project's files and folders, but with a fresh Git history.

### 1. Copy the Template to Get Your Own Example Project

You should be logged into your GitHub account and viewing the example project repository.

1. Click **Use this template** (near the green **Code** button).
2. Select **Create a new repository**.
3. Choose your GitHub account as the **Owner**.
4. **IMPORTANT: Keep the exact same name as the example project.**
5. Select **Public**.
6. Click **Create repository**.

You now have your own GitHub repository containing the example project.

For example:

- Original: `denisecase/datafun-01-foundations`
- Your copy: `YOUR-USERNAME/datafun-01-foundations`

### 2. Copy Your Example Repository URL

1. Open your newly created repository on GitHub.
2. Click the green **Code** button.
3. Select **HTTPS**.
4. Click the copy icon next to the repository URL.

**IMPORTANT:** Copy the URL for YOUR repository under YOUR GitHub account,
not the original example repository.

### 3. Clone Your Example Repository to Your Machine

You should have already
[Created a Place for All Projects (Repos/)](../workflow-a-set-up-machine/05-create-repos-folder.md).

Open a **machine terminal** in your **Repos** folder.

- On Mac/Linux, use the default **Terminal** (zsh or bash).
- On Windows, use **PowerShell** or **PowerShell Core**.
  Do NOT use the older Command Prompt.

In the terminal:

1. Type **git clone**
2. Press the **space bar once**.
3. Use **CTRL v** (or **CMD v**) to paste YOUR repository URL.
4. Press **Enter** (or **Return**) to run the command.

For example, on Windows:

```powershell
cd C:\Repos
git clone https://github.com/YOUR-USERNAME/datafun-01-foundations.git
```

On Mac/Linux:

```shell
cd ~/Repos
git clone https://github.com/YOUR-USERNAME/datafun-01-foundations.git
```

Replace the example URL with the URL copied from your own GitHub repository.

Git creates a local project folder with the same name as the example repository.

---

<details markdown>
<summary> If no template option, then click here.</summary>

If the example repository does not offer **Use this template**,
you can clone the original example directly.

Cloning copies the repository files and Git history to your local machine.

### Copy the Example Repository URL

1. Open the example repository on GitHub.
2. Click the green **Code** button.
3. Select **HTTPS**.
4. Click the copy icon next to the repository URL.

### Clone the Example Repository to Your Machine

You should have already
[Created a Place for All Projects (Repos/)](../workflow-a-set-up-machine/05-create-repos-folder.md).

Open a **machine terminal** in your **Repos** folder.

- On Mac/Linux, use the default **Terminal** (zsh or bash).
- On Windows, use **PowerShell** or **PowerShell Core**.
  Do NOT use the older Command Prompt.

In the terminal:

1. Type **git clone**
2. Press the **space bar once**.
3. Use **CTRL v** (or **CMD v**) to paste the example repository URL.
4. Press **Enter** (or **Return**) to run the command.

For example, on Windows:

```powershell
cd C:\Repos
git clone https://github.com/denisecase/datafun-01-foundations.git
```

On Mac/Linux:

```shell
cd ~/Repos
git clone https://github.com/denisecase/datafun-01-foundations.git
```

**IMPORTANT:** These commands are examples.
Use the URL of the example repository assigned in your course.

Git creates a local project folder with the same name as the example repository.

</details>

---

## Result

You should now have cloned the example project
**to your machine**.

For example, if the example project is named
`datafun-01-foundations`, you should have a new folder
on your machine:

- Windows: `C:\Repos\datafun-01-foundations`
- Mac/Linux: `~/Repos/datafun-01-foundations`

This new folder on your machine will have the same name and files as the original example.

## Verification

- [ ] I can provide a clickable link to the original GitHub example repository.
- [ ] If I used a template, I can provide a link to my GitHub example repository.
- [ ] I opened a terminal on my local machine.
- [ ] I changed directory to my **Repos** folder.
- [ ] I cloned the repository to my **Repos** folder.
- [ ] A new folder with the example repository name appears in my **Repos** folder.
- [ ] The folder contains the example project's files, including **README.md** and **pyproject.toml**.
- [ ] The terminal shows no authentication or repository-not-found errors.

---

[◄ Back to 🔵 Workflow B](index.md)
