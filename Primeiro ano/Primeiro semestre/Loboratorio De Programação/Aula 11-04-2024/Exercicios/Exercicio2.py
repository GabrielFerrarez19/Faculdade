x1 = float(input("Digite a coordenada x1: "))
y1 = float(input("Digite a coordenada y1: "))

x2 = float(input("Digite a coordenada x2: "))
y2 = float(input("Digite a coordenada y2: "))

x3 = float(input("Digite a coordenada x3: "))
y3 = float(input("Digite a coordenada y3: "))

lado1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
lado2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
lado3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    if lado1 == lado2 == lado3:
        print("Equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não é um triângulo.")

