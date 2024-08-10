n = int(input("Digite um número: "))

if n % 2 == 0:
    print("É par", end='')
    if n - 100 > 0:
        print(" e menor que 100")
    else:
        print(" e maior ou igual a 100")
else:
    print("É impar", end='')
    if n - 100 > 0:
        print(" e menor que 100")
    else:
        print(" e maior ou igual a 100")
