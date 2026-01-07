# Python File Structure

REQ:  Introduce the standard structure used in Python scripts and modules.

WHY:  Consistent structure improves readability and reuse.

OBS:  This structure is reused across projects.

---

## Standard Python Programs

Professional Python programs typically follow this order:

- imports at the top
- clearly named variables
- a `main()` function
- a conditional execution guard

This structure appears in both small scripts and large codebases.


## The `main()` Function

A `main()` function groups the primary actions of a script.

OBS:
The function name `main` is a convention.
It signals where execution begins when a file is run directly.


## Conditional Execution Guard

Python files often end with this block:

```python
if __name__ == "__main__":
    main()
```

This pattern is standard across Python projects.


## What the Guard Means

The variables with double underscores (often called *dunders*)
are built into every Python module automatically.

This conditional block means:

- when the file is run directly, `main()` is executed
- when the file is imported, `main()` is not executed

This allows the same file to function as both:

- a runnable script
- an importable module

## Reuse

This structure is reused consistently.

Consistent structure:

- reduces cognitive load
- supports testing and reuse
- makes programs easier to understand and extend
