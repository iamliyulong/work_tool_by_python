from util import http_util
from util import json_util
import json

data_list = []
get_url = "http://localhost:8080/asyncTest"
while True:
    # data = {
    #     "guid": "c19af883-080b-11e5-9e7b-c89cdc7a70da",
    #     "subLog": "N",
    #     "dataList": [
    #         {
    #             "name": "44444444444444444",
    #             "guid": "0416D635E9AE48F49BE8D4462C123414",
    #             "computerGuid": "8ED1D51D-5266-4BFD-A0FE-F8421B71EC6C4",
    #             "computerIp": "192.168.3.4",
    #             "computerIpLong": 3232236515,
    #             "computerName": "T2274",
    #             "computerIdentity": "5VY32CY1+0000",
    #             "eventUser": "superred4",
    #             "personName": "2274",
    #             "departmentName": "1111",
    #             "departmentCode": "01000000000000000000",
    #             "region": "220300",
    #             "clientTime": "2022-05-18 14:14:43",
    #             "serverTime": "2022-05-18 14:14:45",
    #             "hardDiskSerial": "1111"
    #         }
    #     ]
    # }
    # data_list.append(data)
    # if json_util.get_json_size_kb(data_list) > 2 * 1024:
    #     print(data_list)
    #     break
    http_util.request_get(get_url, None)

# request_body = json.dumps(data_list)
#
# post_url = "http://localhost:8080/receive_json"
# a = http_util.request_post(post_url, request_body)
# print(a)
