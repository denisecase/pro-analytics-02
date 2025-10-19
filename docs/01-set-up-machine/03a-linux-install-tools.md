# 🟢 Linux: Install Tools

This page provides instructions to install or verify **Python**, **Git**, and **Visual Studio Code** on a **Linux** machine using standard package managers.
These tools are essential for professional data analytics.

## 1. Use Built-in Package Manager (Recommended for Most Users)

Open a terminal and run the following commands:

```bash
sudo apt update
sudo apt install -y python3 python3-pip git
```

To install VS Code, follow the official instructions to add the Microsoft repository: <https://code.visualstudio.com/docs/setup/linux>.
Once set up, install VS Code with:

```bash
sudo apt install code
```

## 2. Restart Computer After Installation

Restart your computer after installation (optional but recommended).

## 3. Verify

After restarting, open a new Terminal and run the following commands to verify.

```bash
python3 --version
pip3 --version
git --version
code --version
```

IMPORTANT: Each command should return a version number.
If any fail, revisit the installers and try again.

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Install Advanced Tooling (uv)</strong></summary>

These tools are modern, high-performance alternatives to traditional Python tools:

- `uv` replaces `pip` and `venv` with a much faster dependency and environment manager.
- `ruff` replaces `flake8`, `black`, and more with a single ultra-fast linter and formatter.

Install `uv` globally (once per machine):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:

```bash
uv --version
```

NOTE: These are **not required** for most users.
You'll need `uv` to try the advanced option in the project initialization workflow.
Install `ruff` with each project (later).

</details>

---

<details>
<summary><strong>OPTIONAL/ADVANCED: Install Multiple Versions of Python with pyenv</strong></summary>

This is not typically needed.
Only continue with this section if you need to add an earlier version of Python (e.g. to use with complex tools such as Kafka or Spark).

Advanced users may use pyenv to manage multiple Python versions.
Run the following to install pyenv and related tools:

```bash
sudo apt install -y build-essential curl zlib1g-dev libbz2-dev libssl-dev libreadline-dev libsqlite3-dev
curl https://pyenv.run | bash
```

Follow the shell setup instructions printed at the end.
Then restart your terminal and run:

```bash
pyenv install 3.11.11
```

We can specify the desired Python version when creating a project virtual environment in the next workflow.

</details>

