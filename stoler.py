def sette_inn_stoler_gamle_scene(file):
    salnavn = "hovedscenen"
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
                    print ("yoloman")
                    sete_nr -= 1
                    
                elif letter == "0":
                    sete_nr -=1

                    if omraade == "Galleri":
                        print(f"({None}, {sete_nr}, {omraade}, {salnavn}, ikke solgt)")

                    else:
                        print(f"({rad_nr}, {sete_nr}, {omraade}, {salnavn}, ikke solgt)")

                    #Insert()
                elif letter == "1":

                    sete_nr -= 1
                    
                    #Insert()
                    if omraade == "Galleri":
                        print(f"({None}, {sete_nr}, {omraade}, {salnavn}, solgt)")

                    else:
                        print(f"({rad_nr}, {sete_nr}, {omraade}, {salnavn}, solgt)")

            if omraade != "Galleri":
                rad_nr -= 1
            
sette_inn_stoler_hovedscenen("hovedscenen.txt")





        

