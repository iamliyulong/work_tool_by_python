import json

from util.kafka_util import send_message_with_key

topic = 'send66B53717875E48D48AAD6691EB9E3FB2'  # 替换成你的Kafka主题名
key = 'asset'  # 替换成你的消息key
# 资产在线状态
json_asset = {
    "updateTime": 1665986533836,
    "type": "online_type",
    "data": [
        {
            "assetId": "1639181433828290562",
            "assetName": "测试资产35",
            "assetIp": "10.66.77.40",
            "assetCode": "35",
            "dutyPerson": "1",
            "onlineStatus": 0
        },
        {
            "assetId": "1639181433828290563",
            "assetName": "测试资产31",
            "assetIp": "10.66.77.31",
            "assetCode": "31",
            "dutyPerson": "1",
            "onlineStatus": 0
        }
    ]
}

# 监控告警信息
json_alarm = {
    "updateTime": 1665986533836,
    "type": "alarm_info",
    "data": [
        {
            "assetId": "1639181433828290562",
            "startTime": "1665986533836",
            "alarmName": "SNMP服务获取数据失败",
            "alarmType": "网络告警",
            "alarmDesc": "SNMP用户名错误",
            "alarmStatus": 0
        },
        {
            "assetId": "1639181433828290562",
            "startTime": "1665986533836",
            "alarmName": "SNMP服务获取数据失败",
            "alarmType": "网络告警",
            "alarmDesc": "SNMP用户名错误",
            "alarmStatus": 0
        },
        {
            "assetId": "1639181433828290563",
            "startTime": "1665986533836",
            "alarmName": "SNMP服务获取数据失败",
            "alarmType": "网络告警",
            "alarmDesc": "SNMP用户名错误",
            "alarmStatus": 1
        }
    ]
}

asset_value = json.dumps(json_asset, ensure_ascii=False)  # 替换成你的消息内容
alarm_value = json.dumps(json_alarm, ensure_ascii=False)  # 替换成你的消息内容
# 发送消息到kafka
send_message_with_key(topic, key, asset_value)
