# Kafka Setup (Only for Streaming Data)

> Complete this once before starting any streaming data project.

Apache Kafka is a message broker used in streaming data modules.
It runs as a local service on your machine and must be installed and
running before the Python producers or consumers can work.

This setup is done once and reused across all streaming modules.
If Kafka is already installed and working on your machine, skip to
[Start Kafka](start-kafka.md).

## Windows Users

If you are on Windows, read [Windows and WSL](windows-wsl.md) first.
Kafka runs in WSL (Windows Subsystem for Linux) on Windows machines.
The setup steps are the same, but the terminal environment is different.

## What You Will Set Up

By the end of setting up a Kafka project you will have:

- Kafka installed and configured on your machine
- The Kafka broker running as a local service
- A topic created for your project (used to broker messages)
- Four terminals open and ready:
  1. Kafka broker running (tab name: "kafka")
  2. Kafka topic management (tab name: "topics")
  3. Producer ready to send messages (tab name: "producer")
  4. Consumer ready to receive messages (tab name: "consumer")

## Set Up Tasks

1. [Install Kafka](install-kafka.md)
   Download and configure Kafka on your machine.
   One-time setup; once successful, we don't need to do this again.

2. [Open Terminals](many-terminals.md)
   Set up multiple terminals for the broker, producer, and consumer.
   Every course project requires multiple terminals.

## Working on a Kafka Project

Project instructions are provided with the project.
There will be additional tasks as you work through
[Workflow B: Apply Example Project](../workflow-b-apply-example-project/index.md).

## After Finishing a Work Session

Follow [Stop Kafka](stop-kafka.md)
to shut down the broker cleanly when you finish a work session.
Do not leave Kafka running.
Streaming analytics can keep running indefinitely.
**ALWAYS shut down** at the end of a work session.

## Troubleshooting

Kafka setup is the step where most issues occur.
Common problems include:

- Kafka not found in PATH
- Port 9092 already in use
- WSL not installed or not configured (Windows)
- Java not installed

When issues occur, share a screenshot of the error in the course channel.
Include the command you ran and the full error message.
Working through setup issues is part of the course.
