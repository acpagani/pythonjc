from time import sleep

fila = list()

while True:
    nome = input("Pessoa que entrou na fila: ")
    fila.insert(0, nome)

    print(f"|{fila} ...... Atendimento |")

    cont = input("Deseja fechar a fila? [S/N] ")

    if cont.upper() == "S":
        break

print("=" * 30)
for _ in range(len(fila)):
    print(f"{fila} ..... Atendimento\n")

    atendido = fila.pop()

    for c in range(3):
        print(".", end='')
        sleep(1)

    print(f"{atendido.capitalize()} foi atendido!\n")

