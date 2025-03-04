lista1 = [10, 12, 41, 68, 95, 21]


def insertion_sort(lista):
    for i in range(len(lista)):
        aux = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > aux:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = aux


insertion_sort(lista1)

