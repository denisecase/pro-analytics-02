# The src/ Folder

In the src folder, create a folder for the project package.

## Folder Naming Conventions

Follow Python conventions and name folders with lowercase letters and underscores.
For example: `pro_analytics_02`

It is part of Python weirdness that, when published,
folders that use UNDERSCORES are typically converted
to DASHES on package indexes like PyPI.

- So a src/ folder named:  `pro_analytics_02`
- Becomes a package named: `pro-analytics-02`

## Make it a Package

To turn a folder into an importable Python package,
just add a file named: `__init__.py`.
It can be empty.

This special "dunders" (double-underscores) file tells Python
that the folder is a package, and that the modules
inside can be imported and reused.

## It's Just Python

Don't worry about things like this.
Once we know the rules, we can follow them.
