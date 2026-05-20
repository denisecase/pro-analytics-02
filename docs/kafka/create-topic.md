# 🏞️ STREAMING DATA ONLY: Create a Kafka Topic

> Create a topic for the project

<details>
<summary>WHY?</summary>

A Kafka topic gives the project a named place to send specific streaming messages.

Creating a project topic keeps those messages separate from
other projects, examples, and tests.

A producer must know the topic name and ensure the topic exists
**before** sending messages to that topic.

A topic must exist **before** a consumer can begin
consuming messages from that topic.

</details>

## Step 1. Open a New Terminal in VS Code

Windows users:

- Read [Windows and WSL](../kafka/windows-wsl.md) first.
- Open a new WSL terminal in VS Code.
- For example, from the VS Code menu, select **Terminal / New Terminal**.

Your prompt will change to something like `username@DESKTOP:~$`.
IMPORTANT: Do all steps below in this WSL terminal.

All other users:

- Open a new VS Code terminal.
- For example, from the menu select **Terminal / New Terminal**.

## Step 2. Rename Your Terminal Tab to topics

Right-click on your terminal tab name (e.g. wsl, bash, or zsh).
Select **Rename** (or hit F2) and change the name to **topics**.

## Step 3. Create a Topic (Change Name as Needed)

Each module project will provide a recommended name for the topic.
The following commands create the first topic we use (in Module 2): **streaming-02-kafka-case**.

```bash
cd ~/kafka

bin/kafka-topics.sh --create \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1 \
  --topic streaming-02-kafka-case
```

## Step 4. Verify

Use the `--list` flag to see existing topics.

```bash
cd ~/kafka

bin/kafka-topics.sh --list \
  --bootstrap-server localhost:9092
```

## Success

If `streaming-02-kafka-case` shows up in the list,
you have successfully created a Kafka topic.
We can now broker messages between analytics applications.

If not, retrace your steps.
Verify each step as you go and use the course discussions to get help.

---

## More About Topics

A Kafka topic is a named **stream of messages** stored on the Kafka broker.

**Producers write messages into** the topic.

**Consumers read messages from** the topic.

## Topic Messages

Messages are stored in the topic
in the order they arrive and stored until explicitly deleted.

A consumer can always go back and read the topic from the beginning.

## Distributed and Decoupled

We run a producer and a consumer together for convenience.
But in reality, the producer may be running on a website in Utah.
The consumer may be running in a commercial cloud.

Using topics means producers and consumers do not need to know anything about the other.
The system is distributed, with analytics running far
from where the messages are created.

All they need to communicate is the location and name of the topic.

Our Kafka broker is hosted on our machine with the same address for all projects.

Each project uses a unique topic name for messages.
See your project README.me for the suggested topic name.

## Reliable and Scalable

Streaming systems must be reliable; they cannot lose messages.
Steaming systems must be scalable; sometimes one machine is enough,
and sometimes a massive cluster (group) of many machines is required.

Each topic has a name,
one or more partitions (a way of dividing messages for processing),
and a **replication factor** (how many times the topic is duplicated for reliability).

For local development we use **one partition and one replica**.

## IMPORTANT: Manage Topics

See [Manage Topics](./manage-topics.md) for
detailed instructions on how to create more topics,
how to delete them and start fresh,
and how to list all topics,
and how to get more information about a topic
(including how many messages are on the topic).
