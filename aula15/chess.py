import matplotlib.pyplot as plt

tabuleiro = []

tamanho_tabuleiro = 500

for l in range(tamanho_tabuleiro):
    linha = []
    for c in range(tamanho_tabuleiro):
        coluna = []
        if l % 2 == 0:
            if c % 2 == 0:
                coluna.append(255)
                coluna.append(255)
                coluna.append(255)
            else:
                coluna.append(0)
                coluna.append(0)
                coluna.append(0)
        else:
            if c % 2 == 0:
                coluna.append(0)
                coluna.append(0)
                coluna.append(0)
            else:
                coluna.append(255)
                coluna.append(255)
                coluna.append(255)
        linha.append(coluna)
    tabuleiro.append(linha)

plt.imshow(tabuleiro)
plt.axis("off")
plt.show()
