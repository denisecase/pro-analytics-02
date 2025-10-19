# Pro Analytics 02: Setup and Workflow Guide

[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://denisecase.github.io/pro-analytics-02/)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue?logo=python)](#)
[![CI Status](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci.yml/badge.svg)](https://github.com/denisecase/pro-analytics-02/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

> Opinionated guide to professional Python projects.

## Overview

This repository contains the **documentation website** that teaches the Pro Analytics workflow.
It is meant to be **read**, not cloned or forked.

Use this site as a reference for:

- setting up a machine for modern Python development
- starting and structuring a new Python project
- using GitHub effectively
- developing a repeatable, professional daily workflow

## How to Use It

Read the [**published guide**](https://denisecase.github.io/pro-analytics-02/).

- Follow the steps in order, starting with **Workflow 1. Set Up a Machine**.
- When you reach **Workflow 2. Set Up a Project**, copy the [associated starter repository](https://github.com/denisecase/pro-analytics-02-starter) to start a new project.

## October 2025 Update

This guide uses `uv` for faster dependency management and improved cross-platform support.
It succeeds the earlier [pro-analytics-01](https://github.com/denisecase/pro-analytics-01) guide which uses `pip`, `venv`, and `requirements.txt` (still a  common professional approach).
If you prefer that approach, you do not need to switch.

## Feedback and Questions

If you have suggestions or want to request clarifications, use:

- [GitHub Discussions](https://github.com/denisecase/pro-analytics-02/discussions)
- [GitHub Issues](https://github.com/denisecase/pro-analytics-02/issues)

Your feedback helps improve the guide for everyone.

## For Project Contributors

Pull and run checks:

```shell
git pull
uv sync --extra dev --extra docs --upgrade
uv cache clean
git add .
uvx ruff check --fix
uvx pre-commit autoupdate
uv run pre-commit run --all-files
git add .
uv run pytest
```

Build and serve docs:

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

Git add-commit-push to GitHub:

```shell
git add .
git commit -m "Add msg here"
git push -u origin main
```
