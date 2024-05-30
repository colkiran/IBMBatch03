
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="playersdb", port=3306)

cursor = conn.cursor()

query = """
create table player (
plyid varchar(6) PRIMARY KEY,
plyname varchar(50) not null,
sport varchar(30) not null, 
acheivement varchar(50) not null
)
"""

cursor.execute(query)

conn.close()
