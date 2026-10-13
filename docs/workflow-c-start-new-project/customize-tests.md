# 🟠 Review and Customize Tests

<!-- On a page that could be read aloud,
use two asterisks instead of backticks
for code. -->

> Understand how automated tests verify the project's behavior.

Automated tests check that code produces expected results
and continues working as the project changes.

Python projects commonly use **pytest** for testing.

## Previously

Your custom project should be open in VS Code.
You should have reviewed the Python source code.

## Step 1. Review the Tests Folder

In VS Code Explorer, open **tests/**.

Typical test files include:

- **test_*.py** - files containing automated tests.
- **conftest.py** - shared pytest fixtures and configuration, if needed.

Tests commonly use functions whose names begin with **test_**.

If your project does not yet have tests,
you can add them as you develop your project.

## Step 2. Understand the Existing Tests

Open one or more test files.

Identify:

1. Which function or behavior is being tested.
2. What input or test data is provided.
3. What result is expected.
4. How the test determines whether the result is correct.

Tests frequently use **assert** to compare actual results
with expected results.

## Step 3. Identify What to Customize

Review the tests for your new project.

- Keep tests that verify reusable functionality.
- Update tests that depend on example-specific data or results.
- Add tests for new functions and expected behavior.
- Remove tests only when the behavior they verify is no longer relevant.

**IMPORTANT:** Do not change expected results simply to make a failing test pass.
Determine whether the code, test, or expected behavior needs correction.

You will develop and revise tests as you implement your project in Workflow D.

## Running Tests

After setting up the Python environment,
run pytest from the VS Code terminal in the project root:

```shell
uv run pytest
```

Review the results and investigate any failures.

## Verification

- [ ] I can locate the project's tests.
- [ ] I understand what the existing tests verify.
- [ ] I can identify tests that should be retained.
- [ ] I can identify tests that may require changes.
- [ ] I understand how to run pytest.
- [ ] New project behavior will have appropriate tests.

---

[◄ Back to 🟠 Workflow C](index.md)
