def get_fruit(dict, cod):
    for key, value in dict.items():
        if cod == key:
            return value
    return 1


frutas = {
    "1": 0.5,
    "2": 1,
    "3": 4,
    "5": 7,
    "9": 8
}

compras = 0

while True:
    opt = input("Código: ")
    quant = int(input("Quatidade: "))

    if get_fruit(frutas, opt) == 1:
        break

    compras += get_fruit(frutas, opt) * quant

    print(f"Valor da compra: R${compras}")
    cont = input("Deseja continuar? [s/n] ").lower().strip()

    if cont == 'n':
        break
