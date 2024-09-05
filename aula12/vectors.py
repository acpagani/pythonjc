def vector(v, w):
    if len(v) != len(w):
        return "Impossível realizar a operação"

    s = 0
    for c in range(len(v)):
        s += v[c] * w[c]
        
    return s


lista1 = [1, 3, 5]
lista2 = [1, 9, 5]

print(vector(lista1, lista2))
