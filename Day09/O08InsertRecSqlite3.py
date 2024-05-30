
import sqlite3

conn = sqlite3.connect("players.sqlite3")

cursor = conn.cursor()

FL = open("playersdb.txt", "r")

for line in FL.readlines():
    cursor.execute(line)
FL.close()

conn.commit()
conn.close()