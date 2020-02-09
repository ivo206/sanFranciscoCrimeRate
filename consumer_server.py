from kafka import KafkaConsumer
import asyncio



BROKER_URL = "PLAINTEXT://localhost:9092"

async def consume(topic_name):
   
    consumer = KafkaConsumer(topic_name, group_id='consumer-server', bootstrap_servers="localhost:9092")

    while True:
        for message in consumer:
            print(message.value)

        await asyncio.sleep(0.01)


def main():
    try:
        asyncio.run(consume("pd.service.calls"))
    except KeyboardInterrupt as e:
        print("Shut down")


if __name__ == "__main__":
    main()