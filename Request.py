# 22.04.2022
# Burak GÜN 
# burak.gun@hotmail.com

import requests

x = requests.get('https://simple-books-api.glitch.me')

print(x.text)