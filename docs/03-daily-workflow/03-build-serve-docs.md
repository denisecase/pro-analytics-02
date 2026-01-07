# 🔵 Build and Serve Documentation

Make sure you have current doc dependencies, then build your docs, fix any errors, and serve them locally to test.

```bash
uv run mkdocs build --strict
uv run mkdocs serve
```

IMPORTANT: If you get "Failed to canonicalize script path" use:

```shell
uv run python -m mkdocs build --strict
uv run python -m mkdocs serve
```


- After running the serve command, the local URL of the docs will be provided. To open the site, press **CTRL and click** the provided link (at the same time) to view the documentation. Use **CMD and click** on Mac.

- To stop the server, click in the terminal, and press **Ctrl c** (or **Cmd c** on Mac) to terminate the local hosting process.
