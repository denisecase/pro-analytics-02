# Streaming Data ONLY: Install Kafka Message Broker

> Set up **Apache Kafka** locally.

## Step 0. Windows Users: Use WSL

Windows users, read [Windows and WSL](../kafka/windows-wsl.md) first.

Open a WSL terminal in VS Code, open a new terminal and run:

```powershell
wsl
```

Your prompt will change to something like `username@DESKTOP:~$`.

IMPORTANT: Do all steps below in this WSL terminal.

## Step 1. Install Java 17+

Kafka 4.2 supports Java 17, 21, and 25.
We recommend Java 17 because it is likely the most stable baseline required
for Kafka 4.x and is widely available across machines.

Choose the option for your operating system.

### Option 1A: Windows WSL / Ubuntu / Debian

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y openjdk-17-jdk curl wget
java --version
```

### Option 1B: macOS

```bash
brew install openjdk@17
java --version
```

### Option 1C: Red Hat / Fedora

```bash
sudo dnf install -y java-17-openjdk java-17-openjdk-devel curl wget
java --version
```

Expected output: `openjdk 17.x.x` or higher.

## Step 2. Set JAVA_HOME

Kafka scripts may use `JAVA_HOME`.
Set it once so future terminals can find Java reliably.

### Option 2A. Windows WSL / Ubuntu / Debian

```bash
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Option 2B. macOS Apple Silicon

```bash
echo 'export JAVA_HOME=/opt/homebrew/opt/openjdk@17' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Option 2C. macOS Intel

```bash
echo 'export JAVA_HOME=/usr/local/opt/openjdk@17' >> ~/.zshrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Option 2D. Red Hat / Fedora

```bash
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk' >> ~/.bashrc
echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## Step 3. Verify JAVA_HOME and Path

Verify JAVA_HOME, Path, and version:

```bash
echo "$JAVA_HOME"
"$JAVA_HOME/bin/java" --version
java --version
```

## Step 4. Download Kafka

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

## Step 5. Extract and Set Up Kafka

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

## Step 6. Configure Kafka

```bash
echo "$JAVA_HOME"
"$JAVA_HOME/bin/java" --version
cd ~/kafka
```

Generate a unique cluster ID

```shell
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
echo "Cluster ID: $KAFKA_CLUSTER_ID"
```

IMPORTANT: verify you get an actual value for the Cluster ID.

Format storage using the standalone config

```shell
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
```

Expected output: UUID printed, then `Formatting /tmp/kraft-combined-logs` like this:

```text
Bootstrap metadata: BootstrapMetadata(records=[ApiMessageAndVersion(FeatureLevelRecord(name='metadata.version', featureLevel=29) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='eligible.leader.replicas.version', featureLevel=1) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='group.version', featureLevel=1) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='share.version', featureLevel=1) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='streams.version', featureLevel=1) at version 0), ApiMessageAndVersion(FeatureLevelRecord(name='transaction.version', featureLevel=2) at version 0)], metadataVersionLevel=29, source=format command)
Formatting dynamic metadata voter directory /tmp/kraft-combined-logs with metadata.version 4.2-IV1.
```

Note: Kafka 4.x uses `config/server.properties` with the `--standalone` flag.
Older instructions that reference `config/kraft/server.properties` are for Kafka 3.x.
