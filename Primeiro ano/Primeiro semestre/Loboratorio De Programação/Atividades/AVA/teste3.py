# Algoritmo "quatro"
salario_base = float(input("Digite o salário base: "))
filhos = int(input("Digite o número de filhos: "))
tempo = int(input("Digite o tempo de serviço: "))

total = salario_base * 0.10 + 50.00 * filhos + 10.00 * tempo

print("Salário base:", salario_base)
print("Total a receber:", total)