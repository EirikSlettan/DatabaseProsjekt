from datetime import*
from time import*


def sette_inn_stoler_gamle_scene(file):
    salnavn = "gamle scene"
    
    seter_nr =1
    rad_nr = 1
    f = open(file, "r")
    dato = 0 
    for line in f:
        if not dato:
            dato = line[5:].strip()
        line = line.strip()
        if line.isalpha(): 
            omraade = line
        else:
            rad_nr += 1
            for letter in line: 
                if letter == "x":
                    continue
                elif letter == 0:
                    seter_nr +=1
                    
                    #Insert()
                    pass
                elif letter == 1: 
                    sete_nr +=1
                    rad_nr += 1
                    #Insert()
                
def sette_inn_stoler_hovedscenen(file):
    rad_nr = 18
    sete_nr = 524 + 1
    salnavn = "hovedscenen"
    stykkenavn = "Kongsemne"
    f = open(file, "r")
    dato = 0
    omraade = ""
    for line in f:
        line = line.strip()
        if not dato:
            dato = line[5:]
        
        elif line.isalpha(): 
            omraade = line
        else:
            line = line[::-1]
            #print(line)
            for letter in line: 
                if letter == "x":
                    
                    sete_nr -= 1
                    
                #elif letter == "0":
                    #sete_nr -=1

                    #if omraade == "Galleri":
                        #print(f"({None}, {sete_nr}, {omraade}, {salnavn}, ikke solgt)") #SETE!!

                    #else:
                        #print(f"({rad_nr}, {sete_nr}, {omraade}, {salnavn}, ikke solgt)") #SETE!!!

                    #Insert()
                elif letter == "1":
                   

                    sete_nr -= 1
                    
                    #Insert()
                    if omraade == "Galleri":
                        #print(f"({None}, {sete_nr}, {omraade}, {salnavn}, solgt)") #SETE!!!
                        print(f"({1},  {ctime(time())}, {99999999}, billettgruppe, {sete_nr}, {None}, {omraade}, {salnavn}, forestillingsdato, forestillingstid, {stykkenavn})") #BILLETT!!!
                        

                    else:
                        #print(f"({rad_nr}, {sete_nr}, {omraade}, {salnavn}, solgt)") SETE!!!
                        #print(f"({1}, {ctime(time())}, {99999999}, billettgruppe, {sete_nr}, {rad_nr}, {omraade}, {salnavn}, forestillingsdato, forestillingstid, {stykkenavn})") #BILLETT!!!
                        print(f"({ctime(time())}, {stykkenavn})") #FORESTILLING!!


            if omraade != "Galleri":
                rad_nr -= 1
            
sette_inn_stoler_hovedscenen("hovedscenen.txt")





        

