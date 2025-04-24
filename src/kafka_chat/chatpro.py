from kafka import KafkaProducer
import json
import time
import os

def create_producer(broker):
    return KafkaProducer(
        bootstrap_servers=[broker],
        value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode('utf-8'),
        linger_ms=5000  # 5초 단위로 메시지 전송
    )

def input_with_default(prompt, default):
    user_input = input(f"{prompt} (기본값: {default}): ")
    return user_input.strip() or default

def get_current_time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def cli():
    print("채팅 프로그램 - 메시지 발신자")
    
     # 환경변수에서 기본값 읽기
    default_broker = os.environ.get("KAFKA_CHAT_BROKER", "localhost:9092")
    default_topic = os.environ.get("KAFKA_CHAT_TOPIC", "quickstart-events")
    
    broker = input_with_default("브로커 주소", default_broker)
    topic = input_with_default("토픽 이름", default_topic)
    name = input_with_default("대화명", "anonymous")
    
    producer = create_producer(broker)
    
    print("메시지를 입력하세요. (종료시 'exit' 입력)")
    
    while True:
        msg = input(f"{name}: ")
        if msg.lower() == 'exit':
            producer.flush()  # 즉시 전송
            break
        
        data = {
            'name': name,
            'message': msg,
            'time': get_current_time_str()
        }
        
        producer.send(topic, value=data)
        # producer.flush()  # 즉시 전송

    print("채팅 종료")

if __name__ == "__main__":
    cli()
