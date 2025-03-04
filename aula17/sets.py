lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

s1 = set(lista1)
s2 = set(lista2)

comum = s1 & s2
sub = s1 - s2
sub2 = s2 - s1
nao_rep = s1 ^ s2

print(comum)
print(sub)
print(sub2)
print(nao_rep)
