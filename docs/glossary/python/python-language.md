# Python Language Glossary

> Core Python language concepts.

## Script

A `.py` file containing Python instructions that execute top to bottom when run.

## Module

A single Python `.py` file that can be imported by other files.

## Package

A folder of Python modules with an `__init__.py` file that makes it importable.
Example: a folder named `cintel` containing `case_logic.py` and `__init__.py`
is imported as `from cintel.case_logic import run`.

## Import

A Python statement that loads code from another module or package.
Examples:

- `import pandas as pd`
- `from cintel.case_logic import run`

## main()

A conventional function that serves as the entry point of a script.
Called at the bottom of a script with:

```python
if __name__ == "__main__":
    main()
```

## Function

A named, reusable block of code that takes inputs and returns outputs.
Defined with `def`.

## Parameter

A variable in a function definition that receives a value when the function is called.

## Argument

The actual value passed to a function when it is called.

## Return Value

The output a function sends back to the caller using `return`.

## Variable

A named storage location for a value.

## Assignment

Binding a value to a variable name using `=`.
Example: `threshold = 3.5`

---

## String (str)

A text value written in quotes.
Examples: `"hello"`, `'sensor_id'`

## Integer (int)

A whole number value.
Example: `42`

## Float (float)

A decimal number value.
Example: `3.14`

## Boolean (bool)

A `True` or `False` value.
Used in conditions, filtering, and logic.

## None

A special Python value representing the absence of a value.
Similar to NULL in other languages.

## List

An ordered, mutable collection of values.
Example: `[1, 2, 3]`

## Dictionary (dict)

A collection of key-value pairs.
Example: `{"name": "Alice", "score": 98.5}`

## Tuple

An ordered, immutable collection of values.
Example: `(1, 2, 3)`

---

## Conditional (if/elif/else)

A statement that executes different code depending on whether a condition is True or False.

## Loop (for / while)

A statement that repeats a block of code.
`for` iterates over a sequence; `while` repeats while a condition is True.

## Boolean Expression

An expression that evaluates to True or False.
Example: `temperature > 100`

## Comparison Operator

An operator that compares two values and returns a Boolean.
Examples: `==`, `!=`, `>`, `<`, `>=`, `<=`

## Logical Operator

An operator that combines Boolean expressions.
Examples: `and`, `or`, `not`

---

## Exception

An error that occurs during program execution.
Can be caught and handled with `try / except`.

## try / except

A block that attempts code and catches errors if they occur.
Prevents the program from crashing on expected failure conditions.

## f-string (Formatted String Literal)

A Python string that embeds variable values using `{}`.
Example: `f"Temperature is {temp:.2f} degrees"`

## Comment

A line in code beginning with `#` that Python ignores.
Used to explain intent to human readers.

## Type Hint

An optional annotation indicating the expected type of a variable or function parameter.
Example: `def run(filepath: str) -> None:`
Improves readability and enables static type checking tools like Pylance.
