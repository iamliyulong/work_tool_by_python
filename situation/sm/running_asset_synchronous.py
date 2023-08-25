import json
import random
import uuid

from util.kafka_util import send_message_with_key

topic = 'send7FE2233178B14FCEBB7B326BC9C8D543'  # 替换成你的Kafka主题名
key = 'asset'  # 替换成你的消息key
# 资产在线状态
asset_data = []
# 对外服务域-交换机
for i in range(1, 3):
    assetId = f'{uuid.uuid1()}'
    entry = {
        "assetId": assetId,
        "assetName": f'测试资产{assetId}',
        "assetIp": f'1.0.0.{i}',
        "assetCode": assetId,
        "dutyPerson": "1",
        "assetGroupId": '1',
        "onlineStatus": f'{random.choice([0, 1])}',
        "assetGroupName": '对外服务域',
        "assetVendorName": '曙光H620-G30S1',
        "assetOsName": '中科方德',
        "cpuInfo": '飞腾2000',
        "netCardNum": 1,
        "diskCapacity": '240SSD+2TBHDD',
        "memCapacity": '64GB',
        "purchaseTime": 1665986533836,
    }
    asset_data.append(entry)

# 对外服务域-服务器
for i in range(1, 18):
    assetId = f'{uuid.uuid1()}'
    entry = {
        "assetId": assetId,
        "assetName": f'测试资产{assetId}',
        "assetIp": f'2.0.0.{i}',
        "assetCode": assetId,
        "dutyPerson": "1",
        "assetGroupId": '2',
        "onlineStatus": f'{random.choice([0, 1])}',
        "assetGroupName": '对外服务域',
        "assetVendorName": '曙光H620-G30S1',
        "assetOsName": '中科方德',
        "cpuInfo": '飞腾2000',
        "netCardNum": 1,
        "diskCapacity": '240SSD+2TBHDD',
        "memCapacity": '64GB',
        "purchaseTime": 1665986533836,
    }
    asset_data.append(entry)

# 安全服务域-交换机
for i in range(1, 2):
    assetId = f'{uuid.uuid1()}'
    entry = {
        "assetId": assetId,
        "assetName": f'测试资产{assetId}',
        "assetIp": f'3.0.0.{i}',
        "assetCode": assetId,
        "dutyPerson": "1",
        "assetGroupId": '3',
        "onlineStatus": f'{random.choice([0, 1])}',
        "assetGroupName": '安全服务域',
        "assetVendorName": '曙光H620-G30S1',
        "assetOsName": '中科方德',
        "cpuInfo": '飞腾2000',
        "netCardNum": 1,
        "diskCapacity": '240SSD+2TBHDD',
        "memCapacity": '64GB',
        "purchaseTime": 1665986533836,
    }
    asset_data.append(entry)

# 安全服务域-服务器
for i in range(1, 4):
    assetId = f'{uuid.uuid1()}'
    entry = {
        "assetId": assetId,
        "assetName": f'测试资产{assetId}',
        "assetIp": f'4.0.0.{i}',
        "assetCode": assetId,
        "dutyPerson": "1",
        "assetGroupId": '4',
        "onlineStatus": f'{random.choice([0, 1])}',
        "assetGroupName": '安全服务域',
        "assetVendorName": '曙光H620-G30S1',
        "assetOsName": '中科方德',
        "cpuInfo": '飞腾2000',
        "netCardNum": 1,
        "diskCapacity": '240SSD+2TBHDD',
        "memCapacity": '64GB',
        "purchaseTime": 1665986533836,
    }
    asset_data.append(entry)

# 办公区域
for i in range(1, 19):
    assetId = f'{uuid.uuid1()}'
    entry = {
        "assetId": assetId,
        "assetName": f'测试资产{assetId}',
        "assetIp": f'5.0.0.{i}',
        "assetCode": assetId,
        "dutyPerson": "1",
        "assetGroupId": '5',
        "onlineStatus": f'{random.choice([0, 1])}',
        "assetGroupName": '办公区域',
        "assetVendorName": '曙光H620-G30S1',
        "assetOsName": '中科方德',
        "cpuInfo": '飞腾2000',
        "netCardNum": 1,
        "diskCapacity": '240SSD+2TBHDD',
        "memCapacity": '64GB',
        "purchaseTime": 1665986533836,
    }
    asset_data.append(entry)

# asset_data = [
#     {
#         "assetId": '1',
#         "assetName": '测试资产',
#         "assetIp": '5.0.0.1',
#         "assetCode": '1',
#         "dutyPerson": "1",
#         "assetGroupId": '1',
#         "onlineStatus": 1
#     }
# ]

json_asset = {
    "updateTime": 1665986533836,
    "type": "online_type",
    "data": asset_data
}

asset_value = json.dumps(json_asset, ensure_ascii=False)  # 替换成你的消息内容
# 发送消息到kafka
send_message_with_key(topic, key, asset_value)
print(asset_value)
