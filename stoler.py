from datetime import*
from time import*
from insert_into import*



def sette_inn_stoler_gamle_scene(file):
    rad_nr = 0
    sete_nr = 0
    salnavn = "Gamle scene"
    stykkenavn = "Størst av alt er kjærligheten"
    forfatter = "Jonas Corell Petersen"
    sesong = "vinter/vaar"
    kjopsdato = "2024-03-12"
    kjopstid = "00:00:00"
    forestillingsdato = 0
    forestillingstid = "18:30:00"
    billettgruppe = "Ordinaer"
    billettID = 1
    f = open(file, "r")
    omraade = ""
    for line in f:
        line = line.strip()
        if not forestillingsdato:
            forestillingsdato = line[5:]
        
        elif line.isalpha(): 
            omraade = line
        else:
            line = line[::-1]
            
            for letter in line: 
                if letter == "x":
                    
                    sete_nr -= 1
                    
                elif letter == "0":
                    sete_nr -=1

                    if omraade == "Galleri":
                        sete_ledig_galleri = f"({sete_nr}, {None}, {omraade}, {salnavn})" #SETE!!!
                        sete_ledig_galleri = sete_ledig_galleri.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("sete", sete_ledig_galleri)

                    elif omraade == 

                    else:
                        sete_ledig_parkett = f"({sete_nr}, {rad_nr}, {omraade}, {salnavn})" #SETE!!!
                        sete_ledig_parkett = sete_ledig_parkett.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("sete", sete_ledig_parkett)

                    #Insert()
                elif letter == "1":
                   

                    sete_nr -= 1
                    
                    #Insert()
                    if omraade == "Galleri":
                        

                        sete_opptatt_galleri = f"({sete_nr}, {None}, {omraade}, {salnavn})" #SETE!!!
                        sete_opptatt_galleri = sete_opptatt_galleri.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("sete", sete_opptatt_galleri)
                        

                        billett_galleri = f"({billettID}, {kjopsdato}, {kjopstid}, {99999999}, {billettgruppe}, {sete_nr}, {None}, {omraade}, {salnavn}, {forestillingsdato}, {forestillingstid}, {stykkenavn})" #BILLETT!!!
                        billett_galleri = billett_galleri.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("billett", billett_galleri)

                        billettID += 1
                        
                        

                    else:
                        #print(f"({rad_nr}, {sete_nr}, {omraade}, {salnavn}, solgt)") SETE!!!

                        sete_opptatt_parkett = f"({sete_nr}, {rad_nr}, {omraade}, {salnavn})" #SETE!!!
                        sete_opptatt_parkett = sete_opptatt_parkett.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("sete", sete_opptatt_parkett)
                        
                        
                        billett_parkett = f"({billettID}, {kjopsdato}, {kjopstid}, {99999999}, {billettgruppe}, {sete_nr}, {rad_nr}, {omraade}, {salnavn}, {forestillingsdato}, {forestillingstid}, {stykkenavn})" #BILLETT!!!
                        billett_parkett = billett_parkett.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("billett", billett_parkett)

                        billettID += 1
                
def sette_inn_stoler_hovedscenen(file):
    rad_nr = 18
    sete_nr = 524 + 1
    salnavn = "hovedscenen"
    stykkenavn = "Kongsemne"
    forfatter = "Henrik Ibsen"
    sesong = "vinter/vaar"
    kjopsdato = "2024-03-12"
    kjopstid = "00:00:00"
    forestillingsdato = 0
    forestillingstid = "19:00:00"
    billettgruppe = "Ordinaer"
    billettID = 1
    f = open(file, "r")
    omraade = ""
    for line in f:
        line = line.strip()
        if not forestillingsdato:
            forestillingsdato = line[5:]
        
        elif line.isalpha(): 
            omraade = line
        else:
            line = line[::-1]
            #print(line)
            for letter in line: 
                if letter == "x":
                    
                    sete_nr -= 1
                    
                elif letter == "0":
                    sete_nr -=1

                    if omraade == "Galleri":
                        sete_ledig_galleri = f"({sete_nr}, {None}, {omraade}, {salnavn})" #SETE!!!
                        sete_ledig_galleri = sete_ledig_galleri.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("sete", sete_ledig_galleri)

                    else:
                        sete_ledig_parkett = f"({sete_nr}, {rad_nr}, {omraade}, {salnavn})" #SETE!!!
                        sete_ledig_parkett = sete_ledig_parkett.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("sete", sete_ledig_parkett)

                    #Insert()
                elif letter == "1":
                   

                    sete_nr -= 1
                    
                    #Insert()
                    if omraade == "Galleri":
                        

                        sete_opptatt_galleri = f"({sete_nr}, {None}, {omraade}, {salnavn})" #SETE!!!
                        sete_opptatt_galleri = sete_opptatt_galleri.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("sete", sete_opptatt_galleri)
                        

                        billett_galleri = f"({billettID}, {kjopsdato}, {kjopstid}, {99999999}, {billettgruppe}, {sete_nr}, {None}, {omraade}, {salnavn}, {forestillingsdato}, {forestillingstid}, {stykkenavn})" #BILLETT!!!
                        billett_galleri = billett_galleri.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("billett", billett_galleri)

                        billettID += 1
                        
                        

                    else:
                        #print(f"({rad_nr}, {sete_nr}, {omraade}, {salnavn}, solgt)") SETE!!!

                        sete_opptatt_parkett = f"({sete_nr}, {rad_nr}, {omraade}, {salnavn})" #SETE!!!
                        sete_opptatt_parkett = sete_opptatt_parkett.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("sete", sete_opptatt_parkett)
                        
                        
                        billett_parkett = f"({billettID}, {kjopsdato}, {kjopstid}, {99999999}, {billettgruppe}, {sete_nr}, {rad_nr}, {omraade}, {salnavn}, {forestillingsdato}, {forestillingstid}, {stykkenavn})" #BILLETT!!!
                        billett_parkett = billett_parkett.replace("(", "").replace(")", "").strip().split(",")
                        insert_into_table("billett", billett_parkett)

                        billettID += 1
                        
                        


                        

            if omraade != "Galleri":
                rad_nr -= 1


    forestilling = (f"({forestillingsdato}, {forestillingstid}, {stykkenavn})") #FORESTILLING!!
    forestilling = forestilling.replace("(", "").replace(")", "").strip().split(",")
    insert_into_table("forestilling", forestilling)


    teaterstykke = (f"({stykkenavn},{forfatter},{sesong})") #teaterstykke
    teaterstykke = teaterstykke.replace("(", "").replace(")", "").strip().split(",")
    insert_into_table("teaterstykke", teaterstykke) #det er kun ett teaterstykke her




sette_inn_stoler_hovedscenen("gamle-scene.txt")
            
sette_inn_stoler_hovedscenen("hovedscenen.txt")





        

