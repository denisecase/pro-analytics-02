# 🏞️ STREAMING DATA ONLY: Start Kafka Message Broker Service

> Start **Apache Kafka 4.2** locally using `confluent-kafka` package.

<details>
<summary>WHY?</summary>

Apache Kafka must be running before topics, producers, and consumers can
work.

The Kafka broker service manages topics, accepts messages from producers,
and makes messages available to consumers.

**Starting Kafka** at the beginning of each streaming project session is
necessary so the local message broker is available while project messages
are flowing.

**Keeping Kafka running** during the work session is necessary because topics,
producers, and consumers depend on the broker service.

**Restarting Kafka** after closing the VS Code terminal or VS Code is necessary
because closing the terminal automatically stops the local Kafka service.

</details>

## Prerequisites

1. Complete <mark>[**install-kafka**](./index.md)</mark> successfully.
2. Copy **.env.example** (committed) to <mark>**.env**</mark> (not committed, possible secrets).
3. If **Windows** only: in `.env` and `.env.example`, **uncomment this line**:

   Remove the leading # to uncomment it:

   ```text
   KAFKA_BROKER_ADDRESS_FAMILY=v6
   ```

   WHY: On Windows with WSL2, `localhost` resolves to `::1` (IPv6).
   The default `any` tries IPv4 first, which fails.
   Setting `v6` tells the Kafka client to use IPv6 directly.

## Windows Users

Use **WSL** terminals for Kafka and topics.
Use **PowerShell** terminals for the project, producers, and consumers.

## Open a Terminal (WSL if Windows)

Open a new VS Code terminal.
For example, from the menu select **Terminal / New Terminal**.
If running Windows, specify the terminal type as **wsl** or
type `wsl`.
Your prompt will change to something like `username@DESKTOP:~$`.

### Recommended: Rename the Terminal to `kafka`

In the VS Code terminal, look for an icon with the terminal type (e.g., `wsl`, `bash`, `zsh`).
Click the default name / Select "Change name".
Type the new name **kafka**.

## Step 1. (WSL if Windows) Verify Java

Verify Java is available in this terminal.

```shell
echo "$JAVA_HOME"

"$JAVA_HOME/bin/java" --version
```

If you get **`java: command not found`**
Java is not installed or not on your PATH.
Work through [**install-kafka**](./index.md) and verify each step.
The remaining steps will not work until
`java --version` returns a number.

## Step 2. (WSL if Windows) Rebuild Cluster ID (as needed)

You must have Java installed and on the path.
You must be in the `~/kafka` folder for these commands to work.
Run each command by itself by pasting into your terminal
and hitting Enter or Return. Inspect the output.

```shell
cd ~/kafka

rm -rf /tmp/kraft-combined-logs

KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

echo "Cluster ID: $KAFKA_CLUSTER_ID"

bin/kafka-storage.sh format --standalone -t "$KAFKA_CLUSTER_ID" -c config/server.properties
```

## Step 3. (WSL if Windows) Start Kafka Server

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

**Storage already formatted (re-running Step 2)**
If you see `Log directory /tmp/kraft-combined-logs is already formatted`,
either delete the directory and reformat, or skip formatting - it is already ready.

```bash
rm -rf /tmp/kraft-combined-logs
# then rerun the format command
```
