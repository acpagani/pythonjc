def soma(*args):
    s = 0
    for c in args:
        s += c

    return s


rep = int(input("Número de parametros: "))
numeros = []

for a in range(rep):
    n = int(input("Número: "))
    numeros.append(n)

print(soma(*numeros))
