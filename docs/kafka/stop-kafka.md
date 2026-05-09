# STOP_KAFKA.md

> Stop Apache Kafka when you are done working.

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

1. Follow the `START_KAFKA.md` process.
2. Leave the Kafka terminal open.
3. Run the Python producer and consumer from Python.

## Important

You only need to run `SETUP_KAFKA.md` once per machine.

Use `START_KAFKA.md` each time you begin working.

Use `STOP_KAFKA.md` when you are done.
