# prek: Run Git Hook Automated Checks

> prek runs the project's checks (Git hooks) before each commit.

**prek** is a tool that runs a list of automated checks
(called hooks) on project files.
It can run them:

- automatically before every `git commit`
- on demand, whenever you ask
- on GitHub (continuous integration), using the same list

prek is a fast rewrite of a well-known tool named pre-commit,
and it reads the same kind of hook list.
The list is kept in a file named **prek.toml**.

For the commit-time workflow and what each check does, see
[Git Hooks: Automated Quality Checks](github-and-ci/00-git-hooks.md).

## The Commands

```shell
uvx prek install --force
uvx prek update

git add -A
uvx prek run --all-files
```

- uvx runs prek without adding it to your project's dependencies.
- prek install adds a Git hook to this clone,
  so the checks run at every commit. (--force replaces an older hook.)
- prek update moves each hook in prek.toml to its newest version.
- prek run --all-files runs every check on every tracked file.
  Without --all-files, hooks look only at files staged (added) for the commit.
  Run git add -A first so new files are included.

Some hooks fix files (for example, removing extra spaces).
When a hook changes a file, the run reports a failure.

This is expected (and welcome!).
Stage the changes with git add -A and run again.
Repeat until every hook passes.

## Read prek.toml

You rarely have to write prek.toml.
Just copy it from an example project.

```toml
fail_fast = false

[[repos]]
repo = "https://github.com/pre-commit/pre-commit-hooks"
rev = "v6.0.0"

[[repos.hooks]]
id = "check-toml"
name = "B2) Validate TOML syntax"
```

- repo: where the hooks come from.
- rev: the exact version to use.
  Pinning the version means everyone runs the same checks.
- [[repos.hooks]]: one entry per check.
  id picks the check, name is what you see when it runs.
- fail_fast = false: run all hooks and show all problems,
  instead of stopping at the first.
- A top-level exclude lists folders to skip, such as .venv/ and site/.

## Hooks and CI

The same prek.toml can run on GitHub (after a push).
Local hooks check files before the commit;
CI repeats the check on a clean machine.
Passing both means the project works for other people, not only on yours.

Skipping hooks is possible (git commit --no-verify),
but defeats the purpose.
Fixing the problem the check found is better.

<details markdown>
<summary>WHY?</summary>

Small mistakes are cheapest to fix before they enter project history.
A shared list of checks keeps formatting and file problems out of every commit,
and the habit of running them transfers to any professional team.

</details>

## Verification

- [ ] uvx prek run --all-files finishes with every hook passing.
- [ ] You can name two checks in prek.toml and describe what they catch.

---

[◄ Back to 🏠 Guide Home](https://denisecase.github.io/pro-analytics-02/)
