# git-github.md

# Git and GitHub Glossary

A reference for version control with Git and GitHub.

## Version Control

A system that tracks changes to files over time,
enabling restoration to earlier states and viewing the evolving history of a project.

## Git

A distributed version control system that tracks changes to files locally.
Industry standard for managing code. Free and open source.

## GitHub

A cloud platform for hosting Git repositories.
Used to store projects and a professional portfolio.

## Repository (repo)

A version-controlled project folder.
Contains all project files plus the full history of changes.
Can be local (on your machine) or remote (on GitHub).

## Local Repository

The copy of a repository on your own machine.
Changes are made locally before being pushed to GitHub.

## Remote Repository

The copy of a repository hosted on GitHub.
The authoritative shared version of the project.

## Clone

Downloading a copy of a remote repository to your local machine.
Example: `git clone https://github.com/yourusername/your-repo-name`

## Commit

A saved snapshot of changes to the repository with a short descriptive message.
Commits are the building blocks of version history.
Example: `git commit -m "Add rolling window logic"`

## Commit Message

A short description of what changed in a commit.
Written in imperative present tense by convention: "Add feature" not "Added feature."

## Stage (git add)

Marking specific changes to be included in the next commit.
Example: `git add src/cintel/case_logic.py`

## Push

Sending committed changes from your local repository to GitHub.
Example: `git push`

## Pull

Downloading changes from GitHub to your local repository.
Example: `git pull`

## Branch

A parallel version of the repository for developing features or fixes
without affecting the main codebase.

## Main Branch

The primary branch of a repository, typically named `main`.
Represents the stable, current version of the project.

## Merge

Combining changes from one branch into another.

## Pull Request (PR)

A GitHub feature for proposing changes from one branch to another.
Supports code review before merging.

## Fork / Use this template

A personal copy of someone else's GitHub repository under your own account.
Forking is typically used only if you intend to make changes to the original project.
Projects where you don't keep a connection are typically copied
by clicking the green "Use this template" button instead.

## .gitignore

A file in the project root listing paths and patterns Git should not track.
Keeps generated files, environments, and sensitive data out of the repository.
Common entries: `.venv/`, `__pycache__/`.

## git status

A Git command showing which files have changed, are staged, or are untracked.
Run this frequently to understand the current state of your repository.

## git log

A Git command showing the commit history of the repository.

## git diff

A Git command showing the differences between the current files and the last commit.

## README.md

The front-page document of a GitHub repository.
Displayed automatically on the repository's GitHub page.
Explains what the project is, how to run it, and what outputs to expect.
