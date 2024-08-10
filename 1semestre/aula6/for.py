from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)

print("\033[1;30;41mPOW\033[m", end='')
for c in range(20):
    print("\033[1;41m  \033[m ", end='')
    sleep(0.5)
print("\033[1;31;40mCABOOM\033[m", end='')
