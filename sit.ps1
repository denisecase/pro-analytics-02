#Requires -Version 7.0

<#
============================================================
sit.ps1 (ALL-PY-SRC-REPOS)
============================================================
Updated: 2026-09-25: add prek, zizmor, audits

Situate project dependencies, lint, test, and build docs.
For Python tooling repos only.

Run with:
.\sit.ps1
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# ============================================================
# Precheck: pyproject.toml must use [dependency-groups], not the
# old [project.optional-dependencies]. With the old table, `uv sync`
# succeeds but does NOT install dev/docs, and later steps fail confusingly.
# ============================================================
if (Test-Path "pyproject.toml") {
    $pyproject = Get-Content "pyproject.toml" -Raw
    if ($pyproject -match '(?m)^\[project\.optional-dependencies\]') {
        Write-Host ""
        Write-Host "ERROR: pyproject.toml uses the old [project.optional-dependencies] table." -ForegroundColor Red
        Write-Host ""
        Write-Host "This repo has not been migrated. 'uv sync' would run but NOT install" -ForegroundColor Yellow
        Write-Host "the dev and docs dependencies, so linting, tests, and docs would fail." -ForegroundColor Yellow
        Write-Host ""
        Write-Host "FIX: open pyproject.toml and rename this one line:" -ForegroundColor Cyan
        Write-Host "    [project.optional-dependencies]   ->   [dependency-groups]" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Then run .\sit.ps1 again." -ForegroundColor Cyan
        Write-Host ""
        exit 1
    }
}

# ============================================================
# Precheck: dev dependencies must use the current repository tools.
#
# REQ:
# - prek MUST be a dev dependency because it is run with `uv run prek`.
# - pre-commit MUST NOT remain after migration to prek.
# - zizmor MUST NOT be a dev dependency because it is run independently
#   with `uvx zizmor@latest`.
# ============================================================
if (Test-Path "pyproject.toml") {
    $dependencyGroupsMatch = [regex]::Match(
        $pyproject,
        '(?ms)^\[dependency-groups\]\s*(.*?)(?=^\[|\z)'
    )

    if ($dependencyGroupsMatch.Success) {
        $devMatch = [regex]::Match(
            $dependencyGroupsMatch.Groups[1].Value,
            '(?ms)^\s*dev\s*=\s*\[(.*?)^\s*\]'
        )

        if ($devMatch.Success) {
            $devPackages = @(
                [regex]::Matches(
                    $devMatch.Groups[1].Value,
                    '(?m)^\s*"([^"]+)"\s*,?'
                ) | ForEach-Object {
                    $_.Groups[1].Value
                }
            )

            $hasPreCommit = @(
                $devPackages | Where-Object {
                    $_ -match '^pre-commit(?:$|[<>=!~;\[])'
                }
            ).Count -gt 0

            $hasPrek = @(
                $devPackages | Where-Object {
                    $_ -match '^prek(?:$|[<>=!~;\[])'
                }
            ).Count -gt 0

            $hasZizmor = @(
                $devPackages | Where-Object {
                    $_ -match '^zizmor(?:$|[<>=!~;\[])'
                }
            ).Count -gt 0

            if ($hasPreCommit -or -not $hasPrek -or $hasZizmor) {
                Write-Host ""
                Write-Host "ERROR: pyproject.toml uses outdated dev dependencies." -ForegroundColor Red
                Write-Host ""

                if ($hasPreCommit) {
                    Write-Host "REMOVE: `"pre-commit`"" -ForegroundColor Yellow
                    Write-Host "WHY:    prek replaces pre-commit." -ForegroundColor Yellow
                    Write-Host ""
                }

                if (-not $hasPrek) {
                    Write-Host "ADD:    `"prek`"" -ForegroundColor Cyan
                    Write-Host "WHY:    This repo runs hooks with 'uv run prek'." -ForegroundColor Cyan
                    Write-Host ""
                }

                if ($hasZizmor) {
                    Write-Host "REMOVE: `"zizmor`"" -ForegroundColor Yellow
                    Write-Host "WHY:    zizmor runs independently with 'uvx zizmor@latest'." -ForegroundColor Yellow
                    Write-Host ""
                }

                Write-Host "Update the dev dependency group, then run .\sit.ps1 again." -ForegroundColor Cyan
                Write-Host ""
                exit 1
            }
        }
    }
}

uv self update
uv python install
uv lock --upgrade
uv sync
uv audit

# install prek as the Git hook runner and update/freeze hook revisions
uv run prek install -f
uv run prek update --freeze --cooldown-days 7

git add -A
uv run prek run --all-files
# repeat if changes were made
uv run prek run --all-files

# run common chores
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build

Write-Host "All commands executed successfully."
Write-Host "Run a Python module to verify .venv/ is working correctly."
