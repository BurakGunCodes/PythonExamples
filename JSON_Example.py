# 17.04.2022
# Burak GÜN 
# burak.gun@hotmail.com

"""
import json

# Creating a dictionary
Dictionary ={1:'Welcome', 2:'to',3:'Geeks', 4:'for',5:'Geeks'}

# Converts input dictionary into
# string and stores it in json_string
json_string = json.dumps(Dictionary)
print('Equivalent json string of input dictionary:',json_string)
print("	 ")

# Checking type of object
# returned by json.dumps
print(type(json_string))

"""
"""
import json

f = open('screen.json',)

data = json.load(f)

data_x = data['widget']

for i in data_x['text']:
    print(i)

"""

import json
from prettytable import PrettyTable

#table = PrettyTable(['Title', 'Price'])
table = PrettyTable()
table.field_names = ['Title', 'Price']

file = open('Books.json',)

# load  -- json file
# loads -- string

data = json.load(file)

data2 = data['books']
for i in data2:
    table.add_row([ i['title'], i['price'] ]  )

print(table)
    #print(i['title'], i['price'])