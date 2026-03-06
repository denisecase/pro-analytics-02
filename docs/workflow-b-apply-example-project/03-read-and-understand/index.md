# 🔵 Workflow 2.3: Read and Understand the Project

> Read and understand the tools and techniques used in the project.

## Professional Practice

Before modifying a project, first read and understand how it works.
Professional developers often explore a project in a consistent order: documentation, code, data, and outputs.

Focus on the overall flow of the project.
It's not necessary to understand every line of code at this point.

## Professional Project Organization

Real-world projects typically contain more files than course examples.
To make projects predictable, most professional projects follow a standard organization.

## Folder Naming Convention

When referring to a folder, we often add a `/` at the end of the name.
For example: `data` folder and `data/` are often used interchangeably in narrative (like this).
The slash is not part of the folder name; it's just a convention used in documentation.

## Goal

By the end of this step you should understand:

- the purpose of the project
- the main tools or techniques used
- how data flows through the program

## Suggested Reading Order

### README.md (in root project folder)

- Provides a useful overview of the project
- Explains the problem and approach
- Provides instructions for running the project
- May highlight key insights (or these may appear in `docs/`)

### Documentation (usually found in `docs/`)

- The `docs/` folder contains detailed explanations of the project
- Review descriptions of the techniques used
- Build and view the documentation locally if available

### Notebooks and Source Code (usually found in `notebooks/` and `src/`)

Jupyter notebooks are typically kept in the `notebooks` folder.
Notebook execution begins at the top and runs sequentially using the active kernel.

Python module files are typically kept in the `src/` folder inside a project package.
Python file execution usually begins at the program entry point near the end of the file.
In many projects, look for a pattern like:

```python
def main():
    # This is where the execution logic begins

if __name__ == "__main__":
    main()
```

When reading a Python file:

- Scan toward the end of the file and locate the `main()` function
- Read the log statements to understand what the program reports
- Notice which functions are called
- Observe the information  passed to each function as arguments (inside the parentheses)
- Follow the flow of information through the program
- Pay attention to the data types used, as they determine available operations

### Data (usually found in `data/`)

- Explore input datasets and their structure
- Note how data is used in the program

###  Outputs (usually a new folder named `artifacts` or `output`)

- Examine generated results, charts, or reports
- Compare outputs with the project goals

###  Log file (usually found in the root project folder as `project.log`)

- Review messages showing what the program did during execution
- Logs often reveal the order of operations
- Logs provide useful clues when debugging program logic
