def soma(*args):
    s = 0
    for c in args:
        s += c
    return s


L = [1, 2]
print(soma(*L))
