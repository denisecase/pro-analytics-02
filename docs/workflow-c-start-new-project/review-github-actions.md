# 🟠 Review GitHub Actions and CI/CD

> Understand the automated workflows provided with your project.

GitHub Actions can automatically check, build,
and publish parts of a project.

These automated processes are commonly called **CI/CD**.

- **CI (Continuous Integration)** - automatically checks code and tests.
- **CD (Continuous Delivery/Deployment)** - prepares or publishes project outputs.

## Previously

Your custom project should be available on GitHub
and open in VS Code.

## Step 1. Review GitHub Workflows

In VS Code Explorer, open:

```text
.github/
    workflows/
```

Each workflow is defined in a YAML file.

Common workflows include:

- **CI** - checks Python code, tests, and other requirements.
- **Documentation deployment** - builds and publishes a documentation site.
- **Link checking** - verifies links in project documentation.
- **Security checks** - checks dependencies or code for known problems.

Your project may contain additional workflows.

If no workflows exist, you can add appropriate automation
as the project develops.

## Step 2. Understand the Workflows

Open the workflow files and identify:

1. What triggers each workflow.
2. What operating system and tools it uses.
3. What commands or checks it runs.
4. What constitutes successful completion.

For example, a workflow may run automatically
when changes are pushed to GitHub.

## Step 3. Review Project-Specific Settings

Review the workflows for references to:

- Repository names and paths.
- Python versions.
- Package and source folder names.
- Documentation configuration.
- Required GitHub repository settings, variables, or secrets.

Keep workflows that apply to your project.

Update project-specific settings when necessary.
Do not remove important checks simply to avoid failures.

**IMPORTANT:** Never put passwords, API keys, or other secrets
directly into workflow files.

## Step 4. Verify GitHub Actions

After pushing your project changes to GitHub:

1. Open your custom repository on GitHub.
2. Select the **Actions** tab.
3. Review the available workflows and recent runs.
4. Open a workflow run to inspect its results.

A green check indicates successful completion.
A red X indicates a failure that needs investigation.

Some workflows require repository settings or credentials
before they can run successfully.

See [Configure Repository Settings](03-configure-repo-settings.md).

## Verification

- [ ] I can locate the GitHub Actions workflow files, if provided.
- [ ] I understand the purpose of each workflow.
- [ ] I can distinguish CI from CD.
- [ ] I have identified project-specific settings requiring changes.
- [ ] I know where to review workflow results on GitHub.
- [ ] Applicable workflows will be checked after pushing my changes.

---

[◄ Back to 🟠 Workflow C](index.md)
