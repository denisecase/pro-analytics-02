# 🟠 Git Hooks

> Install Git hooks and run the checks.

<details markdown>
<summary>WHY?</summary>

Git hooks catch common issues before code is committed and pushed to GitHub.
Once installed, they run the project's automated checks
every time `git commit` is used.

A newly-cloned repository does not include installed hooks,
so install them for each local copy.

</details>

## Step 1. Install the Hooks and Run the Checks

Open a VS Code terminal in the project root folder.
Copy and paste one command at a time, and press **Enter** or **Return** after each:

```shell
uvx prek install --force
uvx prek update

git add -A
uvx prek run --all-files
```

If checks automatically modify files,
**re-run** (try hitting the UP ARROW to repeat a recent command):

```shell
git add -A
uvx prek run --all-files
```

NOTE: We've recently switched to **prek** from the
earlier pre-commit for several reasons.
Prek is written in Rust (like Ruff and ty),
runs hooks in parallel,
and is significantly faster than the Python-based pre-commit framework.

For more information, see
[Git Hooks: Automated Quality Checks](https://denisecase.github.io/pro-analytics-02/tools/github-and-ci/00-git-hooks/).

## Verification

- [ ] `uvx prek install --force` completes without an error
- [ ] `uvx prek run --all-files` finishes with all checks passing

<details markdown>
<summary>If Git hooks cannot be installed</summary>

On some restricted machines, Git hooks may not be permitted.

You can continue working without installing the hooks.
Run the configured checks manually when possible:

```shell
uvx prek run --all-files
```

Required project checks must still pass before work is considered complete.

</details>

<details markdown>
<summary>If checks fail</summary>

Checks may fail on restricted machines where Git hooks cannot be installed.
If this occurs, it is safe to skip them and continue with the project.

</details>

---

[◄ Back to 🟠 Workflow C](index.md)
