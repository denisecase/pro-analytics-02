# 🏞️ STREAMING DATA ONLY: Stop Kafka Service

> Stop Apache Kafka when you are done working.

<details>
<summary>WHY?</summary>

Apache Kafka should be stopped when the streaming work session is finished.

Stopping Kafka gracefully gives the local broker service time to shut down
cleanly instead of being interrupted suddenly.

A clean shutdown helps avoid leftover terminal processes, locked files, or
confusing errors the next time Kafka is started.

Even though Kafka usually stops when the VS Code terminal is closed,
stopping it intentionally is a good professional habit
when working with local services.

</details>

## When

- Whenever you are done working on a project that uses
  the Kafka message broker service.

## Stop Kafka With CTRL+c

Kafka runs in the foreground in the terminal where you started it.
Go to the terminal where Kafka is running (WSL if Windows user).

Press CTRL key and c key together (CTRL+c).

Wait for the command prompt to return.

## Next Work Session

The next time you work on this project:

1. Follow the [**start-kafka**](./start-kafka.md) process.
2. Leave the Kafka terminal open.
3. Run the Python producer and consumer from Python.

## Important

You only need to run [**install-kafka**](./index.md) once per machine.

Use [**start-kafka**](./start-kafka.md) each time you begin working.

Use [**stop-kafka**](./stop-kafka.md) when you finish a work session.
