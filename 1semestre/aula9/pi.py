def pi(loop):
    pi_number = 0
    for n in range(loop):
        pi_number += (((-1) ** n) * (2 * 3 ** (1 / 2))) / ((3 ** n) * (2 * n + 1))
    return pi_number


def sin(x, loop):
    num_sin = 0
    for n in range(loop):
        num_sin += (((-1) ** n) / fact(2 * n + 1)) * (x ** (2 * n + 1))
    return num_sin


def cos(x, loop):
    num_cos = 0
    for n in range(loop):
        num_cos += (((-1) ** n) / fact(2 * n)) * (x ** (2 * n))
    return num_cos


def tg(x, loop):
    return sin(x, loop) / cos(x, loop)


def fact(x):
    cont = 1
    num_fact = 1
    while cont <= x:
        num_fact *= cont
        cont += 1
    return num_fact


print(tg(pi(640) / 3, 640))
