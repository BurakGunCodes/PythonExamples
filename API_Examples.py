

import requests
import webbrowser

api_url = "https://api.github.com/users/{}".format('BurakGunCodes')

api_response = requests.get(api_url)

json_response = api_response.json()
web_page = json_response['blog']

for values in json_response:
    print( values,":", json_response[values]  )



webbrowser.open(web_page, new=0, autoraise=True)  # Go to example.com/blog page