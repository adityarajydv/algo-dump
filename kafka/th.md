"""
===========================
WORKING PRINCIPLE OF KAFKA
===========================

Apache Kafka is a distributed event streaming platform designed for high-throughput, fault-tolerant, real-time data pipelines.

🔄 BASIC CONCEPTS:
------------------
1. **Producer**: Sends (publishes) data (messages) to Kafka.
2. **Topic**: A named stream of data. Messages are categorized into topics.
3. **Broker**: A Kafka server that stores data and serves clients.
4. **Partition**: Topics are split into partitions for scalability and parallelism.
5. **Consumer**: Reads (subscribes to) messages from topics.
6. **Consumer Group**: A group of consumers that coordinate to consume topic data in parallel.
7. **ZooKeeper (or KRaft)**: Manages cluster metadata (Kafka is moving away from ZooKeeper to its own KRaft mode).

⚙️ HOW IT WORKS:
----------------
1. **Producer sends messages** to a topic.
2. Kafka **writes the message to a partition** (based on key or round-robin).
3. Messages in partitions are **stored sequentially** and assigned an **offset**.
4. **Consumers read messages** by tracking their offset.
5. Kafka retains messages **for a configured time**, even after consumption.

💡 KEY FEATURES:
----------------
- High-throughput and fault-tolerant.
- Horizontally scalable via partitions and brokers.
- Can replay messages by seeking to older offsets.
- Works as a distributed commit log.

📦 USE CASES:
-------------
- Real-time analytics and monitoring
- Log aggregation
- Data pipeline (ETL)
- Event sourcing and stream processing

"""

# Example placeholder for Kafka usage (Producer/Consumer code can be added here)
