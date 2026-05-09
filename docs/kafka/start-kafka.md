# 🏞️ STREAMING DATA ONLY: Start Kafka Message Broker Service

> Start **Apache Kafka 4.2** locally using `confluent-kafka` package.

## Prerequisites

REQUIREMENT 1. Complete <mark>**SETUP_KAFKA.md**</mark> successfully.

REQUIREMENT 2. Copy
**.env.example** (committed to GitHub) to
<mark>**.env**</mark> (not committed to GitHub as it could have secrets).

REQUIREMENT 3. WINDOWS ONLY: in `.env` and `.env.example`,
**uncomment this line**:

```text
KAFKA_BROKER_ADDRESS_FAMILY=v6
```

WHY: On Windows with WSL2, `localhost` resolves to `::1` (IPv6).
The default `any` tries IPv4 first, which fails.
Setting `v6` tells the Kafka client to use IPv6 directly.

## When

- After completing SETUP_KAFKA.md for the first time.
- Again, whenever you are working on a project that uses
  the Kafka message broker service.

## Windows Users

Run commands in **WSL**, not PowerShell.

## Open a Terminal (WSL if Windows)

Open a new VS Code terminal.
For example, from the menu select **Terminal / New Terminal**.

If running Windows, type the following command:

```powershell
wsl
```

Your prompt will change to something like `username@DESKTOP:~$`.
Do all steps in this WSL terminal.

## Recommended: Rename the Terminal to kafka

In the VS Code terminal, look for an icon with the terminal type (e.g., `wsl`, `bash`, `zsh`).
Click the default name / Select "Change name".
Type the new name **kafka**.

## Step 1. (WSL if Windows) Verify Java

Verify Java is available in this terminal.
Then start the kafka broker service.

```shell
echo "$JAVA_HOME"
"$JAVA_HOME/bin/java" --version
```

If you get **`java: command not found`**
Java is not installed or not on your PATH.
Work through **SETUP_KAFKA.md** and verify each step.
The remaining steps will not work until
`java --version` returns a number.

## Step 3. (WSL if Windows) Rebuild Cluster ID (as needed)

You must have Java installed and on the path
and you must be in the ~/kafka folder for these commands to work.
Run each command by itself.

```shell
cd ~/kafka

rm -rf /tmp/kraft-combined-logs

KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

echo "Cluster ID: $KAFKA_CLUSTER_ID"

bin/kafka-storage.sh format --standalone -t "$KAFKA_CLUSTER_ID" -c config/server.properties
```

## Step 4. (WSL if Windows) Start Kafka Server

```shell
cd ~/kafka

bin/kafka-server-start.sh config/server.properties
```

## SUCCESS

The last line of output should look something like this:

```shell
[KafkaRaftServer nodeId=1] Kafka Server started (kafka.server.KafkaRaftServer)
```

## KEEP TERMINAL OPEN AND THE SERVICE RUNNING

**Keep this terminal open and do not use it for any other commands.**
It is running the Kafka service.
If this terminal is closed or you exit VS Code, it will stop the Kafka service.
The Kafka service must be running when working on a Kafka project.

Keep Kafka running in that original terminal.
In VS Code, you'll see a list of active terminals in icons
down the right side of the VS Code terminal window.

For every Kafka project, you will need to start Kafka and
have it running in its own terminal while working on the project.

Open a new terminal in VS Code to work on Python as usual.

---

## Troubleshooting and Common Issues

**Port 9092 already in use**
Another Kafka process may still be running.
Find and stop it:

```bash
# Linux / WSL
sudo lsof -i :9092
sudo kill <PID>
```

**Storage already formatted (re-running Step 4)**
If you see `Log directory /tmp/kraft-combined-logs is already formatted`,
either delete the directory and reformat, or skip formatting - it is already ready.

```bash
rm -rf /tmp/kraft-combined-logs
# then rerun the format command
```

**Windows: Python cannot connect to Kafka**
Confirm you are running the Python command in **PowerShell**, not in WSL.
WSL2 bridges `localhost:9092` automatically - no extra configuration needed.
