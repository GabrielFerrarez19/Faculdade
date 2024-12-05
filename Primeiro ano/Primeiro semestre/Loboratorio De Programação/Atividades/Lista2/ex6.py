taxas_imposto = {
    "MG": 0.07,  # 7%
    "SP": 0.12,  # 12%
    "RJ": 0.15,  # 15%
    "MS": 0.08   # 8%
}

valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite a sigla do estado destino (MG, SP, RJ, MS): ")

if estado_destino in taxas_imposto:
    taxa_imposto = taxas_imposto[estado_destino]
    preco_final = valor_produto * (1 + taxa_imposto)
    print("O preço final do produto para o estado de", estado_destino, "é:", preco_final)
else:
    print("Erro: Estado destino inválido. Por favor, insira uma sigla de estado válida (MG, SP, RJ, MS).")