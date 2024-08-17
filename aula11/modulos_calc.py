def somar(*args):
    s = 0
    for c in args:
        s += c
    return s


def subtrair(*args):
    p = args[0]
    for c in args[1:]:
        p -= c
    return p


def multiplicar(*args):
    m = 1
    for c in args:
        m *= c
    return m


def dividir(*args):
    p = args[0]
    for c in args[1:]:
        if c == 0:
            continue
        p /= c
    return p
