# 🏞️ STREAMING DATA ONLY: Managing Many Terminals in VS Code

Streaming projects require multiple terminals running at the same time.
Each terminal has a specific job.
This guide explains what each one is for and how to set them up.

## Why Multiple Terminals?

In a streaming system, different processes run independently and simultaneously.
Your laptop simulates this with separate terminals:

| Terminal                 | Job                            | After startup            |
| ------------------------ | ------------------------------ | ------------------------ |
| **Terminal 1: Kafka**    | Keeps the Kafka broker running | Minimize and leave alone |
| **Terminal 2: Topic**    | Create, inspect, delete topics | Close when done          |
| **Terminal 3: Producer** | Sends messages to the topic    | Watch while running      |
| **Terminal 4: Consumer** | Reads messages from the topic  | Watch while running      |

Terminals 1 and 2 are infrastructure setup.
Terminals 3 and 4 display live action to monitor.

## Opening a New Terminal in VS Code

Open a new VS Code terminal.
For example, from the menu select **Terminal / New Terminal**.
Or use the keyboard shortcut:

- Windows/Linux: Ctrl+` (backtick)
- Mac: Cmd+` (backtick)

Each new terminal opens as a tab at the bottom of the screen.
You can click the tab name to switch between terminals.
Rename a terminal by right-clicking its tab and choosing **Rename**.

## Open Terminal 1 to start Kafka (WSL if Windows)

Open your first terminal and start Kafka.
See [start-kafka.md](./start-kafka.md) for the exact command.

Once Kafka is running, you do not need to watch this terminal.
Leave it open in the background. **do not close it**.
Closing it stops Kafka.

## Open Terminal 2 to Create a Topic (WSL if Windows)

Open a second terminal (**Terminal / New Terminal**).
Use this terminal to create, inspect, and delete a topic.
See [create-topic.md](./create-topic.md) for the exact commands.

Once your topic exists, you can close this terminal or leave it in the background.

## Open Terminal 3 to Run the Producer

Open a third terminal (**Terminal / New Terminal**).
This is where you will run:

```shell
uv run python -m streaming.kafka_producer_case
```

### Open Terminal 4 to Run the Consumer

Open a fourth terminal (**Terminal / New Terminal**).
This is where you will run:

```shell
uv run python -m streaming.kafka_consumer_case
```

---

## Viewing the Producer and Consumer Side by Side

Once Kafka is running and your topic exists,
you want to watch the producer and consumer at the same time.
Here are two ways to do that.

### Option A. Split the terminal panel (simpler)

This keeps the terminal at the bottom and splits it into two side-by-side panes.

1. Close the file explorer to gain width: **View / Explorer** or `Ctrl+B`
2. Click on the producer terminal tab to make it active
3. Click the **split terminal** button in the top-right corner of the terminal panel
   (it looks like a rectangle split by a vertical line)
   or right-click the tab and choose **Split Terminal**
4. In the new right-hand pane, click the consumer terminal tab to bring it forward

You now have the producer on the left and the consumer on the right,
both visible at the same time at the bottom of the screen.

```text
┌─────────────────────────────────────────────┐
│                                             │
│           VS Code Editor Area               │
│         (file open here or empty)           │
│                                             │
├────────────────────┬────────────────────────┤
│  Terminal 3        │  Terminal 4            │
│  Producer          │  Consumer              │
│                    │                        │
│  > uv run python   │  > uv run python       │
│    -m streaming.   │    -m streaming.       │
│    producer_case   │    consumer_case       │
└────────────────────┴────────────────────────┘
```

### Option B. Full-width terminals replacing the editor (more space)

This moves your terminals into the editor area for maximum visibility.
Use this when you want to focus entirely on watching messages flow.

1. Close the file explorer: `Ctrl+B`
2. Right-click the **producer terminal tab** and choose **Move Terminal into Editor Area**
   The terminal now fills the editor space
3. Right-click the **consumer terminal tab** and choose **Move Terminal into Editor Area**
4. Drag one terminal tab to the right half of the screen to split them side by side

```text
┌────────────────────┬────────────────────────┐
│  Terminal 3        │  Terminal 4            │
│  Producer          │  Consumer              │
│                    │                        │
│  Sending message   │  Consumed message      │
│  key=US-MO ...     │  key=US-MO ...         │
│  Sending message   │  Consumed message      │
│  key=US-CA ...     │  key=US-CA ...         │
│                    │                        │
└────────────────────┴────────────────────────┘
```

To go back to editing files, drag the terminal tabs back down to the terminal panel
or open a file normally. VS Code will restore the editor area.

## Recommendations

- **Rename your terminals** so you always know which is which.
  Right-click a terminal tab and choose **Rename**.
  Suggested names: `kafka`, `topic`, `producer`, `consumer`

- **Do not close Terminal 1 (Kafka)** until you are completely done for the session.
  If Kafka stops, the producer and consumer will both fail.

- **Small laptop screen?**
  Drop the terminal font size to make more text visible:
  Open Settings (`Ctrl+,`), search **terminal font size**, and set it to 12 or 11.

- **Lost track of which terminal is which?**
  Click each tab and look at what command was last run.
  The terminal history stays visible until you close it.
