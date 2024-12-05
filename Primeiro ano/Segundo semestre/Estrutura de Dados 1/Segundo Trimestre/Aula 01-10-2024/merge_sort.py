def intercala(inicio,meio,fim,lista):
    i = inicio
    j = meio
    lista_ardenada = []
    while i < meio and j < fim:
        if lista[i] < lista[j]:
            lista_ardenada.append(lista[i])
            i = i+1
        else:
            lista_ardenada.append(lista[j])
            j = j + 1

    #pq i == meio ou j == fim 
    #garanto que vou pegar todos os elementos da primeira metadae da lista
    while i < meio:
        lista_ardenada.append(lista[i])
        i = i+1

    while j < fim:
        lista_ardenada.append(lista[j])
        j = j + 1
    return lista_ardenada


#main principal 
if __name__ == "__main__":
    valores = [2,9,10,15,1,8,11,12]
    inicio = 0
    fim = len(valores)
    meio = (inicio+fim//2)
    ordendada = intercala(inicio, meio, fim, valores)
    print(ordendada)
