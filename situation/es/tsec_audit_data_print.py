import random
from datetime import datetime


def generate_datetime():
    # return datetime.now().isoformat()
    # return datetime.utcnow().isoformat() + 'Z'
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")


# Generate a random IP address
def generate_ip_address():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


# Generate a random computer name
def generate_computer_name():
    prefixes = ["PC", "Laptop", "Workstation"]
    suffixes = ["1", "2", "3"]
    return random.choice(prefixes) + "-" + random.choice(suffixes)


# Generate a random value for a keyword field
def generate_keyword():
    keywords = ["value1", "value2", "value3", "value4", "value5"]
    return random.choice(keywords)


def generate_erase_flag():
    keywords = ["Y", "N"]
    return random.choice(keywords)


# 部门信息字典，用于关联赋值
department_mapping = [
    {'department_id': 69, 'department_code': '01009946136304171219', 'department_name': '第一所',
     'dep_detail': '厦门市公安厅-同安分局-第一所', 'region_id': '350212', 'region_name': '同安分局'},
    {'department_id': 19, 'department_code': '01009946136354692149', 'department_name': '政治处',
     'dep_detail': '厦门市公安厅-机场分局-政治处', 'region_id': '35020B', 'region_name': '机场分局'},
    {'department_id': 21, 'department_code': '01009946136356960243', 'department_name': '办公室',
     'dep_detail': '厦门市公安厅-公交分局-办公室', 'region_id': '35020C', 'region_name': '公交（地铁）分局'},
    # 添加其他部门的映射关系
]


# Generate a random value for a text field
def generate_text():
    texts = ["Lorem ipsum dolor sit amet", "consectetur adipiscing elit", "sed do eiusmod tempor",
             "incididunt ut labore et dolore magna aliqua"]
    return random.choice(texts)


# Generate a random integer
def generate_integer():
    return random.randint(1, 100)


# Generate test data based on the provided structure
def generate_test_data():
    data = {
        "audit_code_id": 8,
        "erase_flag": generate_erase_flag(),
        "network_env": 0,
        "computer_ip": generate_ip_address(),
        "file_md5": "ddf7a5aaa7b02d70a68bc589e08b0751",
        "copies": '1',
        "event_user": 'admin',
        "region_name": "测试区域",
        "file_name": '测试文稿666',
        "event_type_code": 'a',
        "level_id": 10,
        "local_flag": 'Y',
        "unit_guid": '1234567890',
        "is_successful": '成功打印',
        "computer_name": generate_computer_name(),
        "recognize_flag": 'Y',
        "computer_guid": '5ac6e0ae-4b62-11ec-a596-107b449f4e0e',
        "result": 'F',
        "dep_detail": random.choice(department_mapping)["dep_detail"],
        "department_code": random.choice(department_mapping)["department_code"],
        "department_id": random.choice(department_mapping)["department_id"],
        "department_name": random.choice(department_mapping)["department_name"],
        "device_name": 'Pantum-M7100DN-Series',
        "operation_type": "print",
        "server_time": generate_datetime(),
        "target": 'Kylin-Desktop',
        "person_name": '打印测试五号',
        "program": '更新操作系统',
        "subsys_id": 'A',
        "data_id": 1,
        "computer_ip_long": 3232286849,
        "police_type_id": 1,
        "computer_mac": ":".join("%02x" % random.randint(0, 255) for _ in range(6)),
        "product_type": "h",
        "client_time": generate_datetime(),
        "behavious_type_code": "NORMAL",
        "contents": '文档名称:[测试文稿1], 成功打印, 打印机名称:[Pantum-M7100DN-Series], 打印时间:[2021-04-08 14:35:33], 打印份数:[1], 页数:[2]',
        "computer_identity": "W9AC5Z9T+phytium_ft-1500a",
        "audit_sub_type": 0,
        "region_id": '35020A',
        "timestamp": '2021-04-08 14:35:33',
        "total_pages": '2',
        "critical_level_id": 6,
        "query1": 'PRINT'
    }
    return data
