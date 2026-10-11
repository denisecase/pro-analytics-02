# 🟠 Create Project

> Create the key project files.

## Previously

This assumes your repository is cloned and open in VS Code,
and that it contains the README.md you drafted.
GitHub may also have created files such as **.gitignore** or **LICENSE**.

If an example project exists, it is available on your machine as a reference.
If not, you create each file from scratch.

## How This Page Works

You own the **pyproject.toml** and the shape of the repository.
Copy and modify as you like, but you manage both.

Creating the project **one file at a time** is intended.
Opening each file means reading it,
and each file leaves your hands marked as yours.

For **each file**, follow this pattern:

1. If an example exists, open its file for reference.
2. Create the file in your repository (copy and modify it, or write it).
3. Read it. Change what is specific to the example.
   In a project without an example, confirm every line fits your project.
4. Add your name or alias and the year and month at the top.
5. Save.

The header is one comment line, for example:

```toml
# Your Name or Alias, YYYY-MM
```

Use the comment style of the file type (`#` for Python, TOML, and YAML).
In a Python file, place it after any first `#!` line.

Files that cannot hold comments (such as JSON and CSV) are exempt.

**IMPORTANT:** When copying from an example, do not copy:

- **.git** (the example's Git history)
- **.venv**
- caches and other generated files

If the example's project instructions list files to copy, follow that list.

## Step 1. Check the Workspace

In the VS Code terminal:

```shell
pwd
git status
```

The path should end in **your** repository name,
and Git should report your repository.

## Step 2. pyproject.toml

Start here. This file defines the project.

- [ ] Update the project `name` and `description` to describe YOUR project.
- [ ] Update the `authors` entry to YOUR name.
- [ ] Update repository and documentation URLs
      (such as `Homepage`, `Repository`, and any `project.urls` links).
- [ ] Declare every dependency the project uses.
- [ ] Add the header.

Names chosen here carry into the source code in Step 4.
Keep them consistent.

## Step 3. Configuration and Tooling Files

For example: **.gitignore**, **.vscode/**, and the settings files
for linting, formatting, and type checking.

Apply the pattern to each file.

If GitHub already created a file (such as **.gitignore**),
compare it to the example's version and keep what the project needs.
The **.gitignore** must keep **.venv** and caches out of Git.

## Step 4. Source Code (src/)

Create the package folder, named for YOUR project.

Bring only the files the project uses.
Apply the pattern to each Python file.
Update imports and any references to the example's name.

## Step 5. Tests (tests/)

Apply the pattern to each test file.
Update imports and any references to the example's name.

## Step 6. Data and Other Inputs

Bring the data the project uses so the project can run.
If an example exists, start with the data it uses.

**IMPORTANT:** Do not commit secrets, private data, or oversized files.

## Step 7. Documentation Site (docs/ and zensical.toml)

In **zensical.toml**:

- [ ] Update the `site_name` and `site_description` as needed.
- [ ] Update repository links, such as
      `site_url`, `repo_url`, `repo_name`, and `social` links.

There are usually at least four locations to change.

Update the title, name, and links in **docs/index.md**.
The full story is written in Phase 4.

Update any names and repository references in **.github/workflows/**.

NOTE: Repository Settings / Pages must be set to "GitHub Actions"
(as described earlier).

## Step 8. LICENSE and CITATION.cff

Without an example, keep the LICENSE GitHub created or choose another.
CITATION.cff is optional.

The items below apply when the project started from an example.

If the project includes a `LICENSE` file:

- [ ] Follow the terms of the license for your derived works.
- [ ] Either delete the file or continue to license the work.
- [ ] If terms allow, set your name as the author or copyright holder.

If the project includes a `CITATION.cff` file:

- [ ] Either delete the file, keep the original and add your name, or replace it.
- [ ] Update `repository-code`.
- [ ] Update `url`.
- [ ] Set your name as author.

Generally, in academic projects, the intent is for you to use it and make it yours.
You can preserve credit (and blame) as you like,
but the intent is typically for you to use it as a foundation for your own custom projects.

## Step 9. Check for Leftovers

If an example was used, search for the example's name.
Use the real name of the example repository.

```shell
git grep -n --untracked "example-repo-name"
```

The only results left should be places where you intentionally
credit the example.

Then check what Git sees:

```shell
git status
```

Only files the project uses should be listed.

## Verification

- [ ] pyproject.toml has the project's own name, description, and author,
      and declares every dependency the project uses.
- [ ] Each adapted file has the name or alias and year and month at the top
      (files that cannot hold comments are exempt).
- [ ] The repository contains only files the project uses,
      with no .git, .venv, caches, or generated files
      (including any copied from an example).
- [ ] No unintended references to the example's name remain
      (when an example was used).
- [ ] README.md is the version drafted for this repository, not any example.
- [ ] Repository and documentation links refer to this repository,
      not the example's.
- [ ] No unintended references to the example's name remain.

---

[◄ Back to 🟠 Workflow C](index.md)
