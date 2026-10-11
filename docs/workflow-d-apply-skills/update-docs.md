# 🟣 Update Project Documentation

> Tell the story of the project in docs/index.md.

## Previously

This assumes the project runs, the results are verified,
and the notes from Phase 3 are available:
the modification, the data and settings, the checks, and the results.

A project is never really final.
This page produces the current version of the story,
and it is updated as the project develops.

## Step 1. Open docs/index.md

Open **docs/index.md** in VS Code.
Replace the placeholder content with the sections below.

## Step 2. Write the Sections

Use these sections, in this order,
unless project-specific instructions are provided.
Each section has its own heading and its own content.

| Section                     | Contains                                                                                                                           |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Opening                     | Title, name or alias, year and month, and a short summary of the project                                                           |
| Data                        | The data used, its source, and what one record represents (the grain)                                                              |
| Techniques Applied          | The example's techniques and tools that were applied, and where each is used                                                       |
| Custom Modifications        | The technical modification: what changed, why, and the observed effect                                                             |
| Methods and Settings        | The analytical methods and the settings that affect results (for example thresholds, window sizes, random seeds, model parameters) |
| Verification                | The checks that were performed and what they showed                                                                                |
| Results                     | The numeric results and at least one visual                                                                                        |
| Observations                | What the results show, stated without interpretation                                                                               |
| Interpretation and Insights | What the observations mean                                                                                                         |
| Limitations                 | Limitations and assumptions                                                                                                        |
| Next Steps                  | What could be done next                                                                                                            |

Use the notes from Phase 3 as the starting point for each section.

Write each section with enough detail that a reader unfamiliar with
the project can follow it.
Use short paragraphs and lists, not one block of text.

## Step 3. Add a Visual

Save at least one visual in an images folder under **docs/**.
Link it from **docs/index.md** with a path relative to that file
and write alt text that says what the visual shows.

```markdown
![Description of what the visual shows](images/your-visual.png)
```

## Step 4. Preview

Preview the page as described in the example's project instructions.
The published page is checked after the push, in
[Update GitHub About Section](update-github-about.md).

## Verification

- [ ] docs/index.md includes every required section, in order.
- [ ] Each section has content.
- [ ] At least one visual is included, with alt text.
- [ ] The Data section states the source and what one record represents.
- [ ] Each conclusion is tied to a result or visual shown.
- [ ] Links in docs/index.md point to this project, the example, and the data source.

---

[◄ Back to 🟠 Workflow C](index.md)
