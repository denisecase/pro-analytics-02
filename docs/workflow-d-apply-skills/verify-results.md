# 🟣 Run and Verify Your Results and Visuals

> Confirm the results are correct and repeatable,
> and save a visual that supports them.

## Step 1. Run Again and Compare

Run the project a second time and compare the results to the first run.

- Deterministic projects: the results should be identical.
- Projects with randomness or time dependence
  (random seeds, streaming data): compare as the example's
  project instructions describe.

## Step 2. Check Correctness

Choose a check suited to the project and record what it showed.
Examples:

- recompute one value by hand or with a separate calculation
  from the raw data
- run a known input and confirm the expected output
- compare against a simple baseline
- confirm expected events or alerts appear for known cases

The example's project instructions say what verification means
for its type of project.

## Step 3. Save a Visual

Save at least one visual that supports a result.
Confirm that it:

- opens
- has a title, labeled axes, and units where they apply
- shows what the notes claim it shows

## Step 4. Confirm Git Sees the Visual

```shell
git status
```

The visual should be listed as a new file.
If it is not listed, it may be ignored by Git:

```shell
git check-ignore -v path/to/visual
```

## Step 5. Record for Documentation

Keep notes on:

- the numeric results and the visual
- what the results show (observations)
- what they mean (interpretation and insights)
- limitations and assumptions
- the checks performed and what they showed

These notes fill the **Verification**, **Results**, **Observations**,
**Interpretation and Insights**, and **Limitations** sections
of docs/index.md.

## Verification

- [ ] A second run produced the same results (or the expected variation).
- [ ] A correctness check was performed and recorded.
- [ ] At least one visual is saved, opens, and is labeled.
- [ ] `git status` lists the visual as a file to be added.
- [ ] Results, observations, and limitations are recorded.

---

[◄ Back to 🟠 Workflow C](index.md)
