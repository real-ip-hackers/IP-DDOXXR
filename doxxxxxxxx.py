import requests
import json

ipaddr = input("Give ip address to DOXXXXXXXX and REVEAL!: ")

request = requests.get("http://ip-api.com/json/"+ipaddr).text
info = json.loads(request)


if info["status"] != "success":
    print("F41L!!!!!!!!")
else:
    print("SUCC3SFULLY DOXXXXXXXX3D!!!!!!!!")
    print(f'{info["query"]}:\n Country: {info["country"]} ({info["countryCode"]})\n Region: {info["regionName"]} ({info["region"]})\n City: {info["city"]}\n Coords: {info["lat"]} {info["lon"]}')
