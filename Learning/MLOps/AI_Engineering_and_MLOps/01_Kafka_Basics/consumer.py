from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "messages",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="my-python-consumer"
)

print("Waiting for messages...")

for message in consumer:
    print ("message received",message.value.decode("utf-8"))