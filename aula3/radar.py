v = int(input("Velocidade do carro (km/h): "))

if v > 80:
    income = (v - 80) * 5
    print(f"\033[1;31mMULTADO\033[m. Você ultrapassou o limite de velocidade e recebeu uma multa de R${income}")
else:
    print("\033[1;42mO automóvel está abaixo do limite de velocidade.\033[m")
