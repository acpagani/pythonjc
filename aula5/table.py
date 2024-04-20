import os


def header(txt):
    print("=" * (len(txt) + 10))
    print(txt.center(len(txt) + 10))
    print("=" * (len(txt) + 10))


cont = 's'

header("TABLE MANAGEMENT")
while cont == 's':
    if not os.path.exists("table.txt"):
        file = open("table.txt", "x")

    opt = input("""
Para ADICIONAR um valor à tabela, digite 'a'
Para VER a tabela, digite 'v'
Para DELETAR a tabela, digite 'd'
opção: """).lower().strip()

    if opt == 'a':
        file = open("table.txt", "a")
        header("ADICIONAR VALORES")
        nome = input("Nome: ")
        idade = int(input(("Idade: ")))
        telefone = input("Telefone: ")
        address = input("Endereço: ")
        math = int(input("Quanto é 2 + 1? "))

        file.write(f"{nome:<10}|{idade:<10}|{telefone:<10}|{address:<10}|{math:<10}\n")
        file.close()

    elif opt == 'v':
        file = open("table.txt", "r")
        header("TABELA")
        for f in file:
            print(f)
        file.close()

    elif opt == 'd':
        if os.path.exists("table.txt"):
            os.remove("table.txt")
        else:
            print("A tabela não existe")

    cont = input("Deseja continuar? [s/n] ").lower().strip()
