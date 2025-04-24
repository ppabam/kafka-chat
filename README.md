# kafka-chat

# uses
- 생산자
```bash
$ export KAFKA_CHAT_BROKER=15.164.210.200:19092
$ export KAFKA_CHAT_TOPIC=quickstart-events
chatpro
채팅 프로그램 - 메시지 발신자
브로커 주소 (기본값: 15.164.210.200:19092): 
토픽 이름 (기본값: quickstart-events): 
대화명 (기본값: anonymous): 
메시지를 입력하세요. (종료시 'exit' 입력)
anonymous: 가나다라마바사
anonymous: 안녕하세요
```

- 소비자

# test
```bash
$ $KAFKA_HOME/bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server 15.164.210.200:19092

{"name": "anonymous", "message": "가나다라마바사", "time": "2025-04-24 15:22:09"}
{"name": "anonymous", "message": "안녕하세요", "time": "2025-04-24 15:22:14"}
```