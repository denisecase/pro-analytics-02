# 🟠 Clone Repository To Your Machine

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

You should have already
[Created a Place for All Projects (Repos/)](../workflow-a-set-up-machine/05-create-repos-folder.md).

**IMPORTANT:** Clone your new custom repository into your **Repos** folder,
not inside the original example project folder.

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
3. Use **CTRL v** (or **CMD v**) to paste YOUR custom repository URL.
4. Press **Enter** (or **Return**) to run the command.

**IMPORTANT:** The command below is just an example.
Use **your GitHub account name** and **your exact custom repository name**.

```shell
git clone https://github.com/YOUR-USERNAME/datafun-01-foundations-housing.git
```

Git creates a new folder inside **Repos** with the name of your custom repository.

For example, on Windows:

- Original example: `C:\Repos\datafun-01-foundations`
- Your custom project: `C:\Repos\datafun-01-foundations-housing`

Both projects are independent and have their own folders.

## 3. Verification

- [ ] I opened a terminal on my local machine.
- [ ] I changed directory to my **Repos** folder.
- [ ] I cloned the repository to my **Repos** folder.
- [ ] My custom project has its own folder inside **Repos**.
- [ ] My original example project remains unchanged.
- [ ] The terminal shows no authentication or repository-not-found errors.
- [ ] I can provide a link to my custom repository on GitHub.

---

[◄ Back to 🟠 Workflow C](index.md)
