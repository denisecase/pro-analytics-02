# 🔵 Read and Understand the Project

> Study the working example.

<details markdown>
<summary>WHY?</summary>

Professional work often requires understanding existing code
rather than starting from nothing.

Reading a working example helps explain the problem,
data, project structure, execution flow, and results.

Focus on the **overall flow and objective of the project**.
It's **not** necessary to understand every line of code at this point.

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

## 1. Start in GitHub

First, look at the project on GitHub.

### README.md (root project folder)

- What is the purpose of the project?
- What problem does it address?
- What are the instructions for running it?

### GitHub About Section

- What is the short project description?
- Is there a clickable link to the documentation or website?
- Are there topics (keywords) describing the project?

### Project Documentation

- Click the documentation or website link in the GitHub About section, if provided.
- Read the documentation home page (usually `docs/index.md`).
- Explore a few other documentation pages.
- Notice how the project explains its purpose, provides instructions, and presents its work to others.

### GitHub Activity

- Find the **Commits** link on the Code page.
- How many commits have been made?
- When was the most recent commit?
- Can you trace the evolution from the messages?
- Explore the **Actions** tab.
- Are automated checks passing?

Commits record changes to a project.
Try clicking on one to see what changed.

## 2. Then Explore On Your Machine

Then, open the project you cloned to your machine and explore in
more detail.

### Project Configuration (pyproject.toml)

- Identify the required Python version.
- Review the external dependencies used by the project.
- Distinguish runtime dependencies from development tools.

### Marimo Reactive App (app.py, if present)

Marimo supports interactive, reactive Python notebooks and apps.
Some Marimo apps are published online along with project documentation.
Look for a Python file such as `app.py`.
It may be in the project root, `src/`, or `notebooks/`.

### Source Code (src/)

Python modules are typically stored in src/.
Execution often begins at an entry point near the end of the file:

```python
def main():
    # This is where execution logic begins
```

When exploring the example project:

- identify the command and file that starts execution
- find the **main()** function or application entry point
- observe which functions are called
- identify reusable utility modules and their functions
- follow how data moves through the program
- note what arguments are passed to functions and what they return

### Data (data/)

- Explore the input datasets.
- What does one row or record represent (the grain)?
- What are the important variables?
- Observe how the data is used in the program.

### Documentation (docs/)

- Notice how these files are the source of the project documentation
  available via the About link.

### Tests (tests/, if present)

- What parts of the project are tested?
- How do the tests check that the code works correctly?

### Outputs (artifacts/ or output/)

- Review generated results, charts, or reports

### Log File (project.log)

- Shows what the program did during execution
- Useful for understanding program flow and debugging
- Confirms the program was executed successfully

---

## Success

You are ready to continue after:

- [ ] Explaining the problem and intended results.
- [ ] Describing the data, its grain, and important variables.
- [ ] Identifying the Python version, dependencies, and project structure.
- [ ] Locating the execution entry point and reusable utility modules.
- [ ] Explaining the main program flow from inputs to outputs.
- [ ] Identifying how the project verifies correct behavior.

---

[◄ Back to 🔵 Workflow B](index.md)
