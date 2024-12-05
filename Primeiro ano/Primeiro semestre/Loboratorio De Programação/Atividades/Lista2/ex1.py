import math 

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Número inválido")
else:
    if numero == 0:
        print("Não é possível calcular o logaritmo de 0")
    else:
        logaritmo = 0
        while numero > 1:
            numero /= math.e
            logaritmo += 1
        print("O logaritmo de", numero, "é:", logaritmo)
