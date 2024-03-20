import sqlite3
from utils import create_table

def finn_billetter_solgt(): #Returnerer hvor mange billetter som har blitt solgt for hver forestilling
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    cursor.execute('''  SELECT teaterstykke, 
        dato, 
        tid,
        count(billettID) AS solgt 
 FROM (forestilling 
 FULL OUTER JOIN billett ON forestillingsdato = dato 
 AND forestillingstid = tid AND stykkenavn = teaterstykke)
 WHERE mobilnummer NOT NULL 
 GROUP by teaterstykke, dato, tid  
 ORDER BY solgt DESC;''')
    result = cursor.fetchall()
    con.close()
    create_table(result, ["Teaterstykke", "Dato", "Tid", "Solgt"])
    