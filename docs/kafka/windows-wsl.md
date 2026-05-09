# Windows and WSL

Windows users will need a special terminal just for running Kafka.

Two types of **terminals** in VS Code:

| Terminal       | Used for                                                       |
| -------------- | -------------------------------------------------------------- |
| **PowerShell** | Running Python (`uv run ...`), Git, everything project-related |
| **WSL (bash)** | Starting and stopping the Kafka broker only                    |

In most WSL2 setups, Windows can reach Kafka running in WSL at `localhost:9092`.

If Python cannot connect, verify Kafka is running and that
WSL port forwarding is available on your machine.
