# 🔵 Clone a Repository To Your Machine

> Copy (clone) a GitHub repository to your local machine

## 1. Copy the Web Address (URL) of the GitHub Repository

In your browser, view your GitHub repository.
You should see your account name and the repository name in the browser address bar.

For example, the URL to this repository (in my account) is:
<https://github.com/denisecase/pro-analytics-02>

Verify that you are working with a GitHub repository in **your account**.

Use `CTRL a` to select all and `CTRL c` to copy the URL to your clipboard.
On Mac/Linux, use `CMD a` and `CMD c`.

## 2. Clone the Repository to Your Local Machine

Open a terminal in the folder where you keep your GitHub repositories
(for example `C:\Repos` on Windows or `~/Repos` on Mac/Linux).
If you don't have this folder, see the instructions in "Workflow A: Set Up a Machine".

On Mac/Linux, use the default **Terminal** (zsh or bash).
On Windows, use **PowerShell**.

In the terminal:

1. Type `git clone`
2. Press the **space bar once**
3. Use `CTRL v` (or `CMD v`) to paste the URL to your GitHub repository
4. Press **Enter** (or **Return**) to run the command

**IMPORTANT:** The command below is just an example.
You must use **your GitHub account name** and **your exact repository name** for it to work.

```shell
git clone https://github.com/youraccount/your-repo
```

## 3. Verify

After running the command:

- A new folder (with the repository name) appears in your current directory
- The terminal shows no error messages about authentication or repository not found
