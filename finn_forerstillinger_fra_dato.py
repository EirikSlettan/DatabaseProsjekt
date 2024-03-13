import sqlite3
import math

def print_result(result, dato):
    x = "="
    y = 25
    print(f"{x * y} Oversikt over solgte billetter {dato} {x * y}")
    for row in result:
        print(f"Tid: {row[0]}, Dato: {row[1]}, Navn: {row[2]}, Billetter solgt: {row[3]}")
    print(f"{x *(93)}")
    

def finn_forestillinger(dato):
    con = sqlite3.connect("test1.db")
    cursor = con.cursor()
    
    cursor.execute('''SELECT tid, dato, teaterstykke, count(billettID) AS  antall 
                   FROM(forestilling FULL OUTER JOIN billett ON stykkenavn = teaterstykke AND tid = forestillingstid AND dato = forestillingsdato) 
                   WHERE dato = ?  GROUP BY tid, dato, stykkenavn;''',  (dato,))
    result = cursor.fetchall();
    
    con.close()
    print_result(result, dato) #Printer resultatet
    
    return result

finn_forestillinger('2024-02-03')

