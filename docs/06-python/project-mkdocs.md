# Hosting Project Documentation

Project documentation turns a folder of files into a
clean, navigable website that can be used to present and share analytics projects.

## Professional Purpose

Hosting documentation as a website helps:

- Share project information with a single link (no downloads needed)
- Keep instructions, examples, and policies close to the code
- Document decisions and changes over time
- Demonstrate professional practice (clear documentation is a necessary part of project quality)

In these projects, documentation lives in the `docs/` folder and is built with MkDocs.

## How It Works

- We write pages as Markdown files in `docs/`
- `mkdocs.yaml` (in the repo root) defines the site title, theme, and navigation (`nav:`)
- MkDocs builds a static website into a `site/` folder (generated output)
- GitHub Pages hosts that static website publicly
- GitHub Actions can build and deploy the site automatically on every push

## Prerequisites for a Documentation Site

- The repository must have:
  - `docs/` folder
  - `mkdocs.yaml` in the repo root
- MkDocs is installed in the project environment (via `pyproject.toml`)
- The site is built with commands from the repo root using `uv run ...`

## Step 1: Enable GitHub Pages

In a browser, open the GitHub repository:

1. Go to Settings (gear icon way on the right)
2. Click Pages tab (down the left)
3. Under **Build and deployment**
4. Set Source to **GitHub Actions**

This tells GitHub Pages to publish a site built by a `.github` workflow (instead of a branch).

## Step 2: Configure a GitHub Actions Workflow

See examples of automatic GitHub actions in this project.
We first ensure the site builds in the CI (continuous integration) step and then deploy the docs in a separate step.

- CI: `.github/workflows/ci-python-mkdocs.yml`
- Deploy: `.github/workflows/deploy-mkdocs.yml`

## Step 3: Preview the Docs Locally

From the repo root:

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

> To stop a running Python program, press `Ctrl + C` in the terminal

The build will verify that:

- all files in `docs/` are also in the navigation
- all files listed in `mkdocs.yaml` `nav:` are also in `docs/`.

Step 4: Trigger the First Deploy (Automatically)

When we save progress, the two actions above will be triggered.

Save progress frequently (some tools may make changes; you may need to **re-run git `add` and `commit`** to ensure everything gets committed before pushing):

```shell
git add -A
git commit -m "update"
git push -u origin main
```

## Troubleshooting

### Site shows a 404 (file not found) error

- Confirm **Settings / Pages / Source** is set to **GitHub Actions**
- Confirm the documentation workflow run succeeded (see the GitHub repo **Actions** tab)
- Confirm the site builds locally without errors:
  ```shell
  uv run mkdocs build --strict
  ```

### Build fails with "file not found"

- Check paths in `mkdocs.yaml`, especially under the `nav:` section
- Confirm the referenced page exists in `docs/`
- Verify spelling and capitalization **exactly match** the file name

### Changed docs but site did not update

- Confirm changes were pushed to the `main` branch
- Check the GitHub repo **Actions** tab to verify that a workflow run was triggered
- If needed, re-run the workflow manually from the **Actions** tab


<mark> Powerful tools make professional projects possible from the beginning.</mark>
