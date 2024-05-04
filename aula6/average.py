notas = list()
count = 0
num = int(input("Número de notas a serem lidas: "))

for c in range(num):
    nota = float(input(f"Nota {c + 1}: "))
    count += 1
    notas.append(nota)

avg = sum(notas) / count

print(f"A média de todas as notas é {avg}")
