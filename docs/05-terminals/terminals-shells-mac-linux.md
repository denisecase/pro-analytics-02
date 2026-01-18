# macOS/Linux: Shells and PATH Configuration

Shell-specific details and diagnostic commands for macOS and Linux.

## Common Shells

### zsh

Default on macOS. Configuration files:

| File | Loaded When |
|------|-------------|
| `~/.zshrc` | Interactive shells |
| `~/.zprofile` | Login shells |

### bash

Default on many Linux distributions. Configuration files:

| File | Loaded When |
|------|-------------|
| `~/.bashrc` | Interactive non-login shells |
| `~/.bash_profile` | Login shells |

Which files load depends on whether the shell is a login shell, interactive, or both.
Terminal apps and VS Code may launch shells differently, causing different files to load.

## Inspecting Your Environment

```bash
# Your login shell (what's configured)
echo $SHELL

# The currently running shell
ps -p $$ -o comm=

# Show PATH
echo $PATH

# Find a command (preferred)
command -v uv

# Alternative
which uv
```

## Finding PATH Configuration

Search your shell config files for PATH modifications:

```bash
grep -n "PATH=" ~/.zshrc ~/.zprofile ~/.bashrc ~/.bash_profile 2>/dev/null
```

Missing files are normal—the shell ignores them.

Common patterns that add to PATH:

```bash
# Prepend (searched first)
export PATH="$HOME/.local/bin:$PATH"

# Append (searched last)
export PATH="$PATH:$HOME/.local/bin"
```

## Why VS Code Terminal Differs

VS Code may launch shells as non-login or non-interactive,
skipping some config files.
If `uv` works in Terminal.app but not VS Code:

1. Check which shell VS Code is using (Terminal > Select Default Profile).
2. Compare PATH in both terminals.
3. Verify the PATH export is in a file that VS Code's shell loads.

For zsh, putting PATH modifications in `~/.zshrc` usually works for both.

## Quick Comparison Checklist

Run in both terminals (working and failing):

```bash
# Which shell is running
ps -p $$ -o comm=

# Current PATH
echo $PATH

# Where is uv
command -v uv
```

The difference between outputs explains the problem.
