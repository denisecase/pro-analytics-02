# 🟠 Create pyproject.toml

> Start with the example project's configuration and adapt it for your own Python project.

The **pyproject.toml** file defines your project's identity, Python requirements, dependencies, and development tool settings.

Rather than creating this file from scratch, use the working example as your starting point.

## Previously

You should have:

- Created your own GitHub repository.
- Cloned it to your machine.
- Opened your project in VS Code.
- Drafted your README.md.
- Committed and pushed your initial work.

Keep the example project available for reference.

## Step 1. Open Your Project in VS Code and Copy pyproject.toml

1. Open **VS Code**.
2. Select **File > Open Folder** and choose **your own project repository folder**.
3. Confirm that the VS Code Explorer shows **your repository**, not the example project. If your project is already open, simply confirm that it is the correct folder.
4. Open **Windows File Explorer** and navigate to the example project repository.
5. Find **pyproject.toml** in the example repository root.
6. Copy the file into the root of **your own repository**.
7. Return to **VS Code** and open your new **pyproject.toml** from the Explorer.

You now have a working configuration to adapt.

**IMPORTANT:** Do not edit the original example project. Make changes only in your own repository.

## Step 2. Update Project Identity

Find the **[project]** section.

Review and update:

- **name:** Change to your project's name, using lowercase letters and hyphens.
- **description:** Describe what your project does and the problem it addresses.
- **version:** Set an initial version for your own project, such as **0.1.0**, rather than retaining the example's version.
- **authors:** If present, replace the example's information with your own name or alias.
- **URLs:** Update any repository, homepage, documentation, or other project-specific links.

Keep the project name consistent with your repository and the source package you will create, where applicable.

## Step 3. Review Dependencies

Find the **dependencies** list and **[dependency-groups]** section.

The example may include packages for data processing, visualization, testing, documentation, and other features.

1. Review the dependencies used by the example.
2. Keep packages needed for your project.
3. Remove packages that your project will not use.
4. Add dependencies required for your planned application, if known.
5. Preserve the development and documentation tools that apply to your project.

You can revise dependencies as you develop your project.

The Python environment will be created in a later step using **uv**.

## Step 4. Review Project Configuration

Read the remaining sections of **pyproject.toml**.

Pay particular attention to:

- **Python version:** Confirm the required Python version is appropriate for your project.
- **Build system:** If the project creates an installable package, ensure package paths will match your own source code.
- **uv:** Review dependency management settings.
- **Ruff:** Review linting and formatting settings, if present.
- **ty:** Review type-checking settings, if present.
- **pytest:** Review test configuration, if present.
- **Marimo:** Keep Marimo settings if your project uses Marimo notebooks.

Retain the professional development conventions from the example unless your project requires a change.

**IMPORTANT:** If you change the Python package name or source directory, update any corresponding package references in the configuration.

You will create or adapt the matching project files in the next step.

## Step 5. Check for Example References

Search **pyproject.toml** for the original example's name and other project-specific values.

Confirm that:

- The project name describes your project.
- The description reflects your chosen problem.
- The version belongs to your project.
- Author and repository information is appropriate.
- Dependencies and package paths match your planned project.
- No unintended references to the example remain.

Save the file.

Do not copy the example's **.venv** environment. Your own environment and dependency lockfile will be created during environment setup.

## Verification

- [ ] Your own repository is open in VS Code.
- [ ] **pyproject.toml** exists in the root of your repository.
- [ ] The project name has been updated.
- [ ] The description identifies your project.
- [ ] The version has been updated.
- [ ] Author information and URLs are updated where applicable.
- [ ] Dependencies have been reviewed.
- [ ] Package paths and tool settings have been reviewed.
- [ ] No unintended example-specific information remains.
- [ ] Changes are saved.

You now have the configuration for your own Python project.

---

[◄ Back to 🟠 Workflow C](index.md)
