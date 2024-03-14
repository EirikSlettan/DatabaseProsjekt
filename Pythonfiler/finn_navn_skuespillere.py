import sqlite3
from utils import create_table

def finn_navn_skuespillere():
    con = sqlite3.connect("test1.db")
    cursor = con.cursor()
    cursor.execute('''SELECT DISTINCT teaterstykke.navn AS yoyo, 
        ansatt.navn AS skuespiller, 
        rolle.rollenavn AS rolle

FROM teaterstykke
INNER JOIN akter ON teaterstykke.navn = akter.stykkenavn
INNER JOIN aktharrolle ON akter.aktnr = aktharrolle.aktnr
        AND akter.stykkenavn = aktharrolle.stykkenavn
INNER JOIN rolle ON rolle.rolleID = aktharrolle.rolleID
INNER JOIN harrolle ON rolle.rolleID = harrolle.rolleID
INNER JOIN ansatt ON ansatt.ansattID = harrolle.ansattID''')
    result = cursor.fetchall()
    create_table(result, ["Teaterstykke", "Skuespiller", "Rolle"])
    