def matriz_esparsa(m):
    count_zero = 0
    count = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            count += 1
            if m[i][j] == 0:
                count_zero += 1

    if count_zero >= (count / 2):
        return True
    else:
        return False


m = [
    [1, 3, 3],
    [0, 0, 0],
    [1, 0, 3]
]

if matriz_esparsa(m):
    print("AOouawjd")
