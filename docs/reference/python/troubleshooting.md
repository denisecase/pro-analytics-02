# Troubleshooting

## ERROR: Stuck at `>>>` or `...`

If you see `>>>` or `...` in the terminal, you accidentally started **Python interactive mode**.

This happens sometimes.

**Fix:**
- Press `Ctrl + C`
- On Windows, if needed: press `Ctrl + Z`, then `Enter`

You should return to the normal terminal prompt.


## ERROR: Failed to canonicalize path

This usually means the virtual environment needs to be rebuilt.

**Fix:**

```shell
uv sync --extra dev --reinstall
```

Then continue with the workflow steps.

## Errors on Git Commit

If **optional pre-commit** checks are enabled, they may modify files or report failures.

This is normal.

**Fix:**
- Re-run `git add -A`
- Commit again

Some tools make changes during checks; re-running ensures everything is saved.
