def conta_letra():
    frase = input("Digite uma frase: ")
    letraContar = input("Digite a letra qie deseja contar na frase: ")

    contador = 0

    for letra in frase:
        if letra == letraContar:
            contador +=1
    print(contador)

conta_letra()