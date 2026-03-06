# Tips for Working with Python and VS Code

## VS Code Navigation

- **Explorer (files):** Use the Explorer icon on the left to browse files and folders.
- **Open file quickly:** Use `Ctrl+P` (or `Cmd+P`) to search and open a file by name.
- **Command Palette:** Use `Ctrl+Shift+P` (or `Cmd+Shift+P`) to access any VS Code command.


## VS Code Terminal Tips

- Use the terminal command `clear` to clear output.
- Use the **UP ARROW** key and **DOWN ARROW** key to scroll through past commands.


## Find and Replace (in a file)

- **Find:** `Ctrl+F` (or `Cmd+F`)
- **Replace:** `Ctrl+H` (or `Cmd+H`)


## Find and Replace (across the whole project)

- **Find in files:** `Ctrl+Shift+F` (or `Cmd+Shift+F`)
- **Replace in files:** `Ctrl+Shift+H` (or `Cmd+Shift+H`)

Global changes can have unintended consequences.
Review changes carefully and prefer smaller, incremental edits.

## Python Interpreter (Important)

If Python features do not behave correctly (linting, imports, type hints), the interpreter may not be set to the project environment.

- Open the Command Palette
- Select **Python: Select Interpreter**
- Choose the interpreter inside this project `.venv` folder
- If things still look wrong, run **Developer: Reload Window**

Tip: The selected interpreter typically appears in the bottom status bar when a Python file is open.
