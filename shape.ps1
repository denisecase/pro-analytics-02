# List all working files in the repository
# Run in a PowerShell terminal at the root of the repo:
# .\shape.ps1

# Run with:
#   .\shape.ps1
#
# Lists working files in the repository.
# Uses Git's own ignore rules, including .gitignore, so generated files
# and ignored directories do not need to be duplicated here.

Clear-Host

if (-not (Test-Path ".git")) {
    Write-Error "shape.ps1 must be run from the repository root."
    exit 1
}

git ls-files --cached --others --exclude-standard |
    Sort-Object |
    ForEach-Object {
        ".\" + ($_ -replace "/", "\")
    }
