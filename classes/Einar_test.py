import sqlite3
con = sqlite3.connect("database.db")

print(True)

cursor = con.cursor()
cursor.execute("SELECT * FROM rolle")

table = cursor.fetchall()

print(table)

con.close()