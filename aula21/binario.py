import pickle

arquivo = open('aula.bin', 'wb')

lista = [5, 10, "ola", 10.5]

pickle.dump(lista, arquivo)
