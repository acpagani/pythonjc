animais = list()

a = input("Qual o seu animal de estimação? ")

animais.append(a)
animais.append("gato")

lista2 = ['felinos', 'aves']

# Função que junta listas, faz com que os elementos da lista2 sejam appendados à lista principal
animais.extend(lista2)

print(animais)
