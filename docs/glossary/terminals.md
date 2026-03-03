# terminals.md

# Terminal and Command Line Glossary

> A reference for working in the terminal (command line).

Applies across operating systems (e.g. Windows, macOS, Linux).

## Core Concepts

### cmd (Command Prompt): DEPRECATED (do not use)

The old Windows command-line interface. Not recommended for professional use.
Many modern commands and tools will not work in cmd.
If you see a black window with `C:\>`, you are in cmd. Open Powershell instead.

### Command

An instruction typed into the terminal and executed by pressing Enter.
Commands in this glossary work in zsh, bash, and PowerShell unless noted otherwise.
Example: `uv sync`

### Directory

A folder. Directories contain files and other directories.

### Environment Variable

A named value stored in the shell environment, accessible to programs.
Example: `PATH` tells the shell where to find executable programs.

### File Extension

The ending of a filename indicating its format.
Examples: `.py`, `.csv`, `.md`, `.log`, `.toml`, `.json`

### Home Directory

The personal directory for a user account.
Represented by `~` in the terminal.
Example: `cd ~` navigates to your home directory.

### How to Tell PowerShell from cmd

- PowerShell prompt: `PS C:\Users\yourname>`
- cmd prompt: `C:\Users\yourname>`
- The `PS` prefix confirms PowerShell.

### PATH (Environment Variable)

A special environment variable listing directories where the shell looks for commands.

### Root Directory

The top-level directory of a file system. All paths originate here.

When working with projects, we call the project repository folder the root folder of that project (the topmost folder for that project).

### Shell

The program running inside a terminal that interprets commands.
The shell determines which syntax and commands are available.

| OS      | Default Shell | Notes                                         |
| ------- | ------------- | --------------------------------------------- |
| macOS   | zsh           | bash also common, especially on older systems |
| Linux   | bash          | most distributions                            |
| Windows | PowerShell    | cmd is deprecated and not recommended         |

### Terminal

A text-based interface for running commands, navigating folders, and executing scripts.

| OS      | Default Terminal | Notes                                    |
| ------- | ---------------- | ---------------------------------------- |
| macOS   | Terminal         | iTerm2 is a popular alternative          |
| Linux   | varies by distro | GNOME Terminal, Konsole, etc.            |
| Windows | Windows Terminal | recommended, runs PowerShell by default  |

### Working Directory

The folder your terminal is currently operating in.
All relative paths are interpreted from here.
Check your current working directory with `pwd`.

### WSL (Windows Subsystem for Linux)

A compatibility layer that lets Windows users run a Linux (bash) environment natively.
When using WSL, you are in a bash shell regardless of your Windows default.

---

## Paths

### Absolute Path

A path written from the root of the file system.
Example (Mac/Linux): `/home/username/projects/cintel/data/input.csv`
Example (Windows): `C:\Users\username\projects\cintel\data\input.csv`

### Path

An address to a file or folder on your system.
Paths can be absolute or relative.

### Relative Path

A path written relative to the working directory. Use a single forward slash to separate.
Example: `data/input.csv`
Preferred over absolute paths, works across machines without modification.

---

## Commands

All commands below work in zsh, bash, and PowerShell unless marked otherwise.

### cd (Change Directory)

Navigate between folders.
Example: `cd projects/cintel`

### cp (Copy)

Copy a file or folder.
Example: `cp file.py file_backup.py`

### ls (List)

List files and folders in the current directory.
On Windows (non-WSL): use `dir` instead.

### mkdir (Make Directory)

Create a new folder.
Example: `mkdir data`

### mv (Move / Rename)

Move or rename a file or folder.
Example: `mv oldname.py newname.py`

### pwd (Print Working Directory)

Print the full path of the current working directory.

### rm (Remove)

Delete a file. Use with caution, there is no undo.
Example: `rm old_file.py`
