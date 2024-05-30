
import sqlite3
from prettytable import PrettyTable, from_db_cursor

conn = sqlite3.connect("players.sqlite3")

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

prtyTbl = from_db_cursor(cursor)

print(prtyTbl)

conn.close()