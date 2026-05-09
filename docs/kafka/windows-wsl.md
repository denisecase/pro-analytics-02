# 🏞️ STREAMING DATA ONLY: Windows and WSL

> Windows users need WSL before installing Kafka.
> Complete this page before following the Kafka setup steps.

## What is WSL?

WSL (Windows Subsystem for Linux) lets you run a Linux terminal
directly on Windows.
Kafka runs natively on Linux and macOS.
On Windows, it runs inside WSL.

## Do You Already Have WSL?

Open PowerShell and run:

```powershell
wsl --status
```

If you see a version and distribution name, WSL is already installed.
Skip to [Verify WSL Works](#verify-wsl-works) below.

If you see an error, continue with the installation steps.

## Install WSL

In PowerShell (run as Administrator):

```powershell
wsl --install
```

Restart your machine when prompted.

## Verify WSL Works

Open PowerShell and start a WSL session:

```powershell
wsl
```

Your prompt should change to show a Linux shell (something like `username@machine:~$`).
Type `exit` to return to PowerShell.

## Two Terminal Types in VS Code

Once your project is open in VS Code, you will use two types of terminals:

| Terminal       | Used for                                                 |
| -------------- | -------------------------------------------------------- |
| **PowerShell** | Running Python (`uv run ...`), Git, all project commands |
| **WSL (bash)** | Starting and stopping Kafka, managing topics             |

## How to Open a WSL Terminal in VS Code

To open a WSL terminal in VS Code, either:

- Click the `+` arrow in the terminal panel
  and select **WSL** from the dropdown.

OR

- Open a PowerShell terminal and run:

```shell
wsl
```

## After Completing This Page

Return to [Install Kafka](./install-kafka.md) and continue.
