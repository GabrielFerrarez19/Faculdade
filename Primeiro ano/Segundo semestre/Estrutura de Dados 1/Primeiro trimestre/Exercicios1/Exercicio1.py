def calcula_lista(lista):
    s = 0
    for elemento in lista:
        s += elemento 
    return s 

x = calcula_lista([10,20,30])
print(f"A soma é {x}")