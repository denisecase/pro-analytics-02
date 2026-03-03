# editors.md

# Editors and Development Environment Glossary

A reference for code editors and the development environment.

## Code Editor

A program designed for writing and editing code.
Provides features like syntax highlighting, error detection, and terminal integration.

## VS Code (Visual Studio Code)

A free, widely used code editor developed by Microsoft.
Supports Python, Git integration, terminal access, and extensions.
Recommended editor for all operating systems.
Download: https://code.visualstudio.com/

## Zed Editor

A fast, modern code editor built for performance.
An alternative to VS Code, gaining adoption in the developer community.
Download: https://zed.dev/

## Extension

A plugin that adds functionality to a code editor.
VS Code examples: Python extension, Pylance (type checking), GitLens (Git history).

## Integrated Terminal

A terminal built into the code editor to run commands
without switching to a separate application.
In VS Code: View / Terminal, or Ctrl+` (backtick).

## Syntax Highlighting

Color-coding applied to code by the editor to make structure and keywords easier to read.
Different colors indicate different elements (strings, functions, keywords).

## Linter

A tool that analyzes code for style issues, errors, and potential bugs without running it.
Helps enforce consistent code quality.
Example: ruff.

## Formatter

A tool that automatically rewrites code to conform to style standards.
Example: `ruff format` enforces consistent indentation, spacing, and line length.

## ruff

A fast Python linter and formatter.
Configured in pyproject.toml.
Run with `uv run ruff check .` and `uv run ruff format .`

## Workspace

In VS Code, a workspace is the folder opened as the project root.
Open a project by opening its top-level folder in VS Code.

## Settings (settings.json)

A VS Code configuration file that controls editor behavior per workspace or globally.
Can configure Python interpreter, formatting on save, and other preferences.
