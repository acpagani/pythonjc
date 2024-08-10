import matplotlib.pyplot as plt
import numpy as np

xl = np.arange(0, 6, 0.1)
y = []

for x in xl:
    if x < 2:
        y.append(x)
    elif 2 <= x <= 3.5:
        y.append(2)
    elif 3.5 < x < 5:
        y.append(3)
    else:
        y.append((x ** 2) - (10 * x) + 28)

plt.plot(xl, y)
plt.axhline(y=0, color='r', linestyle='-', linewidth=1)
plt.axvline(x=0, color='b', linestyle='--', linewidth=1)
plt.title("Gráfico da função")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
