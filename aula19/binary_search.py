valores = [12, 34, 56, 78, 90, 100, 150]

num = int(input("Número a ser encontrado: "))


def binary_search(lista, valor):
    init = 0
    final = len(lista) - 1
    while init <= final:
        meio = (init + final) // 2

        if num > lista[meio]:
            init = meio + 1
        elif num < lista[meio]:
            final = meio - 1
        elif num == lista[meio]:
            return meio

    return -1


print(binary_search(valores, num))
