# Disk Space

Professional Python projects use isolated environments.
Each project installs its own packages into a `.venv` folder.
This is intentional to prevent version conflicts between projects.
The tradeoff is disk space.

## How Much Space to Expect

| Project Type                                       | Typical `.venv` Size | Typical Package Count |
| -------------------------------------------------- | -------------------- | --------------------- |
| Basic Python + dev tools + zensical docs           | ~100 MB              | ~47                   |
| + Data files (openpyxl, csv)                       | ~100 MB              | ~49                   |
| + SQL (duckdb, pandas)                             | ~200 MB              | ~51                   |
| + Notebooks (jupyter, pandas, matplotlib, seaborn) | ~350–400 MB          | ~80–85                |
| + Machine learning (scikit-learn added)            | ~400–450 MB          | ~88–92                |

These sizes reflect installed packages only.
Project source code and data files are small by comparison.

## One Active Project at a Time

The recommended workflow is to have **one project open at a time**.
Each project lives in its own folder under `Repos/` with its own `.venv`.
When you finish a project and push to GitHub,
you can delete the **local project repository folder** entirely.

Peak disk usage following this practice is the size of one project,
or about 100–450 MB depending on the project.

## Deleting a Project to Reclaim Space

Once work is in GitHub (verify first!), it can be deleted from the machine.

Everything needed to restore the project is in GitHub.
Project source code, data files, notebooks, and dependency list are all committed.
The `.venv` in not in Git and should not be,
because `uv sync` can rebuild it from `uv.lock` typically in less than a minute.

## Restoring a Project

To pick up where you left off, use git clone to copy your GitHub repo to your machine.
And follow the steps to recreate your environment using uv.

```shell
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade
```

## Safe to Delete

| Path           | Safe to delete? | Notes                                        |
| -------------- | --------------- | -------------------------------------------- |
| `.venv/`       | Yes             | Rebuilt by `uv sync`                         |
| `site/`        | Yes             | Rebuilt by `uv run python -m zensical build` |
| `.coverage`    | Yes             | Rebuilt by `uv run python -m pytest`         |
| `__pycache__/` | Yes             | Rebuilt automatically on next run            |

## Keep These (Ensure They are Safe in GitHub)

| Path              | Safe to delete? | Notes                                       |
| ----------------- | --------------- | ------------------------------------------- |
| `project.log`     | Commit first    | Generated output, commit before deleting    |
| `data/processed/` | Commit first    | Generated output, commit before deleting    |
| `uv.lock`         | Commit first    | Commit this to ensure reproducible installs |
| `pyproject.toml`  | Commit first    | Commit this as it defines the project       |
| `src/`            | Commit first    | Your code lives here                        |
| `notebooks/`      | Commit first    | Your analysis lives here                    |

## Dependabot and Long-Term Maintenance

If you keep a project repo active on GitHub,
Dependabot may open pull requests to update outdated packages.
This is a security and maintenance feature, not an error.

**For active course repos:** you do not need to act on Dependabot PRs.

**After the course:** if you want to keep a repo as a portfolio piece,
merging Dependabot PRs occasionally keeps dependencies current and signals active maintenance.
If you let a repo go inactive, Dependabot will eventually stop opening PRs automatically.

**If you get a Dependabot PR:** the safest action is to merge it, then run:

```shell
git pull
uv sync --extra dev --extra docs --upgrade
uvx pre-commit run --all-files
```

Verify everything still runs before pushing.
