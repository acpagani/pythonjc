lista = [i for i in range(100) if i % 3 == 0]

lista_matriz = [[int(input(f"a{j}{i}:")) for i in range(int(input("Número de colunas")))] for j in range(int(input("Número de linhas")))]

print(lista_matriz)
