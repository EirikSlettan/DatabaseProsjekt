import sqlite3

def convert_values(values): #Konverterer en liste til streng
    string = ""
    for value in values:
        if isinstance(value, str):
            string += f"'{value}', "
        else:
            string += f"{value}, "
    return string[0: -2] #Fjerner mellomrom og komma på slutten
        
def insert_into_table(table, values): #Tar inn string for tabellnavn, og liste for values
    con = sqlite3.connect("eksempel.db") #Endre dette
    cursor = con.cursor()
    string_values = convert_values(values)
    try:
        cursor.execute(f'''INSERT INTO {table} VALUES ({string_values})''') #Sus?
        con.commit()
        con.close()
    except Exception as e:
        print("Noe gikk galt: ", e)