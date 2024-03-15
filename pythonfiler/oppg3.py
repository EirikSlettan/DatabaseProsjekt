import sqlite3
from utils import create_table

def list_opp_forestillinger(svar):
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    
    cursor.execute('''SELECT dato, tid, teaterstykke FROM forestilling WHERE teaterstykke = ? ORDER BY dato, tid DESC;''', (svar,))
    result = cursor.fetchall()
    create_table(result, ["Dato", "Tid", "Navn"])

def finn_ledige_rader(dato, tid, stykke, antall_seter):
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    
    cursor.execute('''select sete.rad, sete.omraade, sete.salnavn, count(billettID) as c 
from (billett FULL OUTER JOIN sete 
ON (billett.setenr = sete.setenr 
AND billett.rad = sete.rad 
AND sete.omraade = billett.omraade
 AND billett.salnavn = sete.salnavn)) 
 FULL OUTER JOIN forestilling 
 ON billett.forestillingsdato = forestilling.dato
 AND billett.forestillingstid = forestilling.tid
 AND billett.stykkenavn = forestilling.teaterstykke
WHERE mobilnummer is NULL 
AND forestilling.dato = ?
AND forestilling.tid = ?
AND forestilling.teaterstykke = ?
 GROUP BY sete.rad, sete.omraade, sete.salnavn 
 HAVING c >=? ORDER BY sete.omraade, sete.rad ASC;''',  (dato, tid, stykke, antall_seter))
    result = cursor.fetchall()
    
    con.close()
    create_table(result, ["Rad", "Omraade", "Navn", "Ledige"]) #Printer resultatet

