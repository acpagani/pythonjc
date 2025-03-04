pessoas = (("João", 15), ("Maria", 21), ("Pedro", 20), ("Ana", 18))

maiores = tuple()

for pessoa in pessoas:
    if pessoa[1] >= 18:
        maiores += (pessoa,)

print(maiores)
