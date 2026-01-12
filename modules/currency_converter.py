import requests
import json

api_key = "YOUR_API_KEY"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz türü (ör: USD): ").upper()
alinan_doviz = input("Alınan döviz türü (ör: TRY): ").upper()
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

response = requests.get(api_url + bozulan_doviz)
data = json.loads(response.text)

oran = data["conversion_rates"][alinan_doviz]

print(f"1 {bozulan_doviz} = {oran} {alinan_doviz}")
print(f"{miktar} {bozulan_doviz} = {miktar * oran} {alinan_doviz}")
