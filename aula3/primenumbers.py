from math import sqrt
from time import sleep

n = 1

isDev = False

while True:
    for c in range(int(sqrt(n)), 1, -1):
        if n % c == 0:
            isDev = True
            break
    if not isDev:
        print(n)
        sleep(1)
    isDev = False
    n += 1
