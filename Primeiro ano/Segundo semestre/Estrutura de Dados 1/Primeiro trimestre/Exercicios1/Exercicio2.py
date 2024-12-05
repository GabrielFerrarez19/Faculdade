def busca(elemento, lista):
    # retornar true caso elemento esteja na lista 
    # retornar false caso elemento não esteja na lista
    for e in lista:
        if elemento == e:
            return True 

    # percorremos a lista toda e não encontramos o elemento        
    return False 


list = [1,2,4,5,6,7,8]
x = int(input("Digite um elemento: "))

if busca(x, list):
    print("O elemento esta na lista")
else:
    print("O elemento não esta na lista")

        

