from kafka import KafkaProducer
import time
from tqdm  import tqdm
import json

producer = KafkaProducer(
        bootstrap_servers='15.164.210.200:19092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

for i in tqdm(range(10000)):
    msg = {"msg" : str(i) }
    
    producer.send('quickstart-events', msg)
    
    # 100 개 단위로 나눠서 flush() 하기
    if i % 100 == 99:
        producer.flush()
    time.sleep(0.01)

producer.flush()
