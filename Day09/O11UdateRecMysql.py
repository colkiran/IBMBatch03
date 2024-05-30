

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="playersdb", port=3306)

cursor = conn.cursor()

query = "update player set plyname = 'Pusarla Venkata Sindhu' where plyid = 'PLY520'"

cursor.execute(query)

conn.commit()
conn.close()