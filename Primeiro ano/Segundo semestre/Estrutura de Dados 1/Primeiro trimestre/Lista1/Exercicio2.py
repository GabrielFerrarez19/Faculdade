def calcula_media():
    lista = input("Digite uma lista de numeros separados por virgulas: ")
    array = lista.split(",")
    array = [float(num) for num in array]
    print(array)
    soma = 0
    for num in array:
        soma += num
    
    media = soma/len(array)
    print(f"A media da lista é {media}")



calcula_media()