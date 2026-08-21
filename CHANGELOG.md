# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

---

## [Unreleased]

- Remove Node installation (os-tools number four), node --version
- Remove the associated markdownlint-cli2 --fix command
- Remove .markdownlint-cli2.yaml from root
- NOTE: works great, just simplifying. May pick up a Python Markdown Linter if I miss it

---

## [0.4.3] - 2026-08-17

- new process with real example projects and taking ownership (rather than templates)
- used `uvx pup-up` to get new ci and docs actions and sit that use local py version

---

## [0.4.2] - 2026-08-11

- changed pyproject.toml from old `[project.optional-dependencies]` to new `[dependency-groups]`
- changed from old `uv sync --extra dev --extra docs` to new `uv sync`.
- always `uv lock --upgrade` to keep deps current (then run `uv sync`).
- updated supporting files using `uvx pup-up` - IMPORTANT: back up zensical.toml navigation first.
- must remain 3.14
- used `uvx pup-clean`, `uvx pup-clean --delete`, and `.\sit.ps1` after changing to 3.14 to rebuild.

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
uvx pup-clean --delete
uvx pup-up
.\sit.ps1

# OR

uv lock --upgrade
uv sync
uv run pre-commit install
uv run pre-commit autoupdate

uv run python -m pro_analytics_02.demo_module_basics
uv run python -m pro_analytics_02.ml_example

git add -A
uv run pre-commit run --all-files
# repeat if changes were made
uv run pre-commit run --all-files

uvx cffconvert --validate

uv run ty check
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

## Only As Needed (delete a tag)

```shell
git tag -d vX.Z.Y
git push origin :refs/tags/vX.Z.Y
```

## Links

[Unreleased]: https://github.com/denisecase/pro-analytics-02/compare/v0.4.3...HEAD
[0.4.3]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.3
[0.4.2]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.2
[0.4.1]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.1
[0.4.0]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.0
[0.3.0]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.3.0

<!-- markdownlint-enable MD024 -->
