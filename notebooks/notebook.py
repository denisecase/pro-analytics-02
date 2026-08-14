"""notebooks/notebook.py - demo Marimo notebook app.

The official name starts with a lowercase "m" (marimo),
and the module name is lowercase (marimo).

See: https://github.com/marimo-team/marimo-uv-starter-template
And: https://marimo.io/gallery

Run with:

uv run python notebooks/notebook.py

To view as notebook,
click the "Open in marimo" button (m inside circle)
in the top right corner of this page.

To view again as a file, right-click and select
"Reopen editor" / "Text Editor".
"""

# === Imports ===

import marimo

# === Declare Version and Create App ===

__generated_with = "0.13.10"
app = marimo.App(width="medium")

# === Set up the app context and import modules ===

with app.setup:
    from pro_analytics_02.app_utils import add

# ==================
# === App Cells ===
# ==================


@app.cell(hide_code=True)
def _(mo):
    """App cell that uses the marimo module."""
    mo.md(
        r"""
# A marimo notebook

You can import your library code.
"""
    )
    return


@app.cell
def _():
    return (add,)


@app.cell
def _(add):
    """App cell that uses the add function from the utils module."""
    add(1, 2)
    return
