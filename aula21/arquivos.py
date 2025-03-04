notas = open("notas.txt", "r+")

alunos = notas.readlines()

for aluno in alunos:
    notas = aluno.split()
    maior = 0
    menor = int(notas[1])
    for i in notas[1:]:
        if int(i) > maior:
            maior = int(i)
        if int(i) < menor:
            menor = int(i)

    print(f"{notas[0]} - Maior Nota: {maior}; Menor Nota: {menor}")
