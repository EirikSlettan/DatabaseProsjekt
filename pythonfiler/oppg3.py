import sqlite3
from utils import *

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
    create_table(result, ["Rad", "Omraade", "Navn", "Ledige"]) #Printer resultatet

def kjop_billetter(rad, antall, omraade, salnavn, mobilnummer):
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    kjopsdato = "0000-00-00"
    kjopstid = "00:00:00"
    
    seter = cursor.execute('''SELECT billettID from billett 
                            WHERE mobilnummer is NULL AND rad = ? AND omraade = ? AND salnavn = ? LIMIT ? ;''', (rad, omraade, salnavn, antall))
    
    #insert_into_table("billettkjop", [kjopsdato, kjopstid, mobilnummer])
    seter = seter.fetchall()
    for sete in seter:
        print(sete[0])
        cursor.execute('''UPDATE billett  SET 
                       kjopsdato = ?, 
                       kjopstid = ?, 
                       mobilnummer = ?, 
                       billettgruppe = ? WHERE billettID = ?
                       ''', (kjopsdato, kjopstid, mobilnummer, 'Honnor',sete[0]))
    con.commit()
    con.close()


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
    con = sqlite3.connect("teater_database.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO kundeprofil VALUES (?, ?, ?)", (mobilnr, navn, adresse))
    con.close()