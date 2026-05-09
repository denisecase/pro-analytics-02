# Kafka Topics

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

## Reliable and Scalable

Streaming systems must be reliable; they cannot lose messages.
Steaming systems must be scalable; sometimes one machine is enough,
and sometimes a massive cluster (group) of many machines is required.

Each topic has a name,
one or more partitions (a way of dividing messages for processing),
and a **replication factor** (how many times the topic is duplicated for reliability).

For local development we use **one partition and one replica**.
