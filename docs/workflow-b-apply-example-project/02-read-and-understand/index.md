# 🔵 Read and Understand the Project

> Study the working example.

<details markdown>
<summary>WHY?</summary>

Before modifying a project, first read and understand how it works.

Reading the project before changing it builds understanding of the project
structure, data flow, commands, and outputs.

Professional work often requires extending existing code
rather than starting from nothing.

Understanding a working example supports better technical decisions
in later modification and application phases.

Focus on the **overall flow of the project**.
It's not necessary to understand every line of code at this point.

</details>

## Professional Project Organization

Real-world projects contain many files,
so most professional projects follow a predictable organization.
You can use the
[Professional Python Project Explainer](https://denisecase.github.io/professional-python-project-explainer/)
to get information about common files and folders.

## Objectives

By the end of this phase you should understand:

- the **purpose** of the project
- the main **tools and techniques** used
- how data flows through the program

## Suggested Reading Order

### README.md (root project folder)

- Overview of the project
- Description of the problem and approach
- Instructions for running the project

### Documentation (docs/)

- Explanations of the project
- Descriptions of techniques used

### Source Code (src/)

Python modules are typically stored in src/.
Execution often begins at an entry point near the end of the file:

```python
def main():
    # This is where execution logic begins
```

When reading a Python file:

- locate the **main()** function
- observe which functions are called
- follow how information flows through the program
- note what is passed to each function as arguments (inside the parentheses)

### Data (data/)

- Explore the input datasets
- Observe how data is used in the program

### Outputs (artifacts/ or output/)

- Review generated results, charts, or reports

### Log File (project.log)

- Shows what the program did during execution
- Useful for understanding program flow and debugging
- Confirms the program was executed successfully

---

[◄ Back to 🔵 Workflow B](../index.md)
