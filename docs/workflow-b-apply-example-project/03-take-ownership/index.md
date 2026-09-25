# 🔵 Take Ownership

> Make the example project yours for experimentation.

<details markdown>
<summary>WHY?</summary>

We typically begin working projects with a similar project.

Use the working example to create an **independent project** with:

- your own Git history,
- your own GitHub repository,
- your name as the project author,
- your own project description,
- your own repository and documentation links.

The original example remains available as a textbook and reference.
Your new repository becomes the custom project to modify and submit.

</details>

## Goal

Disconnect the local project from the example Git repository,
update the project identity,
and publish it as a new repository in your own GitHub account.

## Steps

Part 1. In GitHub (via web browser)

1. [Start in GitHub to Create a New Repository](01-start-in-github.md)
2. [Configure GitHub Repository Settings](02-configure-repo-settings.md)

Part 2. In VS Code Terminal:

<!-- markdownlint-disable MD029 -->

In VS Code, with the example project open,

3. [Delete the original git history (`.git/`)](03-delete-git.md)
4. [Initialize Git](04-init-git.md)
5. [Update project authorship and repository references](05-update-authorship.md)
6. [Run the project](../run-project.md)
7. [Git add-commit-push](07-git-add-commit-push.md)

<!-- markdownlint-enable MD029 -->

## Verification

All commands below are intended to be run in a VS Code terminal open
in the root project folder.

1. I can open the new repository in my GitHub account.

2. I can verify that my local project is connected to my repository:

        git remote -v

   Both the fetch and push URLs point to my GitHub repository.

3. I can verify that the project has its own Git history:

        git log --oneline

   The history begins with the commits for my new project, not the original example history.

4. I can verify that the project identity has been updated:

   - my name appears as the project author where required
   - the project description describes my project
   - repository URLs point to my repository
   - documentation URLs point to my project

5. I can run the project successfully using the command in the README.

6. I can run the standard project checks successfully.

7. I can verify that all changes are committed and pushed:

        git status

   The working tree is clean and the branch is up to date.

8. I can see my latest commits in my GitHub repository.

---

[◄ Back to 🔵 Workflow B](../index.md)
