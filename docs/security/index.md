# Software Security Gates

All software intended for distribution or reuse
must pass applicable security gates, regardless of author.

## Terms Used

- **SCA (Software Composition Analysis)** - Identifies third-party dependencies and checks them for known vulnerabilities.

- **SAST (Static Application Security Testing)** - Analyzes source code for potential security vulnerabilities without executing it.

- **SBOM (Software Bill of Materials)** - A machine-readable inventory of the components and dependencies in software.

- **Syft** - An open-source tool for generating SBOMs from source code, filesystems, containers, and software artifacts.

- **CycloneDX** - An open standard and data format for representing SBOMs and related software supply-chain information.

## Gate 1. Distributed Software

Applies to software made available for others to
clone, run, adapt, or reuse,
including example and instructional projects.

Set up these automatic checks:

- [ ] (git hooks) use prek to run quick pre-checks.
- [ ] (ci) `ty` runs and reports type issues.
- [ ] (ci) Tests run and pass before completion.
- [ ] (ci) SCA runs, e.g. `pip-audit`, and known vulnerabilities are addressed.
- [ ] (repo) SAST runs, e.g. GitHub CodeQL, and security findings are reviewed.
- [ ] (repo) GitHub dependency graph is enabled and complete.
- [ ] (repo) Dependabot alerts are enabled.
- [ ] (repo) Dependency review is enabled where applicable.
- [ ] (repo) Secret scanning and push protection are enabled where available.

Always ensure:

- [ ] GitHub Actions use minimal permissions.
- [ ] Security, dependency, and workflow changes receive careful review.
- [ ] No security check is disabled or weakened to make CI pass.

### Python Project Configuration

A common Python `pyproject.toml`, may include

```toml
[dependency-groups]
dev = [
# REQ: External packages used for linting, testing, type checking, etc.
"pytest", # WHY: Test framework for unit and integration tests.
"pytest-cov", # WHY: Test coverage reporting for quality assurance.
"ruff", # WHY: Fast linting and formatting for code quality and consistency.
"ty", # WHY: Type checking for static analysis and bug prevention (replaces `pyright`).
]
```

### Configure Git Hooks

Configure checks.
See this project's `prek.toml` for an example.

### Configure GitHub Project Repository

For public open-source repositories,
enable GitHub's available security features, including:

- CodeQL/code scanning,
- secret scanning,
- push protection,
- dependency review, and
- Dependabot.

For example, to enable CodeQL:
GitHub repo / Security and quality tab / Set up code scanning /
Tools / CodeQL analysis / Set up / Default / Enable CodeQL

Some GitHub security features that are free for public repositories require
GitHub Code Security, GitHub Secret Protection, or
GitHub Advanced Security for private repositories.

### Configure CI Workflow Action

Use a triggered GitHub action to ensure CI (continuous integration) checks are
run automatically.
See this repo's `.github\workflows\ci-python-zensical.yml` for an example.

### Configure SBOM Workflow Action

Use a triggered GitHub action to automatically create the SBOM using recommended
process and formats.
See this repo's `.github\workflows\sbom.yml` for an example.

### Periodically Monitor the Project Repository

Check your GitHub repository regularly for security alerts,
workflow failures, and pull requests.

When Dependabot creates a pull request, review the proposed changes
and automated check results before deciding whether to merge.

See [How to Accept a Dependabot Pull Request](../tools/github-and-ci/03-accept-dependabot-pr.md)
for step-by-step instructions, including how to update your local project afterward.

To view project dependencies, open your GitHub repository and select
**Insights / Dependency graph / Dependencies**.

## Note on Instructional Projects

For instructional projects, **CI failures during development are expected**.
During this process, we can push work, inspect failed checks,
make corrections, and push again. For example, the CI `ty` check includes:
`continue-on-error: true`.
For production software and when comfortable fixing `ty` errors,
this line should be removed, and the gate can be enforced.

Advisory checks may report findings without blocking development.
All required gates MUST pass before work is considered complete or software released.

## Gate 2. Released Software

Applies in addition to Gate 1 when software is formally published or deployed,
including packages published to PyPI.

Before release:

- [ ] Gate 1 passes.
- [ ] Build release artifacts in CI from the reviewed source.
- [ ] Generate CycloneDX and/or SPDX SBOMs.
- [ ] Submit dependency information so GitHub dependency graph and native SBOM are complete.
- [ ] Retain the generated SBOM with the release where appropriate.
- [ ] Use PyPI Trusted Publishing/OIDC rather than long-lived publishing credentials.
- [ ] Generate provenance/artifact attestations where supported.
- [ ] Verify the release artifact before publication.
- [ ] Publish only from the controlled release workflow.

## Principle

AI-generated and human-written code cross the same security boundary.
No code is trusted because of who or what produced it;
confidence comes from the tests, security analysis,
dependency analysis, provenance, and release controls
it successfully passes.

## Two Independent SBOMs

Content lists are generated by two independent methods.
The SPDX version is built from GitHub's dependency graph.
The CycloneDX version is built from the repository contents.

```text
uv.lock
   │
   └── GitHub/Dependabot
          │
          V
     Dependency Graph
          │
          └── Export ───→ sbom.spdx.json
                          GitHub's view

repository
   │
   └── Syft ────────────→ sbom.cdx.json
                          independent view
```

## See Also

- [CAE Notes on Using AI](./CAE-NOTES-ON-USING-AI.md)

---

[◄ Back to 🏠 Guide Home](https://denisecase.github.io/pro-analytics-02/)
