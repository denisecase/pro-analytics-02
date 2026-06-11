# ============================================================
# shape.ps1
# ============================================================
# Updated: 2026-06-10
#
# REQ: List repository working files while respecting .gitignore.
# WHY: Use Git's own ignore rules instead of duplicating ignore patterns here.
# OBS: Includes tracked files and untracked non-ignored files.
# OBS: Excludes ignored files, .git internals, build output, caches, node_modules, etc.
# OBS: Reflects the working tree as it is NOW: files moved/renamed/deleted on
#      disk but not yet staged are dropped, so stale index paths don't appear.
# CUSTOM: Add path filters only if you want a narrower repo shape.

# Run with:
# .\shape.ps1

Clear-Host

# WHY: Must run from inside a Git repository.
$repoRoot = git rev-parse --show-toplevel 2>$null

if (-not $repoRoot) {
    Write-Error "Not inside a Git repository."
    exit 1
}

Set-Location $repoRoot

# WHY: --cached lists the INDEX, which still holds files moved/renamed/
#      deleted on disk but not staged. Subtract --deleted (tracked files
#      now missing from disk) so listing shows the current on-disk shape
#      without requiring a git add first.
$deleted = git ls-files --deleted

git ls-files --cached --others --exclude-standard |
    Where-Object { $deleted -notcontains $_ } |
    Sort-Object -Unique |
    ForEach-Object {
        ".\$_"
    }
