import requests


url = 'https://pokeapi.co'

response = requests.get(url).json()

print(response)
