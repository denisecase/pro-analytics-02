# OPTIONAL: How to Make the "Your Main Branch Isn't Protected" Warning Go Away

Estimated time: **~10 minutes**

GitHub may display this warning on your repository:

> Your `main` branch isn't protected.
> Protect this branch from force pushing or deletion, or require status checks before merging.

This explains what the warning means and how to address it.

## GitHub Repository Branches

A Git `branch` is a version of your project's files and history.

Branches allow people to work on different changes independently.
For example, a team might create a separate branch
to develop a new feature without changing the `main` version of the project.

The default branch in a GitHub repository is typically named `main`.

In general, for individual projects,
the `main` branch is fine for all development.
In team situations, you may see additional branches.

Because `main` contains important project work,
we protect it from accidental deletion or unwanted changes to its history.

## Protecting Main with Two Simple Rules

GitHub allows repository owners to establish rules that protect important branches.

- **Restrict deletions:** Prevents the `main` branch from being accidentally deleted.
- **Block force pushes:** Prevents someone from forcibly replacing the existing history of `main`.

These help preserve work without altering the normal development process.

## How to Protect Main

1. Open your repository on GitHub.
2. Select **Settings** near the top of the repository page.
3. In the left sidebar, find **Rules** and select **Rulesets**.
4. Select **New ruleset**, then **New branch ruleset**.
5. Enter `Protect main` as the ruleset name.
6. Set **Enforcement status** to **Active**.
7. Under **Target branches**, select **Add target**, then **Include default branch**.
8. Under **Branch rules**, enable only these two options (which might be on by default):
   - **Restrict deletions**
   - **Block force pushes**
9. Leave all other restrictions disabled.
10. Select **Create** to save the ruleset.

GitHub may ask you to confirm your account credentials.

## Verify

Return to your repository.

1. Open **Settings / Rules / Rulesets**.
2. Verify `Protect main` appears.
3. Verify its status is **Active**.
4. Open the ruleset and confirm that it applies to the default branch
   and has the two protections enabled.

Return to the repository main page.
The warning about the unprotected `main` branch should no longer appear.
If the warning remains, confirm that the ruleset is active and applies to `main`.

## Associated Skill

Help protect important project code from unintended alterations.

## Reference

For more information, see the official GitHub documentation:

[About rulesets, GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

---

[◄ Back to 🏠 Guide Home](https://denisecase.github.io/pro-analytics-02/)
