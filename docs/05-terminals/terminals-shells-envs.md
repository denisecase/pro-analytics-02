# Terminals, Shells, and Environments

Understanding why a command works in one terminal but not another.

## The Mental Model

A computer is like a building:

- **Operating system** - the control room
- **Terminal** - a room where you type commands
- **Shell** - the interpreter that translates your commands for the control room
- **Environment variables** - rules that govern each room (each terminal session can have different rules)

The most important environment variable is **PATH**:
an ordered list of folders where the shell searches for programs.
If `uv` is installed in a folder not in PATH, the shell reports "command not found."

## Terminals

A terminal is a program that provides a text-based interface.
It displays input and output but does not interpret commands.

Examples: Windows Terminal, macOS Terminal, iTerm2, VS Code integrated terminal.

## Shells

A shell runs inside a terminal and interprets commands. The shell determines how commands are parsed, how environment variables are read, and which startup files are loaded.

| OS | Common Shells |
|----|---------------|
| Windows | PowerShell, Git Bash |
| macOS/Linux | zsh, bash |

A single terminal can host different shells.
Changing the shell changes command behavior.
The old Windows Command Prompt (cmd) is deprecated and not recommended.


## Environment Variables

An environment is a set of key-value pairs attached to a running process.
Common variables include PATH, HOME, USER, and SHELL.

Each process receives its own copy of the environment when it starts.

## Environment Inheritance

Programs start in a parent-child relationship:

1. A child process inherits a copy of the parent's environment.
2. If you open VS Code from a machine terminal, VS Code inherits that terminal's environment.
3. If VS Code opens an integrated terminal, that terminal inherits VS Code's environment.

This chain explains why PATH can differ between terminals.

## The PATH Variable

PATH contains an ordered list of directories.
When you enter a command:

1. The shell searches directories in PATH order.
2. The first matching executable runs.
3. If no match is found, the command fails.

## VS Code Integrated Terminal

The VS Code terminal inherits VS Code's environment,
then the chosen shell may run its own startup files.
Two VS Code settings affect this:

- **Terminal > Select Default Profile** - which shell runs
- **terminal.integrated.env.{windows,osx,linux}** - environment overrides

If something works in a machine terminal but not VS Code,
the shell or PATH likely differs.

## Diagnosing "Command Not Found"

When a command works in one terminal but not another:

1. Check which shell is running.
2. Compare PATH values.
3. Verify the command location is in PATH.

The difference between working and failing terminals is the explanation.

**Next:** See the OS-specific guides for detailed inspection commands and configuration locations.

- [Windows: Shells and PATH Configuration](terminals-shells-windows.md)
- [macOS/Linux: Shells and PATH Configuration](terminals-shells-mac-linux.md)
