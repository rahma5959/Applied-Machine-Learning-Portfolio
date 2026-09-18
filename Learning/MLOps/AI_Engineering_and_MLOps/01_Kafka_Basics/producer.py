from kafka import KafkaProducer

producer=KafkaProducer(
    bootstrap_servers="localhost:9092"
)
message = "Hello from Python Producer"

producer.send("messages",message.encode("utf-8"))
producer.flush()

print("message sent!")
producer.close()
