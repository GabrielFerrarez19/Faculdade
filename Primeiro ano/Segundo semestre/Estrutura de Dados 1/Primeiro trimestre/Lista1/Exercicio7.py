def bubble_sort(array):
    n = len(array)
    # Passando por toda a lista
    for i in range(n):
        # Últimos i elementos já estão ordenados
        for j in range(0, n - i - 1):
            # Comparando notas (índice 1 de cada tupla)
            if array[j][1] < array[j + 1][1]:
                # Se a nota do aluno atual for menor, trocamos de posição
                array[j], array[j + 1] = array[j + 1], array[j]


frases = [
    "O céu está lindo esta noite.",
    "A tecnologia está mudando o mundo rapidamente.",
    "Aprender algo novo todos os dias é fundamental.",
    "A prática leva à perfeição.",
    "Nunca é tarde para começar um novo projeto."
]

fraseComTamanho = {
    frases: len(frases) for frases in frases
}

print(fraseComTamanho)

lista_frases_tamanho = list(fraseComTamanho.items())
print(lista_frases_tamanho)
bubble_sort(lista_frases_tamanho)

print("Essa e a lista ordenada usando bubble sort:")

i = 1
for lista_frases_tamanho in lista_frases_tamanho:
    print(f"{i} Tamanho:{lista_frases_tamanho[1]} Frase:{lista_frases_tamanho[0]}" )