# 🔵 Workflow 2.3: Read and Understand the Project

> Phase 3. Read and understand the tools and techniques used in the project.

## Professional Practice

Before modifying a project, first read and understand how it works.

Professional developers often explore a project in a consistent order: documentation, code, data, and outputs.

Focus on the overall flow of the project.
It's not necessary to understand every line of code at this point.

## Professional Project Organization

Real-world projects contain many files, so most professional projects follow a
predictable organization.

## Folder Naming Conventions

When referring to a folder in documentation, a `/` is often added to the name.
For example, `data/`.

The slash is **not part of the folder name** - it just indicates a folder.

## Goal

By the end of this phase you should understand:

- the purpose of the project
- the main tools or techniques used
- how data flows through the program

## Suggested Reading Order

### README.md (root project folder)

- Overview of the project
- Description of the problem and approach
- Instructions for running the project

### Documentation (`docs/`)

- Explanations of the project
- Descriptions of techniques used

### Notebooks and Source Code (`notebooks/` and `src/`)

Jupyter notebooks usually run from top to bottom.

Python modules are typically stored in `src/`.
Execution often begins at an entry point near the end of the file:

```python
def main():
    # This is where execution logic begins

if __name__ == "__main__":
    main()
```

When reading a Python file:

- locate the `main()` function
- observe which functions are called
- follow how information flows through the program
- note what is passed to each function as arguments (inside the parentheses)

### Data (`data/`)

- Explore the input datasets
- Observe how data is used in the program

### Outputs (`artifacts/` or `output/`)

- Review generated results, charts, or reports

### Log File (`project.log`)

- Shows what the program did during execution
- Useful for understanding program flow and debugging
- Confirms the program was executed successfully
