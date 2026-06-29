# 🧮 LARGE-SCALE ONLY: Spark Setup

> Complete this once before starting any Spark or large-scale data processing project.

Apache Spark is a data processing engine used for analytics on larger or more complex datasets.
We can run Spark locally through Python using PySpark.

Spark does **not** need to be started and stopped like Kafka.
Once Java and the project dependencies are installed,
Spark starts when the Python script runs and stops when the script finishes.

This setup is done once and reused across Spark-related modules.
If Spark is already working on your machine, skip to Verify PySpark.

## Windows Users

If you are on Windows, read [Windows and WSL](windows-wsl.md) first.
Spark runs in WSL (Windows Subsystem for Linux) on Windows machines.
The setup steps are the same, but the terminal environment is different.

## What You Will Set Up

By the end of setting up Spark, you will have:

- Java JDK 17 installed
- `JAVA_HOME` set in your shell profile
- Python project dependencies installed with `uv`

**Note on SPARK_HOME:**
Do not set `SPARK_HOME`.
When PySpark is installed via `uv` or `pip`, Spark JARs are bundled inside
the Python package.
A `SPARK_HOME` pointing elsewhere causes a `FileNotFoundError` at runtime.
If `SPARK_HOME` is already set on your machine, unset it:

```bash
unset SPARK_HOME
```

## Step 1. Open a New Terminal in VS Code

Windows users:

- Read [Windows and WSL](../kafka/windows-wsl.md) first.
- Open a new WSL terminal in VS Code.
- For example, from the VS Code menu, select **Terminal / New Terminal**.
- Then run:

```bash
wsl
```

Your prompt will change to something like `username@DESKTOP:~$`.
Do all steps below in this WSL terminal.

All other users:

- Open a new terminal in VS Code.
- For example, from the VS Code menu, select **Terminal / New Terminal**.

## Step 2. Install Java 17+

Choose the option for your operating system.

<details>
<summary>Option 2A: Windows WSL / Ubuntu / Debian</summary>

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y openjdk-17-jdk curl wget
java --version
```

</details>

<details>
<summary>Option 2B: macOS</summary>

```bash
brew install openjdk@17
java --version
```

</details>

<details>
<summary>Option 2C: Red Hat / Fedora</summary>

```bash
sudo dnf install -y java-17-openjdk java-17-openjdk-devel curl wget
java --version
```

</details>

Expected output: `openjdk 17.x.x` or higher.

## Step 3. Detect and Set JAVA_HOME

PySpark needs `JAVA_HOME` to locate Java at runtime.
Detect the actual path first, then write it to your profile.

<details>
<summary>Option 3A: Windows WSL / Ubuntu / Debian (tested)</summary>

Tested on WSL.

```bash
# Detect the actual Java path
dirname $(dirname $(readlink -f $(which java)))
```

Use the output of that command as your path below.
Common values are `/usr/lib/jvm/java-17-openjdk-amd64` (AMD64)
or `/usr/lib/jvm/java-17-openjdk-arm64` (ARM64).

```bash
# Replace the path below with the output of the detect command above
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

</details>

<details>
<summary>Option 3B: macOS (please report any issues)</summary>

```bash
# Detect the actual Java path
/usr/libexec/java_home -v 17
```

```bash
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 17)' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

</details>

<details>
<summary>Option 3C: Red Hat / Fedora please report issues)</summary>

```bash
# Detect the actual Java path
dirname $(dirname $(readlink -f $(which java)))
```

```bash
# Replace the path below with the output of the detect command above
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk' >> ~/.bashrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

</details>

## Step 4. Verify JAVA_HOME and Path

```bash
echo "$JAVA_HOME"
"$JAVA_HOME/bin/java" --version
java --version
```

All three commands should succeed and show `openjdk 17.x.x`.
If the first two succeed but the third fails, your PATH is not updated.
Re-run `source ~/.bashrc` (Linux) or `source ~/.zshrc` (macOS).

## Step 5. Install Project Dependencies

Verify that pyproject.toml includes:

```toml
dependencies = [
    "pyspark",
]
```

Then install and upgrade dependencies with:

```shell
uv sync --upgrade
```

This installs PySpark and all other required Python packages.

## Step 6. Verify PySpark

Create this file in your main project package folder
and run it to verify.
Adjust paths as needed for your project.

```python

"""src/bizintel/sparktest.py - Verify PySpark installation.

Run with:
    uv run python src/bizintel/sparktest.py
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkTest").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

print(f"Spark version: {spark.version}")

data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
df = spark.createDataFrame(data, ["id", "name"])
df.show()

spark.stop()
print("PySpark is working.")
```

You should see the following:

```text
Spark version: 3.x.x
+---+-------+
| id|   name|
+---+-------+
|  1|  Alice|
|  2|    Bob|
|  3|Charlie|
+---+-------+
PySpark is working.
```

## Troubleshooting

<details>
<summary>Click for more information</summary>

### SPARK_HOME conflict

If you see:

```text
FileNotFoundError: [Errno 2] No such file or directory: '/opt/spark/./bin/spark-submit'
```

A `SPARK_HOME` variable is set on your machine pointing to a non-existent location.
Unset it for the current session:

```bash
unset SPARK_HOME
uv run python src/your_project/sparktest.py
```

To remove it permanently, delete the `export SPARK_HOME=...` line
from your `~/.bashrc` or `~/.zshrc`.

### Multiple JDK versions

If you have multiple JDK versions installed, select the active one:

```bash
sudo update-alternatives --config java
```

Then re-run Step 3 to detect and set `JAVA_HOME` for the version you selected.

### JAVA_HOME not found

If `echo "$JAVA_HOME"` prints nothing after sourcing your profile,
close and reopen the terminal and try again.
If it still fails, confirm the path from the detect command in Step 3
exists on disk:

```bash
ls "$JAVA_HOME"
```

</details>
