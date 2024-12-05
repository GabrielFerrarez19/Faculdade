#2

def ordenar_bolha(lista):
    tamanho = len(lista)
    contagem_trocas = 0
    for i in range(tamanho):
        for j in range(tamanho - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                contagem_trocas += 1
    return contagem_trocas

def ordenar_insercao(lista):
    tamanho = len(lista)
    contagem_trocas = 0
    for i in range(1, tamanho):
        valor_atual = lista[i]
        k = i - 1
        while k >= 0 and valor_atual < lista[k]:
            lista[k + 1] = lista[k]
            k -= 1
            contagem_trocas += 1
        lista[k + 1] = valor_atual
    return contagem_trocas

# Conjuntos de dados para teste
conjuntos_dados = [
    [2, 4, 6, 8, 10, 12],
    [12, 10, 8, 6, 4, 2],
    [5, 2, 8, 4, 6, 1],
    [1, 2, 3, 9, 8, 7]
]

# Armazenando os resultados das ordenações
resultado_ordenacoes = []

for dados in conjuntos_dados:
    resultado_ordenacoes.append([
        ordenar_bolha(dados[:]),
        ordenar_insercao(dados[:])
    ])

# Exibindo os resultados
print("Dados                | Ordenação Bolha | Ordenação Inserção")
for i, dados in enumerate(conjuntos_dados):
    print(f"{dados} | {resultado_ordenacoes[i][0]}             | {resultado_ordenacoes[i][1]}")
