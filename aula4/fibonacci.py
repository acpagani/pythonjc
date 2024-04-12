from time import sleep

lista = list()
index = 0
n = 0

while True:
    lista.append(n)
    index += 1
    if index == 1:
        lista.append(1)
    n += lista[index - 1]
    print(n)
    sleep(1)
    if index > 4:
        lista.pop(0)
        index -= 1
