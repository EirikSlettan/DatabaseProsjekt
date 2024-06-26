from datetime import*
from time import *
from insert_into import *

def opprett_billetter(billettID, kjopsdato, kjopstid, mobilnummer, billettgruppe, sete_nr, rad_nr,omraade,salnavn, ignore, forestillingstid,stykkenavn, forestillingsdatoer):
    for i in range(1, len(forestillingsdatoer)):
        insert_into_table("billett", [billettID, None, None, None,  None,  sete_nr, rad_nr, omraade, salnavn, forestillingsdatoer[i], forestillingstid, stykkenavn])
        billettID +=1
    if mobilnummer:
        insert_into_table("billett", [billettID, kjopsdato, kjopstid, mobilnummer, billettgruppe, sete_nr, rad_nr, omraade,salnavn,forestillingsdatoer[0], forestillingstid,stykkenavn] )
        billettID += 1
    else:
        insert_into_table("billett", [billettID, None, None, None,  None,  sete_nr, rad_nr, omraade, salnavn, forestillingsdatoer[0], forestillingstid, stykkenavn])
        billettID += 1
        
    return billettID



def sette_inn_stoler_gamle_scene(file):
    galleri_rad_nr = 4
    balkong_rad_nr = 5
    parkett_rad_nr = 11
    sete_nr = 0
    salnavn = "Gamle scene"
    stykkenavn = "Storst av alt er kjaerligheten"
    kjopsdato = "2024-03-12"
    kjopstid = "00:00:00"
    forestillingsdato = 0
    forestillingstid = "18:30:00"
    billettgruppe = "Ordinaer"
    billettID = 1
    billett_kjop = [kjopsdato, kjopstid, 99999999]
    insert_into_table("billettkjop", billett_kjop) #Legger inn billettkjøpentiteter i entitetsklassen billettkjop (Samme for resten som bruker insert_into_table).
    forestillingsdatoer = ["2024-02-03", "2024-02-06", "2024-02-07", "2024-02-12", "2024-02-13", "2024-02-14"]
    
    f = open(file, "r")
    omraade = ""
    for line in f: #Leser gjennom hver linje i fila
        line = line.strip() #Fjerner whitespace og linjeskift
        if not forestillingsdato:
            forestillingsdato = line[5:] #Har satt forestillingsdato = 0. Dvs at forestilling er "not" på første linje. Da setter vi dato til å være datoen, altså fra og med tegn nr. 5 i linje 1.
        
        elif line.isalpha(): #Hvis linjen kun består av bokstaver (som den gjør når man definerer område), setter vi område lik denne linjen.
            omraade = line

        else:
            line = line[::-1] #Når linjen består av tall begynner vi å lese fra høyre siden plassene nummereres ovenfra til høyre og nedover mot venstre. 
            sete_nr = len(line) + 1 #Setter sete_nr til sete på rad med høyest setenr.

            if omraade == "Galleri":
                galleri_rad_nr -= 1
            
            elif omraade == "Balkong":
                balkong_rad_nr -= 1
            
            elif omraade == "Parkett":
                parkett_rad_nr -= 1

            for letter in line: 
                
                if letter == "x": #Dette er mellomrom mellom setene, og fjerner derfor et sete (oppretter ingen)
                    
                    sete_nr -= 1
                    
                elif letter == "0": #Ingen billetter er kjøpt her. Derfor opprettes kun seteentiteter, og ikke billettentiteter.

                    if omraade == "Galleri":
                        sete_nr -=1
                        billett= [billettID, None, None, None,  None,  sete_nr, galleri_rad_nr, omraade, salnavn, forestillingsdato, forestillingstid, stykkenavn] #BILLETT!!!
                        billettID = opprett_billetter(*billett, forestillingsdatoer)
                        sete_ledig_galleri = [sete_nr, galleri_rad_nr, omraade, salnavn] 
                        insert_into_table("sete", sete_ledig_galleri)
                    
                    elif omraade == "Balkong":
                        sete_nr -=1
                        billett= [billettID, None, None, None, None, sete_nr, balkong_rad_nr, omraade, salnavn, forestillingsdato, forestillingstid, stykkenavn] #BILLETT!!!
                        billettID = opprett_billetter(*billett, forestillingsdatoer)
                        sete_ledig_balkong = [sete_nr, balkong_rad_nr, omraade, salnavn] 
                        insert_into_table("sete", sete_ledig_balkong)
                    
                    elif omraade == "Parkett":
                        sete_nr -=1
                        billett = [billettID, None, None, None, None, sete_nr, parkett_rad_nr, omraade, salnavn, forestillingsdato, forestillingstid, stykkenavn] #BILLETT!!!
                        billettID = opprett_billetter(*billett, forestillingsdatoer)
                        sete_ledig_parkett = [sete_nr, parkett_rad_nr, omraade, salnavn] 
                        insert_into_table("sete", sete_ledig_parkett)

                elif letter == "1": #Her er et sete kjøpt, og derfor vil en billettentitet også lages.
                    sete_nr -= 1
                    if omraade == "Galleri":
                        sete_opptatt_galleri = [sete_nr, galleri_rad_nr, omraade, salnavn] 
                        insert_into_table("sete", sete_opptatt_galleri)
                        billett = [billettID, kjopsdato, kjopstid, 99999999, billettgruppe,sete_nr, galleri_rad_nr,omraade,salnavn,forestillingsdato,forestillingstid,stykkenavn]
                        billettID = opprett_billetter(*billett, forestillingsdatoer)
                    
                    elif omraade == "Balkong":
                        sete_opptatt_balkong = [sete_nr,balkong_rad_nr,omraade,salnavn] 
                        insert_into_table("sete", sete_opptatt_balkong)
                        
                        billett = [billettID,kjopsdato,kjopstid,99999999,billettgruppe,sete_nr,balkong_rad_nr,omraade,salnavn,forestillingsdato,forestillingstid,stykkenavn] 
                        billettID = opprett_billetter(*billett, forestillingsdatoer)
                    
                    elif omraade == "Parkett":
                        sete_opptatt_parkett = [sete_nr, parkett_rad_nr, omraade, salnavn]
                        insert_into_table("sete", sete_opptatt_parkett)
                        billett = [billettID, kjopsdato, kjopstid, 99999999, billettgruppe, sete_nr, parkett_rad_nr, omraade, salnavn, forestillingsdato, forestillingstid, stykkenavn]
                        billettID = opprett_billetter(*billett, forestillingsdatoer)

                        
                        

