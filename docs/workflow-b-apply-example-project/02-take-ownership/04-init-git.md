# 🔵 Initialize Git

Create a new Git history for your project and connect it to your new GitHub repository.

## Intent

1. **Initialize Git** - create a new Git history for this project.
2. **Set the branch to `main`** - use `main` as the primary branch.
3. **Set the remote alias `origin`** - connect this project to your new GitHub repository.

## Initialize and Connect Git

Copy the HTTPS URL for **your new GitHub repository**.

In the VS Code terminal, from the project root folder, run:

```shell
git init
git branch -M main
git remote add origin YOUR-NEW-REPOSITORY-URL
```

Replace `YOUR-NEW-REPOSITORY-URL` with the HTTPS URL you copied from GitHub.

For example:

```shell
git init
git branch -M main
git remote add origin https://github.com/youraccount/your-repo.git
```

## Verify

Run:

```shell
git remote -v
```

Verify that `origin` points to **your new GitHub repository**.

---

[◄ Back to 🔵 Phase 2](index.md)
