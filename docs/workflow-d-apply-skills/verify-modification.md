# 🟣 Run and Verify the Modification

> Run the modified project and compare the results to the baseline.

## Step 1. Run the Project

Run the project the same way as before.
See [Run Your Project](run-python.md).

## Step 2. Compare to the Baseline

Compare the new output to the baseline saved before the change.

- **Output differs as predicted:** the modification worked.
- **No difference:** the change may not affect the results,
  or it may not have been applied.
  Confirm the file was saved and the setting is actually used.
- **Output differs from the prediction:** investigate before continuing.
  An unexpected result is useful information. Note what it shows.
- **An error appears:** read the error message starting from the last lines.
  They name the failing file and line.

## Step 3. Undo if Needed

To discard the uncommitted edits in one file
and return it to the last commit:

```shell
git restore path/to/file
```

**IMPORTANT:** This permanently discards uncommitted edits in that file.
Run `git diff` first to confirm what will be lost.

## Step 4. Record the Observed Effect

Add to the notes:

- the observed effect
- whether it matched the prediction
- anything unexpected

## Verification

- [ ] The modified project runs without errors.
- [ ] The new output was compared to the baseline.
- [ ] The observed effect and its match to the prediction are recorded.

---

[◄ Back to 🟣 Workflow D](index.md)
