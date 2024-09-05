def verify_matrix(m):
    num_col = len(m[0])
    for i in m:
        if len(i) != num_col:
            return False
    return True


def print_matrix(m):
    for i in m:
        print("|", end=' ')
        for j in i:
            print(f"{j:^3}", end=' ')
        print("|")


def sum_sub_matrix(m, n, symbol):
    if not verify_matrix(m) or not verify_matrix(n):
        return 'Os dados passados não são matrizes válidas'
    if len(m) != len(n) or len(m[0]) != len(n[0]):
        return 'As matrizes precisam ter o mesmo número de linhas e colunas'

    matrix_operada = []
    for i in range(len(m)):
        lista = []
        for j in range(len(n)):
            if symbol == "+":
                lista.append(m[i][j] + n[i][j])
            elif symbol == "-":
                lista.append(m[i][j] - n[i][j])
            else:
                return "Operação inválida"
        matrix_operada.append(lista)
    return matrix_operada


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

b = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix(sum_sub_matrix(a, b, "-"))
