import sqlite3

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