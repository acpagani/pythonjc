texto = """O SAPO NAO LAVA O PE
NAO LAVA PORQUE NAO QUER
ELE MORA LA NA LAGOA
NAO LAVA O PE PORQUE NAO QUER
MAS QUE CHULE"""

lista = list(texto)
let = input("Letra: ")
texto_final = ''

for c in range(len(lista)):
    if lista[c] in "AEIOU":
        lista[c] = let.upper()
        texto_final += lista[c]
    else:
        texto_final += lista[c]

print(''.join(lista))
