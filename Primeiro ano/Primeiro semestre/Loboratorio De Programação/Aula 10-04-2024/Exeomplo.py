entrada = input("Digite uma lista de números inteiros separados por espaço: ")
lista = list(map(int, entrada.split()))

# Identificando sequências crescentes
sequencias = []
sequencia_atual = [lista[0]]

for i in range(1, len(lista)):
    if lista[i] > lista[i-1]:
        sequencia_atual.append(lista[i])
    else:
        if len(sequencia_atual) > 1:
            sequencias.append(sequencia_atual)
        sequencia_atual = [lista[i]]

if len(sequencia_atual) > 1:
    sequencias.append(sequencia_atual)

# Encontrando a maior sequência
maior_sequencia = []
for seq in sequencias:
    if len(seq) > len(maior_sequencia):
        maior_sequencia = seq

# Exibindo resultados
if sequencias:
    print("Sub-listas que são sequências crescentes:")
    for seq in sequencias:
        print(seq)
    
    print("\nA sequência crescente mais longa é:")
    print(maior_sequencia)
else:
    print("Não foram encontradas sequências crescentes na lista fornecida.")
