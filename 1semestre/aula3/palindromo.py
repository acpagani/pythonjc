s = input("Digite uma palavra ou frase: ")

texto = ''
for i in s.split():
    texto += i

texto = texto.lower()

if texto == texto[::-1]:
    print("Essa frase / palavra é um palíndromo!")
