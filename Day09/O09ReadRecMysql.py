
import pymysql
from prettytable import prettytable, from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="playersdb", port=3306)

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

prtyTbl = from_db_cursor(cursor)

prtyTbl.align['plyname'] = 'l'
prtyTbl.align['sport'] = 'l'
prtyTbl.align['acheivement'] = 'r'

print(prtyTbl)

conn.close()