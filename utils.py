def find_longest_entry(data, column_names): #Finds longest entry in each column
    longest = [0]*len(column_names)
    for i in range(len(data)):
        row = data[i]
        print(i)
        print(longest)
        for j in range(len(row)):
             print(j)
             print(longest)
             if len(str(row[j])) > longest[j]:
                longest[j] = len(str(row[j]))
    for i in range(len(column_names)): 
        if len(column_names[i]) > longest[i]:
            longest[i]= len(column_names[i])
    return longest

def create_table(data, column_names):
    dig = find_longest_entry(data, column_names)
    entry_lengths = [x+1 for x in dig]
    table_length = sum(entry_lengths) + len(column_names)+1
    border = f"{'-' * (table_length-len(column_names))}"
    print(border)
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

data = [('18:30:00', '2024-02-03', 'Storst av alt er kjaerligheten', 27), ('19:00:00', '2024-02-03', 'Kongsemnene', 0)]
column_names = ["Tid", "Dato", "Navn", "Solgt"]

print(find_longest_entry(data, column_names))

create_table(data, column_names )

