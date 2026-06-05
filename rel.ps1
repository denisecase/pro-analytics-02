#Requires -Version 7.0

<#
Run the release validation sequence.

The script echoes each exact command before running it.
#>

Clear-Host

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$PSNativeCommandUseErrorActionPreference = $true

function Invoke-Checked {
    param(
        [Parameter(Mandatory = $true)]
        [string] $Description,

        [Parameter(Mandatory = $true)]
        [scriptblock] $Command,

        [string] $FailureHint = ""
    )

    Write-Host ""
    Write-Host "============================================================"
    Write-Host $Description
    Write-Host "============================================================"

    try {
        & $Command
    }
    catch {
        if ($FailureHint) {
            Write-Host ""
            Write-Host $FailureHint -ForegroundColor Yellow
        }

        throw
    }

    if ($LASTEXITCODE -ne 0) {
        if ($FailureHint) {
            Write-Host ""
            Write-Host $FailureHint -ForegroundColor Yellow
        }

        throw "Command failed: $Description"
    }
}

function Invoke-Step {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Section,

        [Parameter(Mandatory = $true)]
        [string]$Command,

        [Parameter(Mandatory = $true)]
        [scriptblock]$Script
    )

    Write-Host ""
    Write-Host "============================================================"
    Write-Host $Section
    Write-Host "============================================================"
    Write-Host $Command
    & $Script
}

# ============================================================
# A) Toolchain refresh
# ============================================================

Invoke-Step "A1) Upgrade uv lock" "uv lock --upgrade" {
    uv lock --upgrade
}

Invoke-Step "A2) Sync all dependencies" "uv sync --extra dev --extra docs --upgrade" {
    uv sync --extra dev --extra docs --upgrade
}

Invoke-Step "A3) Run pre-commit autofix pass" "uvx pre-commit run --all-files" {
    $oldNativePreference = $PSNativeCommandUseErrorActionPreference
    $PSNativeCommandUseErrorActionPreference = $false

    uvx pre-commit run --all-files
    $exitCode = $LASTEXITCODE

    $PSNativeCommandUseErrorActionPreference = $oldNativePreference

    if ($exitCode -ne 0) {
        Write-Host ""
        Write-Host "Pre-commit may have modified files. Staging changes and continuing to verification pass."
        git add -A
    }
}

Invoke-Step "A4) Run pre-commit verification pass" "uvx pre-commit run --all-files" {
    uvx pre-commit run --all-files
}

# ============================================================
# C) Package command surface and manifest validation
# ============================================================

Invoke-Checked "C1) Validate SE manifest against schema" {
    uvx se-manifest-schema validate-manifest --path SE_MANIFEST.toml --strict
} -FailureHint "SE_MANIFEST.toml did not validate. See schema: https://github.com/structural-explainability/se-manifest-schema/blob/main/manifest-schema.toml"

Invoke-Step "C2) Generate CODEOWNERS file" "uvx se-codeowners generate --strict --output .github/CODEOWNERS" {
    uvx se-codeowners generate --strict --output .github/CODEOWNERS
}

Invoke-Step "C3) Confirm current CODEOWNERS" "uvx se-codeowners check" {
    uvx se-codeowners check
}


# ============================================================
# D) Pre-commit and Python tests
# ============================================================

Invoke-Step "D1) Stage all changes so pre-commit sees tracked/staged files" "git add -A" {
    git add -A
}

Invoke-Step "D2) Run pre-commit autofix pass" "uvx pre-commit run --all-files" {
    $oldNativePreference = $PSNativeCommandUseErrorActionPreference
    $PSNativeCommandUseErrorActionPreference = $false

    uvx pre-commit run --all-files
    $exitCode = $LASTEXITCODE

    $PSNativeCommandUseErrorActionPreference = $oldNativePreference

    if ($exitCode -ne 0) {
        Write-Host ""
        Write-Host "Pre-commit may have modified files. Staging changes and continuing to verification pass."
        git add -A
    }
}

Invoke-Step "D3) Run pre-commit verification pass" "uvx pre-commit run --all-files" {
    uvx pre-commit run --all-files
}

Invoke-Step "D4) Run Python tests" "uv run python -m pytest" {
    uv run python -m pytest
}

Invoke-Step "D5) Run Pyright" "uv run python -m pyright" {
    uv run python -m pyright
}

Invoke-Step "D6) Run final pre-commit check after tests/type checks" "uvx pre-commit run --all-files" {
    uvx pre-commit run --all-files
}

# ============================================================
# E) Documentation
# ============================================================

Invoke-Step "E1) Build documentation" "uv run python -m zensical build" {
    uv run python -m zensical build
}

# ============================================================
# F) Architectural and code-health checks
# ============================================================

# Invoke-Step "F1) Check import layers" "uvx --with-editable . --from import-linter lint-imports --config .github/.importlinter" {
#     uvx --with-editable . --from import-linter lint-imports --config .github/.importlinter
# }

Invoke-Step "F2) Find dead code" "uvx --with-editable . vulture src/pro_analytics_02" {
    uvx --with-editable . vulture src/pro_analytics_02
}

Invoke-Step "F3) Check complexity; any output means C-or-worse complexity exists" "uvx radon cc src/pro_analytics_02 -s -a -n C" {
    uvx radon cc src/pro_analytics_02 -s -a -n C
}

Invoke-Step "F4) Report raw code metrics" "uvx radon raw src/pro_analytics_02 -j | uv run python -c `"import json, sys; data=json.load(sys.stdin); keys=('loc','lloc','sloc','comments','multi','blank','single_comments'); totals={k:sum(file[k] for file in data.values()) for k in keys}; print('\n'.join(f'{k.upper()}: {v}' for k,v in totals.items()))`"" {
    uvx radon raw src/pro_analytics_02 -j | uv run python -c "import json, sys; data=json.load(sys.stdin); keys=('loc','lloc','sloc','comments','multi','blank','single_comments'); totals={k:sum(file[k] for file in data.values()) for k in keys}; print('\n'.join(f'{k.upper()}: {v}' for k,v in totals.items()))"
}

# ============================================================
# G) Distribution artifacts
# ============================================================

Invoke-Step "G1) Build source and wheel distributions" "uv build" {
    uv build
}

Invoke-Step "G2) Check distribution metadata" "uvx twine check dist/*" {
    uvx twine check dist/*
}

Write-Host ""
Write-Host "============================================================"
Write-Host "Release validation completed successfully."
Write-Host "============================================================"
