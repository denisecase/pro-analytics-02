# 🟡 Configure Repository Settings

> Configure repository settings for your project.

## Enable GitHub Pages (If the Project Includes Documentation)

Some project templates include a documentation site built with
**Zensical** (or **MkDocs**).

If your project includes a `zensical.toml` or `mkdocs.yml` file,
enable **GitHub Pages** so the documentation can be published.

If your project does NOT include one of these documentation configuration files,
skip this section.

### Enable GitHub Pages

1. In your new repository, click the **Settings** tab (gear icon, far right).
2. In the left sidebar, select **Pages**.
3. Under **Build and deployment / Source**, choose **GitHub Actions**
4. Click the **Code** tab (upper left) to return to the repository view.

Once enabled, GitHub will automatically build and publish
the documentation website when the documentation workflow runs.
An associated workflow should be provided in `.github/workflows/`.
You are not expected to write GitHub Actions on your own.

## Project Documentation

Our work requires **professional communication**, not just code.
When a project includes a documentation site, it can be used to:

- explain the purpose of the project
- describe methods and techniques
- record experiments and results
- provide clear instructions for others

Not every analytics project requires a separate documentation site.
Use the structure provided by the project template,
or enable GitHub Pages if a documentation site would be a useful addition.
