# Git Hooks: Automated Quality Checks

Git hooks help catch common problems before changes are committed to a repository.

We use **prek** to set up and run automated checks.
Once installed, the Git hook runs automatically when you use `git commit`.

These checks help maintain consistent, reliable projects across Windows, macOS, and Linux.

## Set Up Git Hooks

From the project root, open a VS Code terminal and run:

```shell
uvx prek install --force
uvx prek update
```

We use **uvx** to run prek so we don't have to
add it to our dependencies in `pyproject.toml` and
install it locally in each project's Python environment (`.venv`).

Git hooks are configured once per local repository.

To run all configured checks manually:

```shell
git add -A
uvx prek run --all-files
```

Some hooks may modify files.
If that happens, review the changes, then re-run (UP ARROW):

```shell
uvx prek run --all-files
```

The checks are defined in the repository's
`prek.toml` file.

## What Happens When You Commit?

When Git hooks are installed, `git commit` automatically runs the configured checks.

- **All checks pass:** Git creates the commit.
- **A check fixes a file:** Review the changes, stage them again, and retry the commit.
- **A check reports an error:** Read the message, correct the problem, and retry.

After making corrections, run:

```shell
git add -A
git commit -m "Describe your changes in quotes"
```

Automated checks reduce the risk of committing mistakes.

## Common Checks

Common checks may include the following.

### A. File Formatting

Keep files consistent across operating systems.

- **trailing-whitespace:** Remove unnecessary spaces at the ends of lines.
- **end-of-file-fixer:** Ensure text files end with a newline.
- **mixed-line-ending:** Normalize line endings to LF.

These checks prevent unnecessary differences when working across Windows, macOS, and Linux.

### B. Configuration File Validation

Catch malformed configuration files before they cause problems.

- **check-json:** Validate JSON syntax.
- **check-toml:** Validate TOML syntax, including `pyproject.toml`.
- **check-yaml:** Validate YAML syntax, including GitHub Actions workflows.

### C. Common Repository Problems

Prevent mistakes that can affect Git history or other developers.

- **check-added-large-files:** Reject newly added files exceeding the configured limit.
- **check-merge-conflict:** Detect unresolved Git merge conflict markers.
- **check-case-conflict:** Detect filenames that differ only by capitalization.

These checks are especially useful when projects are shared across operating systems.

### D. Python Formatting and Linting

Use **Ruff** to maintain consistent Python code and identify common programming mistakes.

- **ruff format:** Format Python code consistently.
- **ruff check --fix:** Identify linting problems and automatically correct supported issues.

Ruff uses the project's `pyproject.toml` configuration.

## Professional Practice

Git hooks provide an early opportunity to identify problems before they reach GitHub.

They help:

- Keep shared repositories consistent.
- Catch configuration and formatting errors.
- Prevent common Git mistakes.
- Reduce avoidable failures in GitHub Actions.
- Develop the habit of reviewing and validating changes before committing.

---

[◄ Back to 🏠 Guide Home](https://denisecase.github.io/pro-analytics-02/)
