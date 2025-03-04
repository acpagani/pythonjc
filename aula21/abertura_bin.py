import pickle

arquivo = open('aula.bin', 'rb')

lido = pickle.load(arquivo)

print(lido)
