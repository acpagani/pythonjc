input = int(input("Input: "))
contador = 0
c = 0

while contador <= input:
    while c < contador:
        print(c + 1, end=' ')
        c += 1
    print()
    contador += 1
    c = 0
