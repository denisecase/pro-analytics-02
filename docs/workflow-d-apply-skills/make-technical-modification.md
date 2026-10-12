# 🟣 Make a Technical Modification

> Change one thing in the project and observe its effect.

## Previously

This assumes the renamed project runs and the output from that run
was saved as a baseline for comparison.

## Step 1. Choose One Small Change

Choose **one** change.
If the example's project instructions suggest modifications, start there.

Examples of small, controlled changes:

- a setting that affects results
  (a threshold, a window size, a random seed, a model parameter)
- the columns, fields, or features used
- a calculation or processing step
- the type, labels, or layout of a visual

**IMPORTANT:** Change only one thing.
With a single change, any difference in the results can be traced to it.

## Step 2. Predict the Effect

Before making the change, write one sentence in the form:

> If I change x, I expect y because z.

## Step 3. Make the Change

Edit the project file in VS Code, then confirm Git sees only the
change that was intended:

```shell
git status
git diff
```

## Step 4. Record the Change

Keep notes on:

- what changed (the file and the setting or line)
- why it was chosen
- the predicted effect

These notes become the **Custom Modifications** section of docs/index.md.

## Verification

- [ ] Exactly one change was made.
- [ ] `git diff` shows only the intended change.
- [ ] A prediction was written before the project was run.
- [ ] The change, the reason, and the prediction are recorded.

---

[◄ Back to 🟣 Workflow D](index.md)
