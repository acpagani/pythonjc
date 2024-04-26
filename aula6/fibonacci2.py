from time import sleep

n = 0
n1 = 1
n2 = 0
count = 0

flag = int(input("Número dos n primeiros números da sequência: "))

while True:
    if count == 0:
        n2 = n + n1
    n = n1
    n1 = n2
    n2 = n + n1
    count += 1
    print(n2)
    sleep(0.5)

    if count >= flag:
        break
