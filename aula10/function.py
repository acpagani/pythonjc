import matplotlib.pyplot as plt

xl = []
c = 0
while c <= 3.5:
    xl.append(c)
    c += 0.01

y = []

xll = []
while c <= 6:
    xll.append(c)
    c += 0.01

yl = []
for x in xl:
    if x < 2:
        y.append(x)
    elif 2 <= x <= 3.5:
        y.append(2)

for x1 in xll:
    if 3.5 < x1 < 5:
        yl.append(3)
    else:
        yl.append((x1 ** 2) - (10 * x1) + 28)


plt.plot(xl, y, xll, yl)
plt.axhline(y=0, color='r', linestyle='-', linewidth=1)
plt.axvline(x=0, color='b', linestyle='--', linewidth=1)
plt.title("Gráfico da função")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
