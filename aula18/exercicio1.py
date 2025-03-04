palavras = ["casa", "carro", "casa", "bicicleta", "carro", "carro", "bicicleta"]

count = {}

for palavra in palavras:
    if palavra not in count:
        count[palavra] = 1
    else:
        count[palavra] += 1

print(count)
