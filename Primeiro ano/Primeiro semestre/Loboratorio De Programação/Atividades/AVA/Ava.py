# Solicitar o valor total do centro de usinagem
valor_total = float(input("Digite o valor total do centro de usinagem: "))

# Calcular o valor pago à vista (1/3 do valor total)
valor_a_vista = valor_total / 3

# Calcular o valor restante da dívida
restante_divida = valor_total - valor_a_vista

# Calcular 50% do restante da dívida para pagamento em 30 dias sem juros
valor_30_dias = restante_divida * 0.5

# Calcular o restante da dívida após o pagamento em 30 dias
restante_divida = valor_30_dias

# Calcular juros de 5% sobre o restante da dívida para pagamento em 60 dias
juros = restante_divida * 0.05

#calcula o valor aplicando o juros de 5%
juros_real = juros + valor_30_dias

# Somar todos os valores pagos para obter o valor final do produto
valor_final = valor_a_vista + valor_30_dias + juros_real

# Exibir os resultados
print(f"Valor do centro de usinagem: {valor_total:.2f}")
print(f"Valor pago à vista: {valor_a_vista:.2f}")
print(f"Valor pago em 30 dias: {valor_30_dias:.2f}")
print(f"Valor pago com juros de 5%: {juros_real:.2f}")
print(f"Valor final do produto: {valor_final:.2f}")
