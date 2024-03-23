d = int(input("Dias: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))

total_segundos = (s) + (m * 60) + (h * 60 ** 2) + (d * 24 * 3600)

print(f"Isso aí tem {total_segundos} segundos")
