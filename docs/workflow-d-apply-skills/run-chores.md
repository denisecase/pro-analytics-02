# 🟣 Do Chores

Use the project's configured development tools to format,
check, and test the code:

```shell
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
```

- **Ruff:** Formats code and identifies common programming problems.
- **ty:** Checks Python types.
- **pytest:** Runs automated tests, when available.
  Skip the `pytest` command in projects with no `tests` folder.

Review and address reported issues before continuing.

## Step 4. Build Documentation (If Applicable)

For projects using Zensical to build an associated project
documentation site, run:

```shell
uv run python -m zensical build
uv run python -m zensical serve
```

Open the local URL displayed in the terminal to review the documentation.

Press **Ctrl+C** in the terminal to stop the local server.

---

[◄ Back to 🟣 Workflow D](index.md)
