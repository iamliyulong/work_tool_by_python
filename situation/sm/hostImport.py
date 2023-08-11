import mysql.connector

from situation.database import host_manager

# Establish a connection to the database
connection = mysql.connector.connect(
    host="10.66.77.35",
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

    computerSql = host_manager.tseccomputer_insert(i, i, computer_ip, computer_mac, computer_guid)

    # 融合一
    softwareTriadSql = host_manager.tsec_computer_software_insert("融合一", "triad", computer_guid)

    # 安登
    softwareTerminalSql = host_manager.tsec_computer_software_insert("安全登录", "terminal", computer_guid)

    # 主审
    softwareAuditSql = host_manager.tsec_computer_software_insert("主机审计", "audit", computer_guid)

    # 打刻
    softwarePrintSql = host_manager.tsec_computer_software_insert("打印刻录", "print", computer_guid)

    # 服审
    softwareServerSql = host_manager.tsec_computer_software_insert("服务器审计", "server", computer_guid)

    cursor.execute(computerSql)
    cursor.execute(softwareTriadSql)
    cursor.execute(softwareTerminalSql)
    cursor.execute(softwareAuditSql)
    cursor.execute(softwarePrintSql)
    cursor.execute(softwareServerSql)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
