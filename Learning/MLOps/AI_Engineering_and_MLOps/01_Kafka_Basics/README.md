# Kafka Basics

This project is a beginner-friendly introduction to **Apache Kafka**, **Kafka Producer/Consumer**, and **Docker**.

The goal is to understand how applications can exchange messages through a Kafka broker before integrating Kafka into a larger MLOps / AI Engineering project.

## Project objective

The project demonstrates the basic Kafka communication flow:

```text
Python Producer
      ↓
   Kafka Broker
      ↓
   Kafka Topic
      ↓
Python Consumer
```

Kafka is used as a **message streaming platform** that allows producers and consumers to communicate without being directly connected to each other.

## Technologies

* Python
* Apache Kafka
* Docker
* Docker Compose
* `kafka-python`

## Project structure

```text
01_Kafka_Basics/
│
├── producer.py
├── consumer.py
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Docker setup

Kafka is running inside a Docker container.

The `docker-compose.yml` file defines the Kafka service:

```yaml
services:
  kafka:
    image: apache/kafka:latest
    ports:
      - "9092:9092"
```

The port `9092` allows Python applications running on Windows to communicate with Kafka inside Docker.

Start Kafka with:

```powershell
docker compose up -d
```

Check the running container:

```powershell
docker ps
```

Stop Kafka with:

```powershell
docker compose down
```

## Kafka topic

A Kafka **topic** is a logical channel where messages are stored.

This project uses the topic:

```text
messages
```

The topic was created with:

```powershell
docker exec -it 01_kafka_basics-kafka-1 /opt/kafka/bin/kafka-topics.sh --create --topic messages --bootstrap-server localhost:9092
```

## Console Producer and Consumer

Before using Python, the Kafka console tools were used to verify that the Kafka broker was working correctly.

### Console Producer

```powershell
docker exec -it 01_kafka_basics-kafka-1 /opt/kafka/bin/kafka-console-producer.sh --topic messages --bootstrap-server localhost:9092
```

Example message:

```text
Hello Kafka
```

### Console Consumer

In another terminal:

```powershell
docker exec -it 01_kafka_basics-kafka-1 /opt/kafka/bin/kafka-console-consumer.sh --topic messages --from-beginning --bootstrap-server localhost:9092
```

The consumer can then receive previously stored messages:

```text
hello kafka
Bonjour Kafka
My first Kafka message
Hello Kafka
```

This confirms that the Kafka broker and topic are working correctly.

## Python Producer

The Python Producer uses the `kafka-python` library.

Install the dependency:

```powershell
pip install kafka-python
```

The Producer connects to Kafka on port `9092` and sends a message to the `messages` topic.

Run:

```powershell
python producer.py
```

Example output:

```text
message sent!
```

The message sent by the Python Producer is:

```text
Hello from Python Producer
```

## Python Consumer

The Python Consumer connects to the same Kafka topic and waits for messages.

Run:

```powershell
python consumer.py
```

Example output:

```text
Waiting for messages...
Message received: Hello from Python Producer
```

The Consumer can also read messages that were already stored in the topic because the configuration uses:

```python
auto_offset_reset="earliest"
```

## What I learned

Through this project, I learned the fundamental Kafka concepts:

### Producer

A Producer sends messages to Kafka.

```text
Producer → Kafka
```

### Consumer

A Consumer reads messages from Kafka.

```text
Kafka → Consumer
```

### Broker

The Kafka Broker is the server responsible for receiving, storing, and delivering messages.

```text
Producer
    ↓
Kafka Broker
    ↓
Consumer
```

### Topic

A Topic organizes messages inside Kafka.

In this project:

```text
Topic = messages
```

### Offset

Kafka assigns a position called an **offset** to messages in a topic.

This allows consumers to keep track of which messages they have read.

## Final architecture

The current project architecture is:

```text
┌──────────────────────┐
│   Python Producer    │
└──────────┬───────────┘
           │
           │ Message
           ▼
┌──────────────────────┐
│    Kafka Broker      │
│   Docker Container   │
│                      │
│ Topic: messages      │
└──────────┬───────────┘
           │
           │ Message
           ▼
┌──────────────────────┐
│   Python Consumer    │
└──────────────────────┘
```

## Why Kafka for AI Engineering?

Kafka is useful when an application needs to handle a continuous flow of events or messages.

For example, in a future AI/MLOps application:

```text
User Request
     ↓
Flask API
     ↓
Kafka Producer
     ↓
Kafka Topic
     ↓
AI / LLM Worker
     ↓
Kafka Response Topic
     ↓
Flask API
     ↓
User
```

This architecture separates the web application from the AI processing component.

It can make the system more scalable and easier to extend.

## Next steps

This project is the first step toward a larger **AI Engineering and MLOps pipeline**.

Planned extensions:

* Kafka + Flask
* Kafka + Small Language Model
* Kafka + PySpark
* Kafka + Snowflake
* Dockerized AI services
* Automated testing with Pytest
* CI/CD with Jenkins
* Monitoring with Prometheus and Grafana

The final objective is to build a complete AI/MLOps application using these technologies together.
