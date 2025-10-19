# The src/ Folder

In the src folder, create folders for project packages. 

## Folder Naming Conventions

Follow Python conventions and name folders with: 

- lowercase letters.
- underscores. 

For example: `analytics_project`

It is part of the Python weirdness that, when published, folders that use UNDERSCORES are typically converted to DASHES on package indexes like PyPI. 

- So a src/ folder named:  `analytics_project`
- Becomes a package named: `analytics-project`

## Make it a Package

To turn a folder into an importable Python package, add a file named: `__init__.py`.

It can be empty.

This special "dunders" (double-underscores) file tells Python that the folder is a package, and that the modules inside can be imported and reused.

## It's Just Python

Don't worry about things like this.
If we know the rules, we can follow them.
