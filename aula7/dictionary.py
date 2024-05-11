dictio = {
    "nome": "Edgar",
    "idade": 18,
    "Cargo": None
}

for data in dictio.values():
    if data is None:
        print("Desempregado")
        continue
    print(data)
