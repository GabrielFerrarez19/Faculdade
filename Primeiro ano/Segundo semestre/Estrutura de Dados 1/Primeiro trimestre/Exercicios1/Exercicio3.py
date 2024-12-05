def conta_vogais(texto):
    vogais = ['a','e','i','o','u','A','E','I','O','U']
    qtd = 0 
    for letra in texto:
        # print(letra)
        if letra in vogais:
            qtd = qtd + 1
    return qtd


frase = ("Ola mundo")
quatidade = conta_vogais(frase)
print (f"{frase} tem {quatidade} vogais" )