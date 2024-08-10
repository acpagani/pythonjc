from time import sleep


def cabecalho(string):
    print("=" * (len(string) + 10))
    print(string.center((len(string) + 10)))
    print("=" * (len(string) + 10))


cabecalho("PROGRAMA DE CÉDITOS DO BANCO ACP")

i = int(input("Informe sua idade: "))
s = float(input("Informe sua renda mensal: R$"))
flag = int(input("Código: "))

print("Analisando", end='')
sleep(0.8)
for _ in range(3):
    print(".", end='')
    sleep(0.8)
print("\n")

if i < 18 and flag != 1:
    cabecalho("Infelizmente seu cadastro não foi aprovado, é necessário ter no mínimo 18 anos.")
elif s < 1500.00 and flag != 1:
    cabecalho("Infelizmente seu cadastro não foi aprovado, é necessário ter uma renda acima de R$1500.00.")
else:
    cabecalho("Parabéns, você foi selecionado para o programa de créditos do banco ACP!")
