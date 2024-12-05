import random

def selection_sort(L):
    for i in range(len(L)-1):
        menor = i 
        for j in range(i+1, len(L)):
            if L[menor] > L[j]:
                menor = j
        L[i], L[menor] = L[menor], L[i]
        print(L)  
    return L

lista = random.sample(range(1, 100001), 100000)
 
lista_ordenada = selection_sort(lista)
print(lista_ordenada[:100000])  