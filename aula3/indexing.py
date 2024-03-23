name = input("Escreva seu nome: ")

print(f"Seu nome tem {len(name)} letras")
print(f"A primeira letra do seu nome é {name[0].upper()}")
print(f"A última letra do seu nome é {name[-1].upper()}")

print(name[::-1])
