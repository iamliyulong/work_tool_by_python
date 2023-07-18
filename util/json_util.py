"""
json工具模块
"""

import json


def get_json_size_kb(data):
    """
    获取json数据的大小，单位KB
    :param data:
    :return:
    """
    json_str = json.dumps(data)
    print(len(json_str))
    return json_str
