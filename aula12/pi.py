def pi(loop):
    n = 0
    for lp in range(loop):
        n += ((-1) ** lp) * ((2 * lp + 1) ** (-1))
    return n * 4


print(pi(376849))
