#1

def ordenacao_bolha(lista):
    comprimento = len(lista)
    contagem_trocas = 0
    for i in range(comprimento):
        for j in range(comprimento - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                contagem_trocas += 1
    return contagem_trocas

def ordenacao_insercao(lista):
    comprimento = len(lista)
    contagem_trocas = 0
    for i in range(1, comprimento):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
            contagem_trocas += 1
        lista[j + 1] = chave
    return contagem_trocas

def ordenar_e_contar(lista, func_ordenacao):
    copia_lista = lista[:]
    return func_ordenacao(copia_lista)

def exibir_resultados(listas, resultados):
    print("Lista               | Ordenação Bolha | Ordenação Inserção")
    for i, lista in enumerate(listas):
        trocas_bolha, trocas_insercao = resultados[i]
        print(f"{lista} | {trocas_bolha:<17} | {trocas_insercao}")

# Listas de teste
listas_teste = [
    [2, 4, 6, 8, 10, 12],
    [12, 10, 8, 6, 4, 2],
    [5, 2, 8, 4, 6, 1],
    [1, 2, 3, 9, 8, 7]
]

# Calculando os resultados
resultados = [
    (
        ordenar_e_contar(lista, ordenacao_bolha),
        ordenar_e_contar(lista, ordenacao_insercao)
    )
    for lista in listas_teste
]

# Mostrando os resultados
exibir_resultados(listas_teste, resultados)