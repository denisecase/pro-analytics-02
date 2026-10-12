# ty: Check Python Code

> ty reads code without running it
> and reports mistakes.

**ty** is a Python type checker from Astral,
the makers of `uv` and `ruff`.
Run it as a project chore:

```shell
uv run ty check
```

A clean run ends with:

```text
All checks passed!
```

## Type Hints

A type hint is an optional note in code
about what kind of value a function takes or returns,
such as `def average(values: list[float]) -> float:`.
Python runs fine without them,
and you can add them as your projects grow.

ty reasons possible types from the code
(for example, given `name = "ada"` it knows that `name` is text).

### ty Catches Some Things Even Without Hints

Run on this code, which has no hints:

```python
import pandass


def add(a, b):
    return a + b


add(1)

name = "ada"
name.uppercase()

print(undefined_name)
```

ty reports:

```text
error[unresolved-import]: Cannot resolve imported module `pandass`
error[missing-argument]: No argument provided for required parameter `b` of function `add`
error[unresolved-attribute]: Object of type `Literal["ada"]` has no attribute `uppercase`
error[unresolved-reference]: Name `undefined_name` used when not defined
```

These are mistakes we might make frequently:
a misspelled import,
a missing argument,
a method that does not exist,
and a name that was never created.

### What ty Misses Without Hints

```python
def average(values):
    return sum(values) / len(values)


print(average([1, 2, 3]).upper())
```

ty passes this, even though a number has no `.upper()`.
With hints, ty can follow the types through:

```python
def average(values: list[float]) -> float:
    return sum(values) / len(values)


print(average([1, 2, 3]).upper())
```

```text
error[unresolved-attribute]: Object of type `float` has no attribute `upper`
```

So hints are not required, but they let ty (and your readers) catch more.
Add them where they help most:
functions other people will call,
and functions that take or return data.

## Read a ty Message

```text
error[missing-argument]: No argument provided for required parameter `b` of function `add`
  --> demo.py:13:1
   |
13 | add(1)
   | ^^^^^^
```

- `error` or `warning`: how serious it is. Fix both.
- `[missing-argument]`: the name of the rule that was broken.
- `demo.py:13:1`: the file, line, and column.
- The `^^^^^^` marks the code at fault.

## Common Messages

| Rule                                           | Usual cause                                                | What to try                                                    |
| ---------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------------------- |
| `unresolved-import`                            | Misspelled name, or the package is not installed           | Check the spelling. Then run `uv sync`, or `uv add <package>`. |
| `missing-argument`                             | A function was called with too few values                  | Compare the call to the `def` line.                            |
| `unresolved-attribute`                         | A method or attribute does not exist on that kind of value | Check the spelling and the library documentation.              |
| `unresolved-reference`                         | A name is used before it is created, or is misspelled      | Check the spelling, and where the name is defined.             |
| `invalid-assignment` / `invalid-argument-type` | A value does not match a declared type hint                | Fix the value, or the hint.                                    |

It is best to fix what the message points to.
It's finding bugs that can show up down the road.
We don't recommend adding comments to silence the checks.

Using modern tools to build high quality code is a differentiator.

<details markdown>
<summary>WHY?</summary>

Python reports many mistakes only when the faulty line runs,
which can be after a long data load.
A static type checker can find errors early, in seconds.

Running ty every time builds good professional habits:
read the tool's message, fix the cause, run it again.

</details>

## Verification

- [ ] `uv run ty check` ends with `All checks passed!`.
- [ ] You can explain what one ty message means and which line it points to.

---

[◄ Back to 🏠 Guide Home](https://denisecase.github.io/pro-analytics-02/)
