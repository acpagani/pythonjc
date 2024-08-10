a = 10
b = 20

# Método não recomendado
a, b = b, a
print (a, b)

a1 = 10
b1 = 20

tmp = a1
a1 = b1
b1 = tmp

# Método recomendado
print(a, b)
