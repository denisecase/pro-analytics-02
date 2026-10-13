# 🔵 Copy The Example Project Repository

Get a copy of the example project.

When using Git, the project typically lives in two places:

- **GitHub** - stores the project online with its version history.
- **Your machine** - provides a local copy for editing, running, and developing the project.

There are two ways to get a copy of the example project:

1. **Copy a Template (Recommended)** - Create your own GitHub repository from the example, then clone it to your machine.
2. **Clone the Example** - Clone the original example directly to your machine.

If the example repository has a **Use this template** button, follow Option 1.
Otherwise, follow Option 2.

## Option 1. Copy a Template (Recommended)

This option is fast and easy.

A GitHub template creates a new repository under your GitHub account
with the example project's files and folders, but with a fresh Git history.

### 1.1. Create Your Example Repository from the Template

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

### 1.2. Copy Your Example Repository URL

1. Open your newly created repository on GitHub.
2. Click the green **Code** button.
3. Select **HTTPS**.
4. Click the copy icon next to the repository URL.

**IMPORTANT:** Copy the URL for YOUR repository under YOUR GitHub account,
not the original example repository.

### 1.3. Clone Your Example Repository to Your Repos Folder

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

## Option 2. Clone the Example Repository

If the example repository does not offer **Use this template**,
you can clone the original example directly.

Cloning copies the repository files and Git history to your local machine.

### 2.1. Copy the Example Repository URL

1. Open the example repository on GitHub.
2. Click the green **Code** button.
3. Select **HTTPS**.
4. Click the copy icon next to the repository URL.

### 2.2. Clone the Example Repository to Your Repos Folder

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

---

## Result

Regardless of which option you followed,
you now have a complete copy of the example project on your machine.

For example:

- Windows: `C:\Repos\datafun-01-foundations`
- Mac/Linux: `~/Repos/datafun-01-foundations`

The local project has the same name and files as the original example.

You are ready to open the project in VS Code,
set up the environment, and run the example.

Later, you will create your own project with a different repository name
and apply the techniques to your own problem.

## Verification

- [ ] I opened a terminal on my local machine.
- [ ] I changed directory to my **Repos** folder.
- [ ] I cloned the repository to my **Repos** folder.
- [ ] A new folder with the exact example repository name appears in my **Repos** folder.
- [ ] The folder contains the example project's files, including **README.md** and **pyproject.toml**.
- [ ] The terminal shows no authentication or repository-not-found errors.
- [ ] I can provide a clickable link to the original example repository.
- [ ] If I used a template, I can also provide a link to my copy on GitHub.

---

[◄ Back to 🔵 Workflow B](index.md)
