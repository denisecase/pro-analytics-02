# 🏞️ STREAMING DATA ONLY: Manage Kafka Topics

Kafka topics are **infrastructure**.
They exist independently of any code.
They are created once, producers fill them, consumers read them.

## Prerequisites

Kafka must be running before any of these commands will work.
See [install-kafka.md](./install-kafka.md) if you have not set up Kafka yet.
See [start-kafka.md](./start-kafka.md) if you have not started Kafka yet.

## Windows Users

Run commands for Kafka and topics in **WSL**, not PowerShell.
The Kafka CLI scripts are `.sh` files and require a Linux shell.

## Open a Terminal (WSL if Windows)

Open a new VS Code terminal.
For example, from the menu select **Terminal / New Terminal**.

If running Windows, type the following command:

```powershell
wsl
```

Your prompt will change to something like `username@DESKTOP:~$`.
Do all steps in this WSL terminal.

## Recommended: Rename the Terminal to topics

In the VS Code terminal, look for an icon with the terminal type (e.g., `wsl`, `bash`, `zsh`).
Click the default name / Select "Change name".
Type the new name **topics**.

## Kafka Topics Shell Script (Provided)

`kafka-topics.sh` is a shell script.
A shell script runs in a terminal.
The shell script manages topics directly in the running Kafka service.

The script is provided in the `~/kafka/bin`.
Running `cd ~/kafka` first ensures you are always in the right place.

## Topic Commands

Every kafka-topics command follows the same pattern:

```shell
kafka-topics.sh  --flag  --argument value  --argument value ...
```

- `--flag` tells the script the action to take
- `--argument value` provides details for that action
- `--bootstrap-server` tells how to find the Kafka service

### Arguments

| Argument               | Required                 | Description                                                        |
| ---------------------- | ------------------------ | ------------------------------------------------------------------ |
| `--bootstrap-server`   | Always                   | Address of the Kafka broker. Use `localhost:9092` for local Kafka. |
| `--topic`              | create, describe, delete | The name of the topic to act on.                                   |
| `--partitions`         | create only              | Count of partitions to create. Use `1` for local development.      |
| `--replication-factor` | create only              | Count of message copies to keep. Use `1` for local development.    |

The `\` at the end of a line means the command continues on the next line.

---

## Create a Topic (Change Name as Needed)

Run this once before running a producer
that will send messages to this topic for the first time.

This is just an example.
**Change the name of the topic as needed.**

```bash
cd ~/kafka

bin/kafka-topics.sh --create \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1 \
  --topic streaming-02-kafka-case
```

## List Topics

The `--list` flag lists existing topics.

```bash
cd ~/kafka

bin/kafka-topics.sh --list \
  --bootstrap-server localhost:9092
```

## Describe a Topic

The `--describe` flag describes a topic.
It shows partition count, replication, leader, and current offsets.
Run this after a producer to see how many messages are stored.

```bash
cd ~/kafka

bin/kafka-topics.sh --describe \
  --bootstrap-server localhost:9092 \
  --topic streaming-02-kafka-case
```

## Delete a Topic (Change Name as Needed)

Deleting a topic removes all its messages permanently.
Use this to start completely fresh.

After deleting, recreate the topic before running a producer
that produces messages to this topic again.

This is just an example.
**Change the name of the topic as needed.**

```bash
cd ~/kafka

bin/kafka-topics.sh --delete \
  --bootstrap-server localhost:9092 \
  --topic streaming-02-kafka-case \
```

---

## Easy reference

**Change the name of the topic as needed.**

```bash
cd ~/kafka

bin/kafka-topics.sh --create \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1 \
  --topic streaming-02-kafka-case

bin/kafka-topics.sh --list \
  --bootstrap-server localhost:9092

bin/kafka-topics.sh --describe \
  --bootstrap-server localhost:9092 \
  --topic streaming-02-kafka-case

bin/kafka-topics.sh --delete \
  --bootstrap-server localhost:9092 \
  --topic streaming-02-kafka-case \
```
