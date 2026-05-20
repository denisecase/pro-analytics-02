# 🏞️ STREAMING DATA ONLY: Install Kafka Message Broker

> Set up **Apache Kafka** locally.

This may be challenging, but it is a one-time process.
Once we get it set up successfully, we use it throughout the course.

<details>
<summary>WHY?</summary>

Apache Kafka provides a local message broker for practicing streaming data
workflows.

Running Kafka locally gives a project a controlled place to create, send,
receive, and inspect streaming messages without using cloud services,
credit cards, or external accounts.

In many organizations, managing Apache Kafka is typically more data
engineering or platform engineering work.

Local Kafka setup supports streaming analytics experimentation, technical
practice, and skill development.

</details>

## Step 1. Open a New Terminal in VS Code

Windows users:

- Read [Windows and WSL](../kafka/windows-wsl.md) first.
- Open a new WSL terminal in VS Code.
- For example, from the VS Code menu, select **Terminal / New Terminal**.

Run the following command:

```pwsh
wsl
```

Your prompt will change to something like `username@DESKTOP:~$`.
IMPORTANT: Do all steps below in this WSL terminal.

All other users:

- Open a new terminal in VS Code.
- For example, from the VS Code menu, select **Terminal / New Terminal**.

## Step 2. Rename Your Terminal Tab to kafka

Right-click on your terminal tab name (e.g. wsl, bash, or zsh).
Select **Rename** (or hit F2) and change the name to **kafka**.

## Step 3. Install Java 17+

Kafka 4.2 supports Java 17, 21, and 25.
We recommend Java 17 because it is likely the most stable baseline required
for Kafka 4.x and is widely available across machines.

Choose the option for your operating system.

### Option 3A: Windows WSL / Ubuntu / Debian

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y openjdk-17-jdk curl wget
java --version
```

### Option 3B: macOS

```bash
brew install openjdk@17
java --version
```

### Option 3C: Red Hat / Fedora

```bash
sudo dnf install -y java-17-openjdk java-17-openjdk-devel curl wget
java --version
```

Expected output: `openjdk 17.x.x` or higher.

## Step 4. Set JAVA_HOME

Kafka scripts may use `JAVA_HOME`.
Set it once so future terminals can find Java reliably.

### Option 4A. Windows WSL / Ubuntu / Debian

**IMPORTANT:** If your Java installs to a different location,
you must use that path instead.

```bash
# OPTION A (most users) if Windows (AMD) your path may look like this:
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc

# OPTION B for Windows (ARM), it may be:
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64' >> ~/.bashrc


echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.bashrc

source ~/.bashrc
```

### Option 4B. macOS Apple Silicon

**IMPORTANT:** If your Java installs to a different location,
you must use that path instead.

```bash
echo 'export JAVA_HOME=/opt/homebrew/opt/openjdk@17' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Option 4C. macOS Intel

**IMPORTANT:** If your Java installs to a different location,
you must use that path instead.

```bash
echo 'export JAVA_HOME=/usr/local/opt/openjdk@17' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Option 4D. Red Hat / Fedora

**IMPORTANT:** If your Java installs to a different location,
you must use that path instead.

```bash
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk' >> ~/.bashrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## Step 5. Verify JAVA_HOME and Path

Verify JAVA_HOME, Path, and version:

```bash
echo "$JAVA_HOME"
"$JAVA_HOME/bin/java" --version
java --version
```

## Step 6. Download Kafka

Use the commands below to:

1. change directory (cd) to home directory (~)
2. download the tar gzip (.tgz) file
3. list the properties for the file to verify

```bash
cd ~

curl -O https://downloads.apache.org/kafka/4.2.0/kafka_2.13-4.2.0.tgz

ls -la kafka_2.13-4.2.0.tgz
```

Expected output: File listed at approximately 136 MB.

**If the download fails**, try the mirror:

```bash
curl -O https://archive.apache.org/dist/kafka/4.2.0/kafka_2.13-4.2.0.tgz
```

## Step 7. Extract and Set Up Kafka

Run the commands below one at a time to:

1. extract the file contents
2. remove (rm) the kafka folder
3. rename (mv) the versioned folder to just `kafka`
4. cd into the new kafka directory
5. change permissions to allow execute of the script files (.sh)
6. verify by listing contents of bin dir (first 10 lines)

```bash
tar -xzf kafka_2.13-4.2.0.tgz

rm -rf kafka

mv kafka_2.13-4.2.0 kafka

cd ~/kafka

chmod +x bin/*.sh

ls bin/ | head -10
```

Expected output:

Script files including `kafka-server-start.sh`, `kafka-topics.sh`, etc.

## Step 8. Configure Kafka

```bash
echo "$JAVA_HOME"

"$JAVA_HOME/bin/java" --version
```

Generate a unique cluster ID.
IMPORTANT: verify you get an actual value for the Cluster ID.
Then, format storage using the standalone config.

```shell
cd ~/kafka

KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

echo "Cluster ID: $KAFKA_CLUSTER_ID"

bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
```

## Step 9. One-Time Edit to server.properties

Use the following commands to edit the
Kafka server.properties file and:

1. Find the listeners line and update it
2. Find the advertised.listeners line and update it (or add if missing)

```bash
cd ~/kafka

sed -i 's|^listeners=PLAINTEXT://.*|listeners=PLAINTEXT://0.0.0.0:9092,CONTROLLER://localhost:9093|' ~/kafka/config/server.properties


grep -q "^advertised.listeners" ~/kafka/config/server.properties \
  && sed -i 's|^advertised.listeners=.*|advertised.listeners=PLAINTEXT://localhost:9092|' ~/kafka/config/server.properties \
  || echo "advertised.listeners=PLAINTEXT://localhost:9092" >> ~/kafka/config/server.properties

clear

cat ~/kafka/config/server.properties
```

## Success

Celebrate if you see the
expected output:
UUID printed, then `Formatting /tmp/kraft-combined-logs` like this:

```text
Bootstrap metadata: BootstrapMetadata(records=[ApiMessageAndVersion(FeatureLevelRecord(name='metadata.version', featureLevel=29) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='eligible.leader.replicas.version', featureLevel=1) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='group.version', featureLevel=1) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='share.version', featureLevel=1) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='streams.version', featureLevel=1) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='transaction.version', featureLevel=2) at version 0)], metadataVersionLevel=29, source=format command)
Formatting dynamic metadata voter directory /tmp/kraft-combined-logs with metadata.version 4.2-IV1.
```

If things don't work, try a web search or LLM AI.
Share your commands, results, and screenshots in the course discussions
and we can help.
