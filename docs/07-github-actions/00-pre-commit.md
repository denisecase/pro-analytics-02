# Pre-commit: Automated Quality Checks

Pre-commit is a tool used by professional developers worldwide to check code in any language and any project type.
Once the "hook" is installed, it runs automatically before every `git commit`command.

## Requirements

Pre-commit is a tool written in Python.
It requires a local Python enviroment (e.g. built with `uv` or `venv`) on the machine, even for non-Python projects.

## What Happens on Commit

When pre-commit is active, every `git commit` triggers a series of automated checks before the commit is allowed to succeed.

- If all checks pass, the commit succeeds and the code can be pushed to GitHub safely.
- If a check finds a problem it can fix automatically (like formatting), it fixes the file.
- To stage those changes, re-run `git add -A` and `git commit` which will pick up the fixed version.
- If a check finds a problem it cannot fix (like a syntax error in TOML), it reports what's wrong and where.
- We use the information to fix critical issues, then run `git add -A` and `git commit` again.

This enables many common errors to be caught locally, before they reach GitHub.

At work, pushing broken code to a shared repository is called "breaking the build" and it's not good.
Pre-commit helps make sure that doesn't happen.

## The Checks and Why They're Ordered This Way

Each group of checks depends on the previous group being clean. The order matters.

## A: Normalize File Formatting

WHY FIRST: Files contain invisible characters most people never think about - trailing spaces at the end of lines, inconsistent line endings between Windows and Mac, missing newlines at the end of a file.
These invisible differences cause real problems: noisy diffs that obscure actual changes, tools that behave differently on different operating systems, and teammates who see phantom changes in files nobody actually edited.
These checks clean all of that up silently, so every check that follows sees clean, consistent files.

- A1 trailing-whitespace - removes invisible spaces at the end of lines
- A2 end-of-file-fixer - ensures every file ends with a newline (required by git and many tools)
- A3 mixed-line-ending - normalizes line endings to LF so files work the same on every OS

## B: Validate Data File Formats

WHY NEXT: Projects have configuration files - pyproject.toml tells Python tools how to behave, YAML files configure GitHub Actions, JSON files store settings.
Every tool in the workflow reads these files.
If one has a syntax error - a missing bracket, a bad indent, an unclosed quote - the tools that depend on it will either crash with a confusing error or silently do the wrong thing.
These checks validate that every config file is well-formed before any tool tries to read it.

- B1 check-json - catches syntax errors in JSON files
- B2 check-toml - catches syntax errors in TOML files (like pyproject.toml)
- B3 check-yaml - catches syntax errors in YAML files (like GitHub Actions workflows)

## C: Check for Common Problems

WHY BEFORE CODE: Some mistakes are easy to make and hard to undo.
If a 200MB data file is accidentally staged, it enters the git history permanently - every clone of the repository downloads it forever, even after deletion.
If merge conflict markers (`<<<<<<<`) are left in a file, everything downstream breaks.
If two files are created whose names differ only by capitalization, it works on one machine but fails on another. These checks catch those accidents in seconds, before they become permanent problems.

- C1 check-added-large-files - prevents accidental commits of files over 500KB
- C2 check-merge-conflict - prevents committing unresolved merge conflict markers
- C3 check-case-conflict - prevents filename collisions across operating systems

## D: Python Formatting and Linting

WHY LAST: These are the most powerful checks - they read, understand, and improve Python code.
Ruff format makes code look consistent and professional.
Ruff check finds real bugs: variables defined but never used, names referenced but never imported, patterns that will cause errors at runtime.
These checks run last because they depend on everything above.
Ruff reads its settings from pyproject.toml (validated in B).
It needs consistent line endings (normalized in A).
And there's no point analyzing Python if the commit is going to be rejected for a merge conflict (caught in C).

- D1 ruff format - automatically formats Python code to a consistent style
- D2 ruff check --fix - finds and fixes lint errors; fails if any unfixable issues remain

## A Note on Prefixes

Prefixes (e.g. A1) are just concise identifiers.
When a check fails, the prefix identifies the step that had the problem.
They do not need to match across different projects, they are only for convenience.
