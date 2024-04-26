import requests

#cep1 = input("CEP 1: ")

#url = f"https://viacep.com.br/ws/{cep1}/json/"
advice = f"https://api.adviceslip.com/advice"

url_apis = f"https://publicapis.dev/category/cryptocurrency"

lugar = requests.get(url=advice)

print(lugar.json()['slip']['advice'])


