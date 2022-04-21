# 17.04.2022
# Burak GÜN 
# burak.gun@hotmail.com

# https://www.tutorialguruji.com/python/python-prettytable-add-ljust/

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
# The json.load() is used to read the JSON document from file.
# The json.loads() is used to convert the JSON String document into the Python dictionary.

import json
from prettytable import PrettyTable

#table = PrettyTable(['Title', 'Price'])
table = PrettyTable()
table.field_names = ['Title', 'Price', 'Empty']

# with open ile açıldığı zaman dosyayı kapatmamıza gerek yok
# Sistem otomatik olarak kapatır.
with open('Books.json') as file:
    data1 = json.load(file)

print((data1['books']))
print(type(data1['books']))

# print((data1['books'][0]['language'][0:3])) 
#for x in range( len(data1['books']) ):
print((data1['books'][2]['title'])) 



# print(data1["books"][0:2])
# print(type(data1["books"][1]))
# print(type(data2))


# widget_file = open('screen.json')
# data_widget = json.load(widget_file,)

# print(type(data_widget['widget']), ' ' , type(data['books']))

# # load  -- json file
# # loads -- string



# data2 = data['books']
# for i in data2:
#     table.add_row( [ i['title'], i['price'] ,type(data) ]  )

# print(table)
#     #print(i['title'], i['price'])


