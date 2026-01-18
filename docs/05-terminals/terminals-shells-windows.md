# Windows: Shells and PATH Configuration

Shell-specific details and diagnostic commands for Windows.

## Windows Shells

### PowerShell

The modern default. Uses `$env:PATH` syntax.

Profile script customizes startup. Location varies; run `$PROFILE` to see yours.

### Command Prompt (cmd)

Legacy shell. Uses `%PATH%` syntax.
Different startup configuration than PowerShell.
Not recommended for development work.

### Git Bash

Bash-like shell bundled with Git for Windows.
Uses bash config files in your Windows user home
(as seen by Git Bash): `~/.bashrc` and sometimes `~/.bash_profile`.

A tool can work in PowerShell
but not Git Bash (or vice versa) depending on where PATH is set.

## System vs User Environment Variables

Windows maintains two scopes:

| Scope | Applies To | Common Use |
|-------|-----------|------------|
| System | All users | OS-level tools |
| User | Single account | Developer tools like `uv` |

The effective PATH merges both.
Changes apply only to newly started processes.
**Reopen terminals after changes**,
and sometimes **restart the machine**.

## Inspecting Your Environment

### PowerShell

```powershell
# Which shell process
Get-Process -Id $PID | Select-Object ProcessName

# Find a command
Get-Command uv

# Show PATH
$env:Path

# All environment variables
Get-ChildItem Env:
```

### Command Prompt (cmd)

```cmd
# Show PATH
echo %PATH%

# Find a command
where uv
```

### Git Bash

```bash
# Which shell
echo $0

# Show PATH
echo $PATH

# Find a command
command -v uv
type -a uv
```

## Finding the Source of Truth

### GUI Method

1. Open Start Menu.
2. Search "Edit the system environment variables".
3. Click "Environment Variables...".
4. Check both User variables > Path and System variables > Path.
5. Confirm the folder containing the missing tool, e.g., `uv` is listed.

After changes, close and reopen all terminals and VS Code.

## Quick Comparison Checklist

Run these in both terminals (working and failing):

| Check | PowerShell | cmd | Git Bash |
|-------|-----------|-----|----------|
| Shell | `Get-Process -Id $PID` | — | `echo $0` |
| PATH | `$env:Path` | `echo %PATH%` | `echo $PATH` |
| Find uv | `Get-Command uv` | `where uv` | `command -v uv` |

The difference between outputs explains the problem.
