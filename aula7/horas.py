from time import sleep

for c in range(24):
    for i in range(60):
        for j in range(60):
            print(f"{c:02d}:{i:02d}:{j:02d}")
            sleep(1)
