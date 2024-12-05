n = int(input("Digite quantos valores deseja somar os quadrados: "))

soma_quadrados = 0

for i in range(n):
    valor = float(input(f"Digite o {i+1}º valor: "))
    soma_quadrados += valor ** 2

print("A soma dos quadrados dos valores é:", soma_quadrados)
