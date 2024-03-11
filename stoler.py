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
            for letter in line: 
                if letter == "x":
                    continue
                elif letter == 0:
                    seter_nr +=1
                    rad_nr += 1
                    #Insert()
                    pass
                elif letter == 1: 
                    sete_nr +=1
                    rad_nr += 1
                    #Insert()
                
def sette_inn_stoler_hovedscenen(file):
    rad_nr = 1
    salnavn = "hovedscenen"
    f = open(file, "r")
    dato = 0
    for line in f:
        if not dato:
            dato = line[5:].strip()
        line = line.strip()
        if line.isalpha(): 
            omraade = line
            print(omraade)
        else:
            for letter in line: 
                sete_nr = 1
                if letter == "x":
                    continue
                elif letter == 0:
                    sete_nr +=1
                    rad_nr += 1
                    
                    #Insert()
                    pass
                elif letter == 1:
                    sete_nr +=1
                    rad_nr += 1
                    #Insert()
                    print(rad_nr, sete_nr, omraade, salnavn)

sette_inn_stoler_hovedscenen("hovedscenen.txt")
        







