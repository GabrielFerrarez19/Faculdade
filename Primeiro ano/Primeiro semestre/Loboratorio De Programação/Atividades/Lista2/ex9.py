custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

if custo_fabrica <= 12000:
    comissao = custo_fabrica * 0.05
    impostos = custo_fabrica * 0.45
elif 12000 < custo_fabrica <= 25000:
    comissao = custo_fabrica * 0.10
    impostos = custo_fabrica * 0.35
else:
    comissao = custo_fabrica * 0.15
    impostos = custo_fabrica * 0.25

custo_consumidor = custo_fabrica + comissao + impostos

print("O custo ao consumidor do carro é de R$", custo_consumidor)