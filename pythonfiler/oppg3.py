import sqlite3
from utils import *
from time import *

def list_opp_forestillinger(svar):
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    #print(f"SELECT dato, tid, teaterstykke FROM forestilling WHERE teaterstykke = {svar} ORDER BY dato, tid DESC;")
    
    cursor.execute('''SELECT dato, tid, teaterstykke FROM forestilling WHERE teaterstykke = ? ORDER BY dato, tid DESC;''', (svar,))
    result = cursor.fetchall()
    create_table(result, ["Dato", "Tid", "Navn"])

def finn_ledige_rader(dato, tid, stykke, antall_seter):
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    
    cursor.execute('''select sete.rad, sete.omraade, sete.salnavn, count(billettID) as c 
from (billett INNER JOIN sete 
ON (billett.setenr = sete.setenr 
AND billett.rad = sete.rad 
AND sete.omraade = billett.omraade
 AND billett.salnavn = sete.salnavn)) 
INNER JOIN forestilling 
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

    return result
    # create_table(result, ["Rad", "Omraade", "Navn", "Ledige"]) #Printer resultatet

def kjop_billetter(rad, antall, omraade, salnavn, type_billett, mobilnummer):
    datotid = localtime()
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    kjopsdato = strftime("20%y-%m-%d", datotid)
    kjopstid  = strftime("%H:%M:%S", datotid)
    
    insert_into_table("billettkjop", [kjopsdato, kjopstid, mobilnummer])
      
    seter = cursor.execute('''SELECT billettID from billett 
                            WHERE mobilnummer is NULL AND rad = ? AND omraade = ? AND salnavn = ? LIMIT ? ;''', (rad, omraade, salnavn, antall))
    
    seter = seter.fetchall()
    for sete in seter:
        cursor.execute('''UPDATE billett  SET 
                       kjopsdato = ?, 
                       kjopstid = ?, 
                       mobilnummer = ?, 
                       billettgruppe = ? WHERE billettID = ?
                       ''', (kjopsdato, kjopstid, mobilnummer, type_billett, sete[0]))
    con.commit()
    con.close()
    return finn_pris(seter, salnavn)    

def finn_pris(billetter, salnavn):
    stykke = finn_stykke_fra_salnavn(salnavn)
    total_sum = 0
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    for billett in billetter:
        billettID = billett[0]
        cursor.execute('''SELECT pris FROM billettgruppe WHERE gruppe = 
                       (SELECT billettgruppe FROM billett WHERE billettID = ?) AND stykkenavn = ?''', (billettID, stykke))
        pris = cursor.fetchall()
        total_sum += pris[0][0]
    con.close()
    return total_sum
        
        


def sjekk_om_kundeprofil_eksisterer(mobilnr):
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()

    kundeprofiler = cursor.execute("SELECT mobilnummer FROM kundeprofil").fetchall()
    con.close()

    for kundeprofil in kundeprofiler:
        if kundeprofil[0] == mobilnr:
            return True

    return False


def lag_kundeprofil(mobilnr, navn, adresse):
   insert_into_table("kundeprofil", [mobilnr, navn, adresse])
   
def hent_billett_typer(stykkenavn):
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    billettpriser = cursor.execute('''SELECT gruppe, pris FROM billettgruppe WHERE stykkenavn = ?''', (stykkenavn, )).fetchall()
    con.close()
    create_table(billettpriser, ["Gruppe", "Pris (kr)"])
    
    