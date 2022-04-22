


import json
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['name', 'type']

with open('books2.json') as file:
    books = json.load(file)

for each in books:
    table.add_row([ each['name'],each['type'] ])

print(table)
 

