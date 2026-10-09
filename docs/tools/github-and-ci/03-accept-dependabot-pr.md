# OPTIONAL: How to Accept a Dependabot Pull Request

Estimated time: **~10 minutes**

GitHub may notify you that Dependabot has created a pull request for your repository.

Dependabot helps keep project software up to date.
This activity explains what Dependabot does, what a pull request is,
and how to review and accept a proposed update.

## Dependabot

Most software projects rely on tools and packages created by others.
These are called **dependencies**.
Dependencies are updated over time to fix problems,
address security concerns, and introduce improvements.

GitHub provides a tool called **Dependabot**
that checks for available updates to repository dependencies.
Dependabot can propose updates to:

- Python packages used by your project.
- GitHub Actions used to check and deploy your project.
- Tools used by your project's automated checks.

Dependabot does not automatically change the `main` branch
when it creates a pull request.
**You decide** whether to accept the proposed changes.

## What Is a Pull Request?

A **pull request (PR)** is a proposal to change files in a repository.

Instead of changing `main` directly,
Dependabot prepares updates in a separate branch
and asks you to review them.

You can inspect the proposed changes,
review the results of automated checks,
and decide whether to accept the update.

Accepting a pull request is called **merging**.
When you merge a Dependabot pull request,
GitHub incorporates the proposed changes into `main`.

## How to Review a Dependabot Pull Request

1. Open your repository on GitHub.
2. Select **Pull requests** near the top of the repository page.
3. Look for a pull request created by **dependabot[bot]**.
4. Select the pull request to open it.
5. Read the description to understand what Dependabot proposes to update.
6. Select **Files changed** to see exactly which files will change.
7. Look for the results of the automated checks near the bottom of the pull request.

For example, Dependabot might propose updating the version of a Python package
or replacing an older GitHub Action with a newer version.

Check that the proposed changes are appropriate for your project.

## Check the Automated Results

GitHub Actions can automatically check proposed changes before you accept them.
Depending on the repository, these checks may include:

- Python code checks.
- Automated tests.
- Documentation builds.
- Security checks.

Look for a message indicating that the required checks have passed.

- A green check indicates success.
- A red X indicates a failed check.
- A yellow indicator may mean that checks are still running.

**Do not merge a pull request with failed checks without investigating the failure.**

If checks are still running, return after they finish.

If the proposed update introduces an unexpected change,
you do not have to accept it.

## Optional: Accept a Pull Request

After reviewing the proposed changes and confirming that the checks pass:

1. Return to the **Conversation** tab of the pull request.
2. Scroll to the section near the bottom containing the merge controls.
3. Select **Merge pull request**.
4. Review the confirmation.
5. Select **Confirm merge**.

GitHub will merge the proposed changes into `main`.

If GitHub offers a different merge option or requires additional checks,
follow the repository's established requirements.

### Verify

Return to your repository.

1. Select **Pull requests**.
2. Select **Closed** to find the completed pull request.
3. Open the Dependabot pull request.
4. Verify that GitHub indicates the pull request was **Merged**.
5. Return to the repository's **Actions** tab.
6. Check that the automated workflows triggered by the merge complete successfully.

The dependency update is now part of your project's `main` branch on GitHub.

### Important: Git Pull Change to Local Machine After Accepting a PR

If you already have the repository on your computer,
it is important to keep your local copy in sync with the updated GitHub.

**Important:** Before making any local changes,
open the project in VS Code and update your local copy
by running `git pull` to fetch and merge the recent changes,
and then running `uv sync` to update the environment:

```powershell
git pull
uv sync
```

## Optional: Close Without Accepting the PR

You don't have to accept Dependabot pull requests.
If the update is inappropriate or introduces problems,
you can leave the pull request open while investigating.

You can also select **Close pull request**
to decline the proposed changes.
Closing a pull request does not change `main`.

## Best Practices

These habits apply to many professional software projects.

- Review changes.
- Check results. Look for passing tests and investigate failures.
- Watch major versions. Large version changes may require other changes.
- Prioritize security. Security fixes may be more urgent than routine updates.
- Keep projects working. Verify the project after accepting changes.
- Update deliberately. Not every suggested update needs to be accepted immediately.

## Associated Skills

- Review proposed updates.
- Examine a pull request before deciding on it.
- Interpret automated check results.
- Technical judgment
- Git merge a pull request.
- Verification
- Repository synchronization.

## Reference

For more information, see the official GitHub documentation:

[Managing pull requests for dependency updates, GitHub Docs](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/manage-dependabot-prs)

---

[◄ Back to 🏠 Guide Home](https://denisecase.github.io/pro-analytics-02/)