def sette_inn_stoler_hovedscenen(file):
    rad_nr = 18
    sete_nr = 524 + 1
    salnavn = "Hovedscenen"
    stykkenavn = "Kongsemnene"
    kjopsdato = "2024-03-12"
    kjopstid = "00:00:01"
    forestillingsdato = 0
    forestillingstid = "19:00:00"
    billettgruppe = "Ordinaer"
    billettID = 1993
    billett_kjop = [kjopsdato, kjopstid, 99999999]
    insert_into_table("billettkjop", billett_kjop) #Legger inn billettkjøpentiteter i entitetsklassen billettkjop (Samme for resten som bruker insert_into_table).
    forestillingsdatoer = ["2024-02-03", "2024-02-01", "2024-02-02", "2024-02-05", "2024-02-06"]

    f = open(file, "r")
    omraade = ""
    for line in f: #Leser gjennom hver linje i fila
        line = line.strip() #Fjerner whitespace og linjeskift
        if not forestillingsdato:
            forestillingsdato = line[5:] #Har satt forestillingsdato = 0. Dvs at forestilling er "not" på første linje. Da setter vi dato til å være datoen, altså fra og med tegn nr. 5 i linje 1.
        
        elif line.isalpha(): 
            omraade = line #Hvis linjen kun består av bokstaver (som den gjør når man definerer område), setter vi område lik denne linjen.
        else:
            line = line[::-1] #Når linjen består av tall begynner vi å lese fra høyre siden plassene nummereres ovenfra til høyre og nedover mot venstre. 
            for letter in line: 
                if letter == "x": #Dette er mellomrom mellom setene, og fjerner derfor et sete (oppretter ingen)
                    sete_nr -= 1
                    
                elif letter == "0": #Ingen billetter er kjøpt her. Derfor opprettes kun seteentiteter, og ikke billettentiteter.
                    sete_nr -=1
                    if omraade == "Galleri":
                        sete_ledig_galleri = [sete_nr, 0, omraade, salnavn] 
                        insert_into_table("sete", sete_ledig_galleri)
                        billett_galleri = [billettID, None, None, None, None, sete_nr, None, omraade, salnavn, forestillingsdato, forestillingstid, stykkenavn] #BILLETT!!!
                        billettID = opprett_billetter(*billett_galleri, forestillingsdatoer)

                    else:
                        billett_parkett = [billettID, None, None, None, None, sete_nr, rad_nr, omraade, salnavn, forestillingsdato, forestillingstid, stykkenavn] #BILLETT!!!
                        billettID = opprett_billetter(*billett_parkett, forestillingsdatoer)
                        sete_ledig_parkett = [sete_nr, rad_nr, omraade, salnavn] 
                        insert_into_table("sete", sete_ledig_parkett)

                   
                elif letter == "1": #Her er et sete kjøpt, og derfor vil en billettentitet også lages.
                    sete_nr -= 1
                    if omraade == "Galleri":
                        sete_opptatt_galleri = [sete_nr, 0, omraade, salnavn] 
                        insert_into_table("sete", sete_opptatt_galleri)
                        billett_galleri = [billettID, kjopsdato, kjopstid, 99999999, billettgruppe, sete_nr, 0, omraade, salnavn, forestillingsdato, forestillingstid, stykkenavn] #BILLETT!!!
                        billettID = opprett_billetter(*billett_galleri, forestillingsdatoer)
                        
                    else:
                        sete_opptatt_parkett = [sete_nr, rad_nr, omraade, salnavn] 
                        insert_into_table("sete", sete_opptatt_parkett)
                        
                        
                        billett_parkett = [billettID, kjopsdato, kjopstid, 99999999, billettgruppe, sete_nr, rad_nr, omraade, salnavn, forestillingsdato, forestillingstid, stykkenavn] #BILLETT!!!
                        billettID = opprett_billetter(*billett_parkett, forestillingsdatoer)

                        billettID += 1
            if omraade != "Galleri":
                rad_nr -= 1





sette_inn_stoler_gamle_scene("tekstfiler/gamle-scene.txt")
            
sette_inn_stoler_hovedscenen("tekstfiler/hovedscenen.txt")





        

