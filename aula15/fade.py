import matplotlib.pyplot as plt
import numpy as np

painel = []
tam = 10

cor1 = [255, 0, 0]
cor2 = [0, 0, 255]

transition = [
    [
        (((cor2[0] - cor1[0]) * (i + 1)) / tam)
         if
            cor2[0] > cor1[0]
         else
            cor1[0] + (((cor2[0] - cor1[0]) * (i + 1)) / tam)
         for i in range(tam)
     ],
    [((cor2[1] - cor1[1]) * (i + 1)) / tam for i in range(tam)],
    [((cor2[2] - cor1[2]) * (i + 1)) / tam for i in range(tam)]
]



for l in range(tam):
    linha = []
    for c in range(tam):
        coluna = []
        coluna.append([transition[0][c], transition[1][c], transition[2][c]])
    linha.append(coluna)


print(transition)
plt.imshow(linha)
plt.axis("off")
plt.show()
