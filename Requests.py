import requests

def response():
  r = requests.get("https://steamspy.com/api.php?request=top100in2weeks")
  r2 = requests.get("https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=730&count=3&maxlength=300&format=json")
  print(r.status_code)
  print(r.json())
  print(r2.status_code)