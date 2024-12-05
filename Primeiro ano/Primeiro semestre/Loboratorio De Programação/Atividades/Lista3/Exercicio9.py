x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

# Inicializar variáveis para armazenar o resultado da divisão e o resto
quociente = 0
resto = x

# Enquanto o resto for maior ou igual a y, continuamos subtraindo y do resto
while resto >= y:
    resto -= y
    quociente += 1

print("Resultado da divisão de x por y:", quociente)
print("Resto da divisão de x por y:", resto)
