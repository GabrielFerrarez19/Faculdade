def selection_sort(array):
    # Passar por todos os elementos da lista
    for i in range(len(array)):
        # Encontrar o menor elemento na parte não ordenada
        menor_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[menor_idx]:
                menor_idx = j
        
        # Trocar o menor elemento encontrado com o primeiro elemento não ordenado
        array[i], array[menor_idx] = array[menor_idx], array[i]

Cartas = [7, 1, 13, 9, 3]

selection_sort(Cartas)

i = 1 
for Cartas in Cartas:
    print(f"{i} Numero da carta: {Cartas}")