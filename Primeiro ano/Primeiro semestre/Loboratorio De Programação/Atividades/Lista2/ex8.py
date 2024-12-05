venda_mensal = float(input("Digite o valor da venda mensal: "))

if venda_mensal >= 100000:
    comissao = 700 + (venda_mensal * 0.16)
elif 80000 <= venda_mensal < 100000:
    comissao = 650 + (venda_mensal * 0.14)
elif 60000 <= venda_mensal < 80000:
    comissao = 600 + (venda_mensal * 0.14)
elif 40000 <= venda_mensal < 60000:
    comissao = 550 + (venda_mensal * 0.14)
elif 20000 <= venda_mensal < 40000:
    comissao = 500 + (venda_mensal * 0.14)
else:
    comissao = 400 + (venda_mensal * 0.14)

print("A comissão é de R$", comissao)