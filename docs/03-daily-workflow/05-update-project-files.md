# 🟠 Personalize Common Project Files

Personalize core files common in professional analytics projects.
Especially:

- `pyproject.toml` — defines project metadata, dependencies, and build settings
- `mkdocs.yml` — configures project documentation website (powered by MkDocs)
- `README.md` — explains the project and how to use it

> Note: A required `.gitignore` file is provided in this and most starter repositories. You need to have it, but you typically won't need to edit it.

---

## Before Starting

1. Open your project repository in **VS Code**
2. Confirm your terminal is in the **project root**
3. Verify that `pyproject.toml`, `mkdocs.yml`, and `README.md` are in the root folder (same level as `.gitignore`)

---

## Task 1. Update `pyproject.toml`

The `pyproject.toml` file is the **single source of truth** for your project's dependencies and metadata. Tools like `uv`, `pip`, and VS Code use this file to understand how to install and run your project.

### What it controls

- The project name, version, and description
- The list of required Python packages
- Development-only tools (formatters, linters, testing)
- Build and packaging settings (if you later publish your project)

### Task 1 Actions

1. Open `pyproject.toml` in the root of your repo
2. Update:
   - `name` to use your project's top-level package name
   - `dependencies` to include only the packages you actually need
   - Any **URLs** - replace starter GitHub links with those to your project

---

## Task 2. Update `mkdocs.yml`

MkDocs is configured by the `mkdocs.yml` file in the root.
MkDocs builds the project **documentation site** from the `docs/` folder.
The `mkdocs.yml` file controls your site navigation, theme settings, and page structure.

### What it controls

- The site title
- Which pages appear in the navigation
- Markdown extensions, themes, and organization

### Task 2 Actions

1. Open `mkdocs.yml` and update:
   - The `site_name` field
   - Navigation entries if needed
2. Edit pages in the `docs/` folder (especially `index.md`) to match your project

---

## Task 3. Update `README.md`

Your README is the **entry point to your project**.
It should provide enough information for a new user to understand, set up, and run your project.

### A good README includes:

- What does this project do
- How do I set it up
- How do I run it
- Where are the docs, notebooks, and report
- Display key visuals and insights.

### Task 3 Actions

- Update the README from the beginning (don't leave it as a placeholder)
- Replace any references to the starter repo or starter GitHub account

---

## Task 4. (Optional) Review Other Project Files

Your starter repository includes additional files for code quality, automation, and documentation. You generally won't edit them now, but you should know they exist.

### Task 4 Actions

- Skim these files so you know what they are for
- Modify them only if your project requires customization later

## Task 5. Git add-commit-push to GitHub

Save progress (some tools may make changes; re-running ensures everything is committed):

```shell
git add -A
git commit -m "update"
git add -A
git commit -m "update"
git push -u origin main
```
---

After this initial effort, your project will have a professional foundation.
