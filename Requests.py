import requests
import json

list = []

r = requests.get('https://steamspy.com/api.php?request=top100in2weeks')
print(r.status_code)
jsondata = json.loads(r.text)

for k, v in jsondata.items():
  print(k, v['name'])
  list.append(v['name'])