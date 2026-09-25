# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

---

## [Unreleased]

---

## [0.4.7] - 2026-09-25

### Before Next Block TODOS

- Update instructions and projects to use `prek` instead of `pre-commit`.
- Update project `pyproject.toml` files: add `prek`; remove `pre-commit`,
  `pip-audit`, and project-installed `zizmor` where present.
- Update project README/setup commands to use `prek` and `uv audit`.
- Update `.pre-commit-config.yaml` to use advisory `uvx zizmor@latest`.
- Update `sit.ps1` to use `prek` and run `uv audit`.
- Update CI to run `uv audit`.
- SHA-pin GitHub Actions in the canonical workflows with `gha-tools`,
  then verify with `zizmor`.

### Added

- Added `docs/stylesheets/extra.css`.
- Added advisory zizmor audit to repository hooks.
- Added `uv audit` to `sit.ps1` and Workflow B for dependency security auditing.

### Updated

- Replaced `pip-audit` with uv's built-in `uv audit`.
- Changed the Git hook runner from `pre-commit` to `prek` for this repo.
- Updated all GitHub Actions references to immutable SHAs for increased security.
- Updated `zensical.toml` to include admonitions and CSS.
- Updated `worker/src/index.js` to avoid information exposure through a stack trace.
- Updated Cloudflare Worker code and redeployed.
- Updated and simplified the opening page.
- Updated Workflow A Set Up Machine home page to include verification.

---

## [0.4.6] - 2026-09-22

### Added

- Added `docs/security/index.md` with software security gates.
- Added `docs\security\CAE-NOTES-ON-USING-AI.md`.
- Added `sbom.yml` to generate SPDX and CycloneDX SBOMs.
- Added `pip-audit` for software composition analysis (SCA).

### Updated

- Updated `docs\workflow-a-set-up-machine\03b-mac-install-tools.md` to install using native so `uv self update` works.
- Updated `.pre-commit-config.yaml`.
- Updated `pyproject.toml` development dependencies.
- Updated `.github/dependabot.yml` for automated dependency updates.
- Updated `.github/workflows/ci-python-zensical.yml` with the SCA security check.
- Updated to `.github/workflows/deploy-zensical-ga-ai.yml` to reflect both Google Analytics and addition of AI assistant.
- `worker\src\index.js` here and in CloudFlare
  Workers & Pages / pro-analytics-02-assistant / Edit code.
  (See observability / logs for debugging.)
- updated from `gemini-2.5-flash` to `gemini-3.6-flash` in `worker\wrangler.toml` and `worker\src\index.js`.

### Fixed

- Ask the Assistant integrated AI is working (with limits).

## [0.4.5] - 2026-09-17

- Add initial Google Analytics page-view and unique-visitor counts to documentation pages.
- Add daily scheduled refresh of documentation analytics.
- Add initial Google Gemini integrated AI assistant with an “Ask the agent” dialog.
- Add a Cloudflare Worker to keep the Gemini API key outside browser code.
- Add build-time generation of guide-context.json for assistant integration.
- Add Google Analytics and AI assistant setup instructions.
- Remove Node installation (os-tools number four) and the node --version check.
- Remove the associated markdownlint-cli2 --fix command.
- Keep .markdownlint-cli2.yaml in the repository root for optional use.

---

## [0.4.4] - 2026-08-22

- updated links
- updated NotebookLM and video

---

## [0.4.3] - 2026-08-17

- new process with real example projects and taking ownership (rather than templates)
- used `uvx pup-up` to get new ci and docs actions and sit that use local py version

---

## [0.4.2] - 2026-08-11

- changed pyproject.toml from old `[project.optional-dependencies]` to new `[dependency-groups]`
- changed from old `uv sync --extra dev --extra docs` to new `uv sync`.
- always `uv lock --upgrade` to keep deps current (then run `uv sync`).
- updated supporting files using `uvx pup-up`
- must remain 3.14
- used `uvx pup-clean`, `uvx pup-clean --delete`, and `.\sit.ps1`
  after changing to 3.14 to rebuild.

---

## [0.4.1] - 2026-06-10

- used dc-up to update baseline files (except zensical.toml).

---

## [0.4.0] - 2026-06-04

## Updated

- Updated release validation order to run `uv lock --upgrade` before `uv sync`.
- Updated repository hygiene configuration for cross-platform.
- Updated Markdown lint configuration for authored course documentation.
- Updated setup guidance to include Node.js for tools that run through `npx`.

## Added

- Added accountable surface declaration.
- Added generated GitHub CODEOWNERS projection from accountable surfaces.

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
1.2. `pyproject.toml` - update `version`
1.3. CHANGELOG.md: add section, move unreleased entries, update links

### Task 2. Validate

```shell
uvx pup-clean --delete
# uvx pup-up

.\sit.ps1

# Update GitHub Actions and pin all action references to immutable SHAs
uvx gha-tools autoupdate --pin=all --write .github/workflows

# Then audit the resulting GitHub configuration for security findings
uvx zizmor@latest .github/

uvx cffconvert --validate
npx markdownlint-cli2 --fix

uv run python -m pro_analytics_02.demo_module_basics
uv run python -m pro_analytics_02.ml_example

Remove-Item project.log

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

[Unreleased]: https://github.com/denisecase/pro-analytics-02/compare/v0.4.7...HEAD
[0.4.7]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.7
[0.4.6]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.6
[0.4.5]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.5
[0.4.4]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.4
[0.4.3]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.3
[0.4.2]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.2
[0.4.1]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.1
[0.4.0]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.4.0
[0.3.0]: https://github.com/denisecase/pro-analytics-02/releases/tag/v0.3.0

<!-- markdownlint-enable MD024 -->
