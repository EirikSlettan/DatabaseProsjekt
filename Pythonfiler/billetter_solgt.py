import sqlite3
from utils import create_table

def finn_billetter_solgt():
    con = sqlite3.connect("test1.db")
    cursor = con.cursor()
    cursor.execute('''  SELECT teaterstykke, 
        dato, 
        tid,
        count(billettID) AS solgt 
 FROM (forestilling 
 FULL OUTER JOIN billett ON forestillingsdato = dato 
 AND forestillingstid = tid AND stykkenavn = teaterstykke) 
 GROUP by teaterstykke, dato, tid  
 ORDER BY solgt DESC;''')
    result = cursor.fetchall()
    create_table(result, ["Teaterstykke", "Dato", "Tid", "Solgt"])