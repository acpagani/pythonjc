def main():
    amigo = amigos(220, 284)

    if amigo:
        print("São amigos")
    else:
        print("São inimigos")


def soma_divisores(num):
    lista = list()
    for c in range(1, num):
        if num % c == 0:
            lista.append(c)

    return sum(lista)


def amigos(num1, num2):
    if soma_divisores(num1) == num2 and soma_divisores(num2) == num1:
        return True
    else:
        return False


main()
