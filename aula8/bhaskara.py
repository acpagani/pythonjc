import matplotlib.pyplot as plt
import numpy as np


def bkr(a, b, c):
    delta = (b ** 2) - (4 * a * c)

    if delta == 0:
        x = (-b) / (2 * a)
    else:
        x = list()
        x.append(((-b) + (delta ** (1/2))) / (2 * a))
        x.append(((-b) - (delta ** (1/2))) / (2 * a))

    return x


def funcao(x, a, b, c):
    y = a * x ** 2 + b * x + c

    return y


def main():
    a = int(input("Determine um valor para a: "))
    b = int(input("Determine um valor para b: "))
    c = int(input("Determine um valor para c: "))

    print(bkr(a, b, c))

    x = np.arange(-10, 10, 0.1)

    y = funcao(x, a, b, c)

    plt.plot(x, y)
    plt.axhline(y=0, color='r', linestyle='-', linewidth=2)
    plt.axvline(x=0, color='b', linestyle='--', linewidth=1)

    plt.title("Gráfico da função")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.show()


main()
