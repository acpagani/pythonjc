print("(_)x² + (_)x + c")
a = int(input("Coloque um valor para a: "))
print(f"({a})x² + (_)x + c")
b = int(input("Coloque um valor para b: "))
print(f"({a})x² + ({b})x + c")
c = int(input("Coloque um valor para c: "))
print(f"({a})x² + ({b})x + ({c})")

delta = b ** 2 - (4 * a * c)

if delta < 0:
    print("A sua equação não tem raízes reais!")
else:
    x1 = (-b + delta ** (1/2)) / (2 * a)
    x2 = (-b - delta ** (1/2)) / (2 * a)

    if x1 == x2:
        print(f"A raíz da equação é {x1}")
    else:
        print(f"As raízes da equação são {x1} e {x2}")
