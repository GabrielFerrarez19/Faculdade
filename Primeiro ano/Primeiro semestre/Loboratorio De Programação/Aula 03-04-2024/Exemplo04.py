valor1 = int(input("Digite valor1:"))

valor2 = int(input("Digite valor2:"))

maior_que = valor1 >= valor2
igualdade = valor1 == valor2

if maior_que or igualdade:
    print(f"valor {valor1} é igual a {valor2} ")
else:
    print(f"valor {valor2} é maior que {valor1}")