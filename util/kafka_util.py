import json

from kafka import KafkaProducer

# Kafka集群的地址和端口
bootstrap_servers = ['10.66.77.35:9092']

# 创建KafkaProducer实例
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         sasl_mechanism="SCRAM-SHA-256",
                         security_protocol='SASL_PLAINTEXT',
                         sasl_plain_username="admin",
                         sasl_plain_password="admin-secret")


# 发送带有key的消息
def send_message_with_key(topic, key, value):
    key_bytes = bytes(key, 'utf-8')
    value_bytes = bytes(value, 'utf-8')
    producer.send(topic, key=key_bytes, value=value_bytes)
    producer.flush()
    producer.close()


# 测试发送消息
if __name__ == "__main__":
    topic = 'send66B53717875E48D48AAD6691EB9E3FB2'  # 替换成你的Kafka主题名
    key = 'asset'  # 替换成你的消息key
    json_value = {
        "updateTime": 1665986533836,
        "type": "online_type",
        "data": [
            {
                "assetId": "1639181433828290563",
                "assetName": "测试资产",
                "assetIp": "127.0.0.1",
                "assetCode": "123",
                "dutyPerson": "1",
                "onlineStatus": 1
            }
        ]
    }
    value = json.dumps(json_value, ensure_ascii=False)  # 替换成你的消息内容

    send_message_with_key(topic, key, value)
