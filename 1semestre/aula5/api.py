import requests

#cep1 = input("CEP 1: ")

#url = f"https://viacep.com.br/ws/{cep1}/json/"
advice = f"https://api.adviceslip.com/advice"

payload = {'origem': 37044150, "destino": 5651231}

lugar = requests.post(url=url2, data=payload)

print(lugar.text)
