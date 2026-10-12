# API Reference

> Your code is a valuable artifact.
> Document it to showcase what it can do.

An **API** (application programming interface) is the set of functions,
classes, and modules that one piece of code offers to another.
You use APIs every day:
`pandas.read_csv(...)`, `Path.exists()`, and `json.loads(...)`.
Those are all APIs that someone else defined and implemented.

When you write a function that code (or people) can call,
you are designing an API.

## Reading Documentation

Reading the documentation for a popular library such as
[pandas](https://pandas.pydata.org/docs/reference/index.html)
shows how a good API is organized:
the function name, the inputs it accepts, what it returns,
what can go wrong, and a short example.

When a job asks for "five years of experience,"
they aren't talking Python and SQL syntax.
Syntax is quick to learn.
What takes years is knowing **what already exists**
and being familiar with the massive amount of
free, tested code in the Python ecosystem,
and knowing which tool can help.
Experienced people often read documentation constantly,
and they know what a library can do before they start a project.

Build the same skill from both directions:
read the documentation of the libraries you use,
and write documentation for the code you create.

<details markdown>
<summary>WHY?</summary>

Employers hire people who can
use existing capabilities rather than rebuilding them.
Reading API documentation quickly is how to find those capabilities.

Writing documentation for your own code shows others
what you built and how to use it.
Well-named functions with clear inputs and outputs
are easier to test, reuse, and trust.

</details>

## Design Good Functions

A good function:

- does one thing
- has a clear name (a verb phrase, such as `mean_by_group`)
- declares its input and output types
- explains itself in a docstring

The docstring is the documentation.
This project uses the **Google style**:

```python
def mean_by_group(rows: list[dict], group: str, value: str) -> dict[str, float]:
    """Return the mean of a numeric column for each group.

    Args:
        rows: Records, each a dict with at least the group and value keys.
        group: Key whose distinct values define the groups.
        value: Key holding the numeric values to average.

    Returns:
        A dict mapping each group to the mean of its values.

    Raises:
        KeyError: If a row is missing the group or value key.

    Example:
        >>> mean_by_group([{"g": "a", "v": 1}, {"g": "a", "v": 3}], "g", "v")
        {'a': 2.0}
    """
    values_by_group: dict[str, list[float]] = {}
    for row in rows:
        values_by_group.setdefault(row[group], []).append(row[value])
    return {name: sum(vals) / len(vals) for name, vals in values_by_group.items()}
```

Add a short docstring at the top of each module
and in each package's `__init__.py`.
Those become the overview text on the page.

## Build an API Page from Your Code

With the structure above, free tools write an API page automatically.
[mkdocstrings](https://mkdocstrings.github.io/) reads docstrings,
and Zensical builds them into a documentation site.
Automation keeps the published API in sync with the code.

### 1. Use the src layout

Code lives in a package folder under `src/`.
The folder name is the package import name (use underscores, not hyphens):

```text
src/
  your_package/
    __init__.py
    your_module.py
```

### 2. Configure the Python Project

Include these in `pyproject.toml`:

```toml
[dependency-groups]
docs = [
    "mkdocstrings[python]",
    "zensical",
]
```

### 3. Configure mkdocstrings

In `zensical.toml`, tell mkdocstrings where your code is
and which docstring style you use:

```toml
[project.plugins.mkdocstrings.handlers.python]
paths = ["src"]

[project.plugins.mkdocstrings.handlers.python.options]
docstring_style = "google"
show_source = true
show_submodules = true
```

### 4. Create an API page

Create `docs/api.md`
with a line that starts with three colons and names your package:

```markdown
# API Reference

::: your_package
options:
show_submodules: true
show_source: true
```

### 5. Build and check

```shell
uv run python -m zensical build
```

Open the site (or run `uv run python -m zensical serve`)
and look at your API page.
Link to it from docs/index.md.

Each function should show its signature, description, arguments, return value,
and an optional link to the source code.

If a function is missing or blank, check:

- the package name in `:::` matches the folder under `src/`
- `paths = ["src"]` is in `zensical.toml`
- the module has a docstring, and the function has a docstring

## Verification

- [ ] Every public function has a Google-style docstring.
- [ ] Each module and package has a short docstring.
- [ ] `docs/reference/api/api.md` contains `::: your_package`.
- [ ] `uv run python -m zensical build` completes without errors.
- [ ] The built API page lists your functions with their arguments and descriptions.

## This Project's API

The reference below was generated automatically
from the docstrings in this guide's own Python code.
Nothing below this was typed by hand.

::: pro_analytics_02
options:
show_submodules: true
show_source: true

---

[◄ Back to 🏠 Guide Home](https://denisecase.github.io/pro-analytics-02/)
