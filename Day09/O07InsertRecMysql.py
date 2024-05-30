
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="playersdb", port=3306)

cursor = conn.cursor()

FL = open("playersdb.txt", "r")

for line in FL.readlines():
    cursor.execute(line)
FL.close()

conn.commit()
conn.close()