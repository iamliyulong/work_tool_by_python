import json
import random
import time

import mysql.connector

from util.kafka_util import send_message_with_key

topic = 'send7FE2233178B14FCEBB7B326BC9C8D543'  # 替换成你的Kafka主题名
key = 'asset'  # 替换成你的消息key

# Establish a connection to the database
connection = mysql.connector.connect(
    host="10.66.77.35",
    user="security",
    password="s2u1p3e4r",
    database="situation_manager"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()
sql = "select asset_id from tsec_asset"
cursor.execute(sql)
asset_ids = cursor.fetchall()

# 资产告警
alarm_data = []
# 对外服务域-交换机
for i in asset_ids:
    entry = {
        "assetId": i[0],
        "startTime": str(int(time.time() * 1000)),  # Current time in milliseconds
        "alarmName": "SNMP服务获取数据失败",
        "alarmType": "网络告警",
        "alarmDesc": "SNMP用户名错误",
        "alarmStatus": f'{random.choice([0, 1])}'
    }
    alarm_data.append(entry)

# alarm_tmp = {
#     "assetId": 'c12abe3e-3829-11ee-81aa-70321708e081',
#     "startTime": str(int(time.time() * 1000)),  # Current time in milliseconds
#     "alarmName": "SNMP服务获取数据失败",
#     "alarmType": "网络告警",
#     "alarmDesc": "SNMP用户名错误",
#     "alarmStatus": f'{random.choice([0, 1])}'
# }
# alarm_data.append(alarm_tmp)

json_alarm = {
    "updateTime": 1665986533836,
    "type": "alarm_info",
    "data": alarm_data
}

alarm_value = json.dumps(json_alarm, ensure_ascii=False)  # 替换成你的消息内容
# 发送消息到kafka
send_message_with_key(topic, key, alarm_value)
print(alarm_value)
