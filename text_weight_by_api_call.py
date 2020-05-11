
import requests


payload = {'text1': 'Ferocious big beasts including lions, tigers and bears', 'text2': 'Cats, playful, baby, cute', 'token': '524277f0cefd4c0cb8bcee02d76a9fd9','lang':'en','bow':'always'}
r = requests.post("https://api.dandelion.eu/datatxt/sim/v1/", params=payload)
print (r.content)

