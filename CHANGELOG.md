# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

---

## [Unreleased]

---

## [0.4.1] - 2026-06-10

- used dc-up to update baseline files (except zensical.toml).

---

## [0.4.0] - 2026-06-04

## Updated

- Updated release validation order to run `uv lock --upgrade` before `uv sync`.
- Updated repository hygiene configuration for cross-platform line endings and generated outputs.
- Updated Markdown lint configuration for authored course documentation.
- Updated setup guidance to include Node.js for tools that run through `npx`.
- Updated release procedure to validate the SE manifest and generated CODEOWNERS before release.

## Added

- Added accountable surface declaration for central teaching instructions and repository governance.
- Added generated GitHub CODEOWNERS projection from accountable surfaces.
- Added governance checks for SE manifest validation and CODEOWNERS drift where applicable.

## Fixed

- Treated course log files as text evidence instead of binary files.
- Excluded generated documentation and coverage outputs from GitHub language statistics.

---

## [0.3.0] - 2026-05-08

- initial versioned release

---

## Notes on Versioning and Releases

- We use **SemVer**:
  - **MAJOR** - breaking changes
  - **MINOR** - backward-compatible
  - **PATCH** - fixes, documentation, tooling
- Versions are driven by git tags. Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.

## Release Procedure (Required)

Follow these steps exactly when creating a new release.

### Task 1. Update release metadata (manual edits)

1.1. `CITATION.cff` - update `version` and `date-released`
1.2. CHANGELOG.md: add section, move unreleased entries, update links
1.3. `pyproject.toml` - update `version`

### Task 2. Validate

```shell
uv lock --upgrade
uv sync --extra dev --extra docs --upgrade
uvx pre-commit install
uvx pre-commit autoupdate

# optional: generate and check CODEOWNERS
# based on roles defined in .accountability/surfaces.toml
uvx se-codeowners generate --strict --output .github/CODEOWNERS
uvx se-codeowners check

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
uvx pre-commit run --all-files

uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

git add -A
git commit -m "your message here"
git push -u origin main
```

### Task 4. Commit, push, tag

```shell
git add -A
git commit -m "Prepare X.Y.Z"
git push -u origin main
```

Verify actions run on GitHub. After success:

```shell
git tag vX.Y.Z -m "X.Y.Z"
git push origin vX.Y.Z
```

### Task 5. Verify tag consistency

```shell
uvx se-manifest-schema check-version --require-tag
```

Confirms CITATION.cff version matches the pushed git tag.
Run this after `git push origin vX.Y.Z`; it will fail before that point.

## Only As Needed (delete a tag)

```shell
git tag -d vX.Z.Y
git push origin :refs/tags/vX.Z.Y
```

## Links

[Unreleased]: https://github.com/denisecase/pro-analytics-02/compare/v0.4.1...HEAD
[0.4.1]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.1
[0.4.0]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.0
[0.3.0]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.3.0

<!-- markdownlint-enable MD024 -->
