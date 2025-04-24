from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'quickstart-events',
    bootstrap_servers=['15.164.210.200:19092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

def cli():
    print("컨슈머 시작...")
    for message in consumer:
        print(f"Topic: {message.topic}, Partition: {message.partition}, Offset: {message.offset}, Key: {message.key}, Value: {message.value}")

if __name__ == "__main__":
    cli()