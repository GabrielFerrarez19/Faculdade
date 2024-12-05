def soma_lista(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma_lista(lista[1:])

numeros = [1, 2, 3, 4, 5]
resultado = soma_lista(numeros)
print("Soma dos elementos da lista:", resultado)
