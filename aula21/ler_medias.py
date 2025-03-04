import pickle

arquivo = open('medias.bin', 'rb')

medias = pickle.load(arquivo)

print(medias)
