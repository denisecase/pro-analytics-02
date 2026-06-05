# CONTRIBUTING.md

Thank you for helping improve this project.

This repository is central infrastructure.
Changes should make the instructions clearer,
more accurate, easier to follow, or easier to maintain.

## Before changing content

Review the relevant instructions in `README.md`.
For release and versioning expectations, use `CHANGELOG.md`.

## Contribution expectations

Contributions should:

- use clear, direct language;
- preserve instructional intent;
- avoid unnecessary tool churn;
- keep instructions cross-platform and consistent;
- include updated navigation when modifying documentation pages;
- keep generated files and source files clearly separated;
- pass configured checks before committing.

## AI-assisted contributions

AI tools may be used to draft, review, or improve changes.
The human contributor remains responsible for the submitted work, including:

- checking accuracy,
- reviewing generated changes,
- verifying commands,
- ensuring no private data or credentials are included,
- confirming that the final change fits the intended purpose.

AI assistance does not replace human review.

## Local checks

Run the repository checks before committing:

```shell
uvx pre-commit run --all-files
```

Some hooks may modify files.
If that happens, review the changes, then run:

```shell
git add -A
uvx pre-commit run --all-files
```

## Terminals

Commands are typically run from the root project folder unless otherwise stated
in an integrated VS Code terminal.

Windows users should use PowerShell, not the old Command Window.
