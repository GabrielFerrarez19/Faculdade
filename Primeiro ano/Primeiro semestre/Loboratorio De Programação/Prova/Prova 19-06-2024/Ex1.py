Valores = input("Digite uma lista de números inteiros separados por espaço: ")
Valores = Valores.strip()
lista_str = Valores.split()

lista = []
for num in lista_str:
    lista.append(int(num))

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

maior_sequencia = []
for seq in sequencias:
    if len(seq) > len(maior_sequencia):
        maior_sequencia = seq

if sequencias:
    print("Sub-listas crescentes:")
    for seq in sequencias:
        print(seq)
    
    print("\nA sequência crescente mais longa é:")
    print(maior_sequencia)
else:
    print("Não foram encontradas sequências crescentes na lista fornecida.")
