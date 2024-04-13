

def piram(n):
    if n > 0:
        piram(n - 1)
    print("#" * n)


piram(int(input("Numero de layers: ")))
