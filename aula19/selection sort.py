valores = [50, 40, 36, 9, 45, 67, 89]


def menor_index(lista, init):
    min_value = init

    for i in range(len(lista)):
        if lista[i] < lista[min_value]:
            min_value = i

    return min_value


def selection_sort(lista):
    min_value = 0
    for i in range(len(lista)):
        for j in range(len(lista) - i):
            min_value = menor_index(lista, i)

        tmp = lista[i]
        lista[i] = lista[min_value]
        lista[min_value] = tmp
    return lista


print(selection_sort(valores))