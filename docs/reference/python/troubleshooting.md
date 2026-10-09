# Troubleshooting

## Windows PowerShell ERROR: Execution Policy / Not Digitally Signed

When running a PowerShell script (`.ps1`) on Windows, you may see:

> File cannot be loaded because it is not digitally signed.
> You cannot run this script on the current system.

If you have reviewed the script and trust its source,
you can temporarily allow it to run in the current PowerShell session.

Run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then run the script. For example, if the file is named `sit.ps1`:

```powershell
.\sit.ps1
```

Important:

- Replace `sit.ps1` with the actual script filename.
- Run these commands in PowerShell, from the folder containing the script.
- This setting applies only to the current PowerShell session.
- Some organization-managed computers may prevent this change.

For more information, see
[Microsoft PowerShell Execution Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy).

## ERROR: Stuck at `>>>` or `...`

If you see `>>>` or `...` in the terminal, you may have started
**Python interactive mode**.

**Fix:**

- Press `Ctrl + C`.
- If needed, type `exit()` and press Enter.
- On Windows, you can also press `Ctrl + Z`, then Enter.

You should return to the normal terminal prompt.

## ERROR: Failed to canonicalize path

This may indicate a problem with the project's Python environment.

**Fix:**

Delete the project's `.venv` folder, then rebuild the environment:

```shell
uv lock --upgrade
uv sync
```

Then continue with the workflow steps.

## Errors on Git Commit

If Git hooks are installed, prek automatically runs the configured
checks when you commit.

Some checks may modify files or report problems that need correction.

**Fix:**

1. Read the messages and correct any remaining problems.
2. Review any files automatically modified by the checks.
3. Stage the corrected files and commit again.

```shell
git add -A
git commit -m "Describe your changes here"
```

Repeat as needed until the checks pass.

---

[◄ Back to 🏠 Guide Home](https://denisecase.github.io/pro-analytics-02/)
