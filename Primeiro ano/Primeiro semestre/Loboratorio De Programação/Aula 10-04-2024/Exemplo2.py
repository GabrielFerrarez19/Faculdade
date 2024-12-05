entrada = input("Digite uma lista de números inteiros separados por espaço: ")
lista = list(map(int, entrada.split()))

# Contagem de ocorrências usando um dicionário
contagem = {}
for numero in lista:
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

# Criando uma nova lista apenas com os números que aparecem mais de uma vez
numeros_repetidos = [numero for numero, qtd in contagem.items() if qtd > 1]

# Exibindo o dicionário de contagem e a nova lista
print("Dicionário com a contagem de cada número:")
print(contagem)

print("\nLista de números que aparecem mais de uma vez:")
print(numeros_repetidos)
