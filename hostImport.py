import mysql.connector

# Establish a connection to the database
connection = mysql.connector.connect(
    host="10.66.77.40",
    user="security",
    password="s2u1p3e4r",
    database="host_manager"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Loop to generate 400 rows
for i in range(1, 401):
    computer_ip = f"192.168.188.{i}"  # Update the computer_ip value
    computer_mac = f"00-0C-29-74-81-{i:02}"  # Update the computer_mac value
    computer_guid = f"061301-{i:03}"  # Update the computer_guid value

    # Execute the modified SQL statement
    computerSql = f"""
    INSERT INTO host_manager.tseccomputer
    (computer_id, computer_name, computer_ip, computer_mac, computer_ip_long, computer_guid,
    register_time, modify_time, last_logon_time, online_flag, department_code, region_id,
    department_name, version, old_version, manage_person, person_id, department_id,
    agent_version, computer_gateway, asset_number, user_name, hardware_serial, unit_name,
    operating_system, cpu_arch, product, remark, sec_level, sub_system, active_flag,
    active_time, active_department_code, extend1, extend2, extend3, person_name, osname,
    osdesc, osversion, usbkey_reg, reg_update, person_id_card, os_install_time,
    computer_type, tel, installation_progress, use_person, office_number, unit_id,
    vendor, machine, soc_num, net_use, is_general, plain_password, encrypted_password,
    stored_key, server_key, salt, iterations, clean_flag, lock_flag, computer_short_code,
    os_version_id, agent_state, exit_whether, memos, department_detail, computer_location,
    person_guid, computer_os_type, terminal_type, user_mode, config_ver, cascade_flag,
    cascade_server_ip, clean_tool_is_hide_client)
    VALUES
    ({i}, '测试主机{i}', '{computer_ip}', '{computer_mac}', 12151515, '{computer_guid}',
    NULL, NULL, NULL, 'Y', '01001640000000000000', '000000', '关联融合一测试部门1', NULL, NULL, '测试人员1',
    2, 2, NULL, NULL, NULL, '测试人员1', NULL, NULL, NULL, NULL, NULL, NULL, 0, 'H', 'N',
    NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', NULL, NULL, NULL, NULL, 4, NULL,
    1, NULL, NULL, '', NULL, 2, NULL, 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, NULL, 'N', NULL, NULL, NULL, NULL, NULL, 3, 2, 0, '1', NULL, 'OFF');
    """

    softwareTriadSql = f"""
    INSERT INTO host_manager.tsec_computer_software
    (software_name, active_flag, active_time, online_flag, register_time, last_logon_time, 
    version, old_version, secret_level, memos, computer_guid, sub_system, subsystem_computer_guid)
    VALUES
    ('融合一', 'Y', '2023-06-19 00:00:00.000', 'Y', '2023-06-19 00:00:00.000', '2023-06-19 00:00:00.000', 
    '1.0', NULL, NULL, NULL, '{computer_guid}', 'triad', NULL);
    """

    softwareTerminalSql = f"""
        INSERT INTO host_manager.tsec_computer_software
        (software_name, active_flag, active_time, online_flag, register_time, last_logon_time, 
        version, old_version, secret_level, memos, computer_guid, sub_system, subsystem_computer_guid)
        VALUES
        ('安全登录', 'Y', '2023-06-19 00:00:00.000', 'Y', '2023-06-19 00:00:00.000', '2023-06-19 00:00:00.000', 
        '1.0', NULL, NULL, NULL, '{computer_guid}', 'terminal', NULL);
        """

    softwareAuditSql = f"""
        INSERT INTO host_manager.tsec_computer_software
        (software_name, active_flag, active_time, online_flag, register_time, last_logon_time, 
        version, old_version, secret_level, memos, computer_guid, sub_system, subsystem_computer_guid)
        VALUES
        ('主机审计', 'Y', '2023-06-19 00:00:00.000', 'Y', '2023-06-19 00:00:00.000', '2023-06-19 00:00:00.000', 
        '1.0', NULL, NULL, NULL, '{computer_guid}', 'audit', NULL);
        """

    # softwarePrintSql = f"""
    #     INSERT INTO host_manager.tsec_computer_software
    #     (software_name, active_flag, active_time, online_flag, register_time, last_logon_time,
    #     version, old_version, secret_level, memos, computer_guid, sub_system, subsystem_computer_guid)
    #     VALUES
    #     ('打印刻录', 'Y', '2023-06-19 00:00:00.000', 'Y', '2023-06-19 00:00:00.000', '2023-06-19 00:00:00.000',
    #     '1.0', NULL, NULL, NULL, '{computer_guid}', 'print', NULL);
    #     """

    softwareServerSql = f"""
        INSERT INTO host_manager.tsec_computer_software
        (software_name, active_flag, active_time, online_flag, register_time, last_logon_time,
        version, old_version, secret_level, memos, computer_guid, sub_system, subsystem_computer_guid)
        VALUES
        ('服务器审计', 'Y', '2023-06-19 00:00:00.000', 'Y', '2023-06-19 00:00:00.000', '2023-06-19 00:00:00.000',
        '1.0', NULL, NULL, NULL, '{computer_guid}', 'server', NULL);
        """

    cursor.execute(computerSql)
    cursor.execute(softwareTriadSql)
    cursor.execute(softwareTerminalSql)
    cursor.execute(softwareAuditSql)
    # cursor.execute(softwarePrintSql)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
