import sqlite3
from utils import create_table

def finn_forestillinger(dato):
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    
    cursor.execute('''SELECT tid, dato, teaterstykke, count(billettID) AS  antall 
                   FROM(forestilling FULL OUTER JOIN billett ON stykkenavn = teaterstykke AND tid = forestillingstid AND dato = forestillingsdato) 
                   WHERE dato = ?  GROUP BY tid, dato, stykkenavn;''',  (dato,))
    result = cursor.fetchall()
    
    con.close()
    create_table(result, ["Tid", "Dato", "Navn", "Solgt"]) #Printer resultatet

