# 🔵 Clone the Example Repository to Your Machine

Cloning a repo means copying the repository to a location on your local machine.

## 1. Copy the Web Address (URL) of the GitHub Repository

View the example GitHub repository in your web browser.
Click once in the browser's **address bar** to
highlight the entire URL,
then **CTRL c** (Mac: **CMD c**) to copy it.

## 2. Clone the Repository to Your Local Machine

Open a **machine terminal** in the folder where you keep your GitHub repositories
(for example **C:\Repos** on Windows or **~/Repos** on Mac/Linux).
If you don't have a **Repos** folder,
see instructions in "Workflow A: Set Up a Machine".

- On Mac/Linux, use the default **Terminal** (zsh or bash).
- On Windows, use **PowerShell** or **PowerShell Core**.
  Do NOT use the older Command Prompt for these instructions.

In the terminal:

1. Type **git clone**
2. Press the **space bar once**
3. Use **CTRL v** (or **CMD v**) to paste the URL to your GitHub repository
4. Press **Enter** (or **Return**) to run the command

**IMPORTANT:** The command below is just an example.
The exact command you need will be shown in the **project README.md**.

Windows: From a machine terminal on your local machine:

```shell
cd C:\Repos
git clone https://github.com/denisecase/datafun-01-foundations
```

Mac/Linux: From a machine terminal on your local machine:

```shell
cd ~/Repos
git clone https://github.com/denisecase/datafun-01-foundations
```

## Verification

- I opened a terminal on my local machine.
- I changed directory to my `Repos` folder.
- A new folder (with the repository name, e.g. `datafun-01-foundations`) appears in my current directory (e.g. the `Repos` directory).
- The terminal shows no error messages about authentication or repository not found.

---

[◄ Back to 🔵 Phase 1](index.md)
