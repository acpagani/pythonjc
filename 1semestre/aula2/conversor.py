sec = int(input("Indique quantos segundos deverão ser convertidos: "))

segundos = sec % 60
min = sec // 60
minutos = min % 60
horas = min // 60
print(f"{sec} segundos equivalem a {horas} horas, {minutos} minutos e {segundos} segundos")
