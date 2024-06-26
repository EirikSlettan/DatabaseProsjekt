import sqlite3
from utils import create_table

def find_colleagues(navn):
    con = sqlite3.connect("teater_database.db") #Endre dette
    cursor = con.cursor()
    cursor.execute('''SELECT DISTINCT a1.navn AS skuespiller1, a2.navn AS skuespiller2, akter.stykkenavn AS skuespill
FROM ansatt AS a1
INNER JOIN harrolle AS hr1 ON a1.ansattID = hr1.ansattID
INNER JOIN rolle AS r1 ON hr1.rolleID = r1.rolleID
INNER JOIN aktharrolle AS ahr1 ON r1.rolleID = ahr1.rolleID
INNER JOIN akter ON ahr1.aktnr = akter.aktnr AND ahr1.stykkenavn = akter.stykkenavn
INNER JOIN aktharrolle AS ahr2 ON akter.aktnr = ahr2.aktnr AND akter.stykkenavn = ahr2.stykkenavn
INNER JOIN rolle AS r2 ON ahr2.rolleID = r2.rolleID
INNER JOIN harrolle AS hr2 ON r2.rolleID = hr2.rolleID
INNER JOIN ansatt AS a2 ON hr2.ansattID = a2.ansattID
WHERE a1.navn != a2.navn AND a1.navn = ?;''', (navn,))
    
    create_table(cursor.fetchall(), ["Navn", "Spiller med", "Teaterstykke"])
