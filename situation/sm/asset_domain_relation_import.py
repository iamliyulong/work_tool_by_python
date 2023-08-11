import mysql.connector

from situation.database import situation_manager

# Establish a connection to the database
connection = mysql.connector.connect(
    host="10.66.77.35",
    user="security",
    password="s2u1p3e4r",
    database="situation_manager"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Loop to generate 400 rows
# 对外服务域-交换机
for i in range(1, 3):
    doamin1 = situation_manager.tsec_asset_domain_relation_insert(1, i)
    cursor.execute(doamin1)
# 对外服务域-服务器
for i in range(1, 18):
    doamin2 = situation_manager.tsec_asset_domain_relation_insert(2, i)
    cursor.execute(doamin2)
# 安全服务域-交换机
for i in range(1, 2):
    doamin3 = situation_manager.tsec_asset_domain_relation_insert(3, i)
    cursor.execute(doamin3)
# 安全服务域-服务器
for i in range(1, 4):
    doamin4 = situation_manager.tsec_asset_domain_relation_insert(4, i)
    cursor.execute(doamin4)
# 办公区域
for i in range(1, 19):
    doamin5 = situation_manager.tsec_asset_domain_relation_insert(5, i)
    cursor.execute(doamin5)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
