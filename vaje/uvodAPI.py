# uvod v API-je
import requests #pip install requests
base_url = "https://api.chucknorris.io/jokes/random"

call = requests.get(base_url)
#print(call.text) preveri vsebino klica
callJSON = call.json()
print(callJSON["value"])