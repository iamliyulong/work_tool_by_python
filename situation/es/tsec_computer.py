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


def generate_active_flag():
    keywords = ["Y", "N"]
    return random.choice(keywords)


def generate_clean_flag():
    keywords = ["Y", "N"]
    return random.choice(keywords)


def generate_tel():
    keywords = ["13522465248", "12547854128"]
    return random.choice(keywords)


def generate_erase_flag():
    keywords = ["Y", "N"]
    return random.choice(keywords)


def generate_online_flag():
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


# Generate a random boolean flag
def generate_flag():
    return random.choice([True, False])


# Generate a random integer
def generate_integer():
    return random.randint(1, 100)


# Generate test data based on the provided structure
def generate_test_data(computer_guid):
    data = {
        "@timestamp": generate_datetime(),
        "@version": "1",
        "active_flag": generate_active_flag(),
        "active_time": generate_datetime(),
        "agent_state": "NORMAL",
        "agent_version": random.randint(1, 100),
        "agentversion": random.randint(1, 100),
        "clean_flag": "N",
        "client_ip": generate_ip_address(),
        "computer_guid": computer_guid,
        "computer_ip": generate_ip_address(),
        "computer_ip_long": random.randint(0, 4294967295),
        "computer_mac": ":".join("%02x" % random.randint(0, 255) for _ in range(6)),
        "computer_name": generate_computer_name(),
        "computer_short_id": random.randint(1, 100),
        "data2": generate_text(),
        "data3": generate_text(),
        "data_guid": generate_text(),
        "dep_detail": random.choice(department_mapping)["dep_detail"],
        "department_code": random.choice(department_mapping)["department_code"],
        "department_id": random.choice(department_mapping)["department_id"],
        "department_name": random.choice(department_mapping)["department_name"],
        "encipher_flag": generate_keyword(),
        "encryptedpassword": "51fed4fd4606471f4ed43a94be15caac41e3a16e1403f11679cf2cb4bbfb314e91aa6bcc9a221585",
        "encryption_result": generate_integer(),
        "erase_flag": generate_erase_flag(),
        "hardware_serial": generate_keyword(),
        "host_exit_status": generate_text(),
        "install_status": 1,
        "iterations": random.randint(1, 100),
        "last_logon_time": generate_datetime(),
        "local_flag": "Y",
        "lock_flag": "N",
        "manage_person": f"测试{computer_guid}",
        "memos": generate_keyword(),
        "modify_time": generate_datetime(),
        "network_env": 0,
        "office_number": generate_keyword(),
        "old_version": random.randint(1, 100),
        "online_flag": generate_online_flag(),
        "openfire_server_guid": generate_text(),
        "os_inst_time": generate_datetime(),
        "os_name": generate_keyword(),
        "os_version": generate_keyword(),
        "plainpassword": generate_keyword(),
        "police_type_id": random.randint(1, 100),
        # "reg_update": generate_keyword(),
        "region_id": random.choice(department_mapping)["region_id"],
        "region_name": random.choice(department_mapping)["region_name"],
        "register_time": generate_datetime(),
        # "salt": generate_keyword(),
        "serverkey": generate_keyword(),
        "storedkey": generate_keyword(),
        "tel": generate_tel(),
        # "type_name": generate_keyword(),
        "unit_guid": generate_keyword(),
        # "usbkey_reg": generate_keyword(),
        "use_person": generate_keyword(),
        "version": random.randint(1, 100)
    }
    return data
