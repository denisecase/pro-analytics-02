# 🔵 Make a Modification

## Professional Modifications

A technical modification is a deliberate change that affects what the project does, what it produces, or what it reports.

Start with a small change and observe its effect.
Small, incremental changes make cause and effect easier to understand.
Many useful discoveries happen this way.

## Requirements

Your modification must:

- be your own work (not a copy of someone else's unchanged result)
- be clearly described in your documentation or notes
- run successfully after the change

Technical modifications may often be something from the categories below (see your project for specifics).

### A. Change an Input or Setting

- use a different input file or dataset
- change a parameter, threshold, or configuration value
- change a filter, selection, or query

### B. Change the Logic

- add, remove, or adjust a transformation step
- add a new feature, metric, or derived value
- modify how results are computed or summarized

### C. Change the Output

- add a new result table, report, or summary
- add a new visualization (or adjust an existing one)
- change how results are saved (format, naming, location)

### D. Improve Observability

- add or refine logging statements
- add basic validation checks (for example: missing values, ranges, schema)
- improve error messages or warnings


## What to Record

Before moving to the next step, record your modification and observations in:

- **Required:** `README.md`
- **Required:** later, when saving your work, use the Git commit message to describe what you did
- **Optional (advanced):** describe your modification and observations in `docs/`, and ensure that `mkdocs.yml` in the root project folder includes your page in the **nav** section (usually at the end).

Record:

- what you changed
- why you made the change
- what you observed after running the project
