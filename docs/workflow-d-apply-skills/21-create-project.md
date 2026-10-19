# 🟣 Get the Example Running

> Ensure the example still runs in your repository.

## Step 1. Check the Workspace

In the VS Code terminal:

```shell
pwd
git status
```

The pwd command means "print working directory".
The path should end in **your** repository name,
and Git should report your repository.

## Step 2. pyproject.toml

Start here. This file defines the project.

- [ ] Update the project `description` to describe YOUR project.
- [ ] Update any `authors` entry (if provided) to YOUR name.

## Step 3. Configuration and Tooling Files

For example: **.gitignore**, **.vscode/**, and the settings files
for linting, formatting, and type checking.
Most all of these can be used without changes.
They are silent helpers that help catch and avoid errors.

## Step 4. Data and Other Inputs

Start with the data the example uses and make sure the example
runs on the original data first, before making any code or data changes.

## Step 5. Project Code

Code may be found under src/, under notebooks, or elsewhere.
Understand how to find the project code, regardless of the type of example project.

Note the files the project uses.
Note any src/ **package** folder, typically named to be specific to the type of project.

When we change a data source, the code will have to change to reflect
the new data file name (and path).
In addition, the content, columns, attributes, or features likely change as well.

**IMPORTANT:** When adding files, do not commit secrets, private data, or oversized files.

## Step 6. Documentation Site (docs/ and zensical.toml)

In **zensical.toml**:

- [ ] Update the `site_name` and `site_description` as needed.
- [ ] Update repository links, such as
      `site_url`, `repo_url`, `repo_name`, and `social` links.

There are usually at least **four locations to change**.

Update the title, name, and links in **docs/index.md**
and use the docs/ folder to present your project process, results, and insights.

Briefly review the GitHub Actions configured in **.github/workflows/**.

NOTE: Repository Settings / Pages must be set to "GitHub Actions"
(as described earlier).

## Step 7. LICENSE and CITATION.cff

If the project includes a `LICENSE` file:

- [ ] Follow the terms of the license for your derived works.
- [ ] Either delete the file or continue to license the work.
- [ ] If terms allow, set your name as the author or copyright holder.

If the project includes a `CITATION.cff` file:

- [ ] Either delete the file, keep the original and add your name, or replace it.
- [ ] Update `repository-code`.
- [ ] Update `url`.
- [ ] Set your name as author.

Generally, in academic projects,
the intent is for you to use the example and make it your own project.
You can preserve credit (and blame) as you like,
but examples are typically offered as working foundations for your own custom projects.

## Verification

- [ ] pyproject.toml has the project's own name, description, and author,
      and declares every dependency the project uses.
- [ ] Each project code file has the name / alias and year and month at the top.
- [ ] README.md is the version for **your** repository and custom project.
- [ ] Repository and documentation links refer to **your** repository.

---

[◄ Back to 🟣 Workflow D](index.md)
