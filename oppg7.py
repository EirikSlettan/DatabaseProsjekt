import sqlite3
con = sqlite3.connect("test1.db") #Endre dette
cursor = con.cursor()

def find_actor(name):

    cursor.execute("SELECT * FROM person WHERE navn")
