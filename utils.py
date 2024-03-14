from re import *

def find_longest_entry(data, column_names): #Finner input med flest tegn i hver kolonne, returnerer en list
    longest = [0]*len(column_names)
    for i in range(len(data)):
        row = data[i]
        for j in range(len(row)):
             if len(str(row[j])) > longest[j]:
                longest[j] = len(str(row[j]))
    for i in range(len(column_names)): 
        if len(column_names[i]) > longest[i]:
            longest[i]= len(column_names[i])
    return longest

def create_table(data, column_names): #Lager en tabell lik den i sqlite3 .mode table, tar inn cursor.fetchall()
    dig = find_longest_entry(data, column_names)
    entry_lengths = [x+1 for x in dig]
    table_length = sum(entry_lengths) + len(column_names)+1
    border = f"{'-' * (table_length-len(column_names))}"
    formatter = "|"
    columns = "|"
    i = 0
    for i in range(len(column_names)):
        formatter += "{" + f":<{entry_lengths[i]}" + "}|"
        columns += "{" + f":^{entry_lengths[i]}" + "}|"
    index = 0
    for length in entry_lengths:
        border = border[:index] + "+" + border[index:]
        index += length+1
    border = border[:index] + "+" + border[index+1:]
    
    print(border)  
    print(columns.format(*column_names))
    print(border)
    for row in data: 
        print(formatter.format(*row))
    print(border)

def velkommen_melding():
    bredde = 56
    bredde2 = 14
    tegn = "-"
    print(tegn *bredde)
    print(tegn *bredde)
    print(f"{tegn*bredde2} VELKOMMEN TIL VÅRT TEATER! {tegn*bredde2}")
    print(tegn*bredde)
    print(tegn*bredde)

def validate_input(svar, melding):
    while True:
        if svar.upper() == "Y" or svar.upper() == "N":
            return svar
        print("Ugyldig svar, prøv igjen")
        svar = input(melding).upper()
        
def validate_date(dato):
    gyldig_input = r'^\d{4}-\d{2}-\d{2}$'
    if match(gyldig_input, dato):
        return True
    False 