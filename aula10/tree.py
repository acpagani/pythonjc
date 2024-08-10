n = int(input("Número de linhas: "))
ind = (2 * n) - 1
c = 1

while c <= ind:
    print(f"{('*' * c):^{ind}}")
    c += 2
