# 🟠 Configure Custom Repository Settings

> While in GitHub, configure your custom repository settings.

## Providing Project Documentation

Our work requires **professional communication**, not just code.
A documentation site allows us to:

- explain the purpose of the project
- describe methods and techniques
- record experiments and results
- provide clear instructions for others

GitHub Pages provides a clean and professional way
to publish project documentation.
The documentation site is separate from the source code
and project outputs, which reflects common professional practice.

## 1. Enable GitHub Pages (for Project Documentation)

Instructions:

1. In your new GitHub repository, click the **Settings** tab
   (gear icon, far right - you may need to click on "More" first.
2. In the left sidebar, select **Pages**.
3. Under **Build and deployment / Source**, choose **GitHub Actions**
4. Click the **Code** tab (upper left) to return to the repository view.

With Pages enabled, GitHub will build and publish
the documentation website when the documentation workflow runs.
An associated workflow should be provided in `.github/workflows/`.
You are not expected to write GitHub Actions on your own.

## Note

Not every analytics project publishes documentation publicly,
but creating clear, professional project documentation
is a valuable skill.

---

[◄ Back to 🟠 Workflow C](index.md)
