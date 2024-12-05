entrada = input("Digite uma lista de números inteiros separados por espaço: ")
lista = entrada.split()

lista_inteiros = []
for numero in lista:
    lista_inteiros.append(int(numero))

contagem = {}
for numero in lista_inteiros:
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

numeros_repetidos = []
for numero, qtd in contagem.items():
    if qtd > 1:
        numeros_repetidos.append(numero)

print("Dicionário com a contagem de cada número:")
print(contagem)

print("\nLista de números que aparecem mais de uma vez:")
print(numeros_repetidos)
