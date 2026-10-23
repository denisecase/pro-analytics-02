# 🟣 Workflow D: Apply Skills

<!-- On a page that could be read aloud,
use two asterisks instead of backticks
for code. -->

> Apply the tools and techniques from the example project
> to a different problem.

<details markdown>
<summary>WHY?</summary>

Professional work often involves learning from existing projects
and applying proven techniques to new problems.

This workflow develops the ability to understand an example,
make deliberate technical changes, and apply the same
tools and techniques independently.

The goal is to demonstrate that you can use what you learned
to produce meaningful results for a different problem.

</details>

Be sure you have completed
[Workflow C: Start New Project](../workflow-c-start-new-project/)
successfully before beginning.

## Progression

Build your custom project progressively,
applying the same workflow each time.

Start with the working example.
Then make a small technical change and observe its effects.
Then apply the important tools and techniques demonstrated
in the example to your new problem or dataset.

Make your own analytical decisions.
Explain what you changed, why you changed it,
and what the results show.

| Progression                       | Change the project                                                  | Commit that evidences it                        |
| --------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------- |
| 1. Project works like the example | [Run the Project](run-project.md)                                   | `Baseline: project runs like the example`       |
| 2. Change a bit                   | [Make a Technical Modification](make-technical-modification.md)     | `Modified: <what changed> because <why>`        |
| 3. Apply to a new problem         | [Apply the Example to a Different Problem](apply-example-skills.md) | `Applied: <new problem or data> for <question>` |
| 3. (continued) Report the results | [Verify Results and Visuals](verify-results.md)                | `Results are visible and narrated`             |

## The Usual Loop

Workflow C established the project environment and installed the Git hooks.

As you develop your project, use the commands in your project README.md.
Repeat the usual loop after making each change:

1. [Manage the Environment](manage-environment.md) - as needed when dependencies change.
2. [Run Git Hooks](git-hooks.md) - check the changed files.
3. [Run the Project](run-project.md) - verify the project runs and produces expected output.
4. [Do Chores](run-chores.md) - run the project quality checks.
5. [⭐Git Add-Commit-Push to GitHub](git-add-commit-push.md) - use a commit message that communicates what changed and why.

Verify with the matching page before each commit:
[modification](verify-modification.md),
[new problem](verify-new-problem.md),
[results](verify-results.md).

## Your Thinking, Displayed in Code and Commits

The analytical decisions are yours.
Record them in the code as much as possible.
Your commit history provides clear evidence.

- [ ] The commit history includes one (or more) commits for each progression.
- [ ] Each commit message states what changed and why.
- [ ] The modification commit reflects just the small change chosen.
- [ ] It should be easy to review your commits and see how your project developed (LARGE commits should only occur during initialization).

---

[◄ Back to 🏠 Guide Home](../index.md)
