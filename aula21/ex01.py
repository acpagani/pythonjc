import pickle

arquivo = open('medias.bin', 'wb')

alunos = open('notas.txt', 'r')

mediasJSON = {}

for aluno in alunos:
    notas = aluno.split()
    soma = 0
    count = 0
    for nota in notas[1:]:
        soma += int(nota)
        count += 1

    media = soma / count

    mediasJSON[notas[0]] = media

pickle.dump(mediasJSON, arquivo)
