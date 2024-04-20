import requests

cep = input("CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"
url2 = f"https://www.tutorialspoint.com/python-program-to-search-an-element-in-a-dictionary"

payload = {'origem': 37044150, "destino": 5651231 }
headers = {'usernaome': key:}

lugar = requests.post(url=url2, data=payload, headers=header)

print(lugar.text)


