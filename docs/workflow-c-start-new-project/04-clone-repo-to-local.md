# 🟠 Clone Your Repository To Your Machine

> Copy (clone) your custom GitHub repository to your local machine

## 1. Copy the Web Address (URL) of the GitHub Repository

In your browser, view your GitHub repository.
You should see your account name and the repository name in the browser address bar.

For example, the URL to this repository (in my account) is:
<https://github.com/denisecase/pro-analytics-02>

Verify that you are working with your custom GitHub repository in **your account**.

Use `CTRL a` to select all and `CTRL c` to copy the URL to your clipboard.
On Mac/Linux, use `CMD a` and `CMD c`.

## 2. Clone the Custom Repository to Your Repos Folder

Clone your new repository into your **Repos** folder.

You should have already
[Created a Place for All Projects (Repos/)](../workflow-a-set-up-machine/05-create-repos-folder.md).

### 2.1. Open a Machine Terminal

- On Mac/Linux, use the default **Terminal** (zsh or bash).
- On Windows, use **PowerShell** or **PowerShell Core**.
  Do NOT use the older Command Prompt.

### 2.2. Change to Your Repos Folder

On Windows:

```powershell
cd C:\Repos
pwd
```

On Mac/Linux:

```shell
cd ~/Repos
pwd
```

Verify that the terminal shows your **Repos** folder as the current location.

### 2.3. Clone Your Custom Repository

In the terminal:

1. Type **git clone**
2. Press the **space bar once**.
3. Use **CTRL v** (or **CMD v**) to paste YOUR new repository URL.
4. Press **Enter** (or **Return**) to run the command.

Git creates a new folder inside **Repos** with the name of your new repository.

## 3. Verification

- [ ] I opened a terminal on my local machine.
- [ ] I changed directory to my **Repos** folder.
- [ ] I cloned the repository to my **Repos** folder.
- [ ] My new project has its own folder inside **Repos**.
- [ ] The terminal shows no authentication or repository-not-found errors.

---

[◄ Back to 🟠 Workflow C](index.md)
