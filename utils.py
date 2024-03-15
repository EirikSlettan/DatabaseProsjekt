from re import *
import sqlite3

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
    for length in entry_lengths: #Setter inn + ved alle kryss
        border = border[:index] + "+" + border[index:] 
        index += length+1
    border = border[:index] + "+" + border[index+1:]
    
    print(border)  
    print(columns.format(*column_names))
    print(border)
    for row in data: 
        row = [str(c) for c in row] #Konverterer all NULL verdier til string
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
    if match(gyldig_input, dato): #Returnerer true hvis input matcher regex
        return True
    False 
def convert_values(values): #Konverterer en liste til streng og tupler
    string = ""
    tuple = ()
    for value in values:
        string += f"?, "
        tuple += (value,)
    return string[0: -2], tuple #Fjerner mellomrom og komma på slutten
        
def insert_into_table(table, values): #Tar inn string for tabellnavn, og liste for values
    parameters, tuple = convert_values(values)
    con = sqlite3.connect("teater_database.db") #Endre dette
    cursor = con.cursor()
    
    try:
        cursor.execute(f"INSERT INTO {table} VALUES ({parameters})", (tuple)) 
        con.commit()
        con.close()
    except Exception as e:
        print("Noe gikk galt: ", e, table, values)