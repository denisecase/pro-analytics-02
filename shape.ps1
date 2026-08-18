# ============================================================
# shape.ps1 (ALL-REPOS)
# ============================================================
# Updated: 2026-08-16
#
# REQ: List project working files and directories that currently exist on disk.
# WHY: Provide a concise, copyable view of the current project structure.
# OBS: Does NOT depend on Git tracking or staging status.
# OBS: Newly created files and directories appear immediately without git add.
# OBS: Empty authored directories are included in the project shape.
# OBS: Excludes common generated, cached, virtual environment, and build folders.
# CUSTOM: Add path filters only if you want a narrower project shape.
#
# Run in a PowerShell terminal (available cross platform) with:
# .\shape.ps1


# === CONFIGURE EXCLUDED DIRECTORIES ===

# WHY: These directories contain generated, cached, downloaded, or temporary
#      content rather than authored project structure.

$excludedDirectories = @(
    ".git",
    ".venv",
    "__pycache__",
    ".cache",
    ".ruff_cache",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    ".nox",
    "node_modules",
    "build",
    "dist",
    "site"
)


# === GET PROJECT SHAPE ===

$projectRoot = (Get-Location).Path

Get-ChildItem -Path $projectRoot -Recurse -Force |
    Where-Object {
        $relativePath = [System.IO.Path]::GetRelativePath(
            $projectRoot,
            $_.FullName
        )

        $pathParts = $relativePath -split '[\\/]'

        $exclude = $false

        foreach ($directory in $excludedDirectories) {
            if ($pathParts -contains $directory) {
                $exclude = $true
                break
            }
        }

        -not $exclude
    } |
    ForEach-Object {
        $relativePath = [System.IO.Path]::GetRelativePath(
            $projectRoot,
            $_.FullName
        )

        if ($_.PSIsContainer) {
            ".\$relativePath\"
        }
        else {
            ".\$relativePath"
        }
    } |
    Sort-Object -Unique
