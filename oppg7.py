import sqlite3
con = sqlite3.connect("test1.db") #Endre dette
cursor = con.cursor()

def find_actor(navn):

    cursor.execute("SELECT* FROM person WHERE navn = ?", (navn))

