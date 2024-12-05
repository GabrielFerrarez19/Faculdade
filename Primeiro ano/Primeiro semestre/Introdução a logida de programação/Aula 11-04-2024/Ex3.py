camisas = ['vermelho','azul','verde','amarelo','roxo']
calcas = ['preto','cinza','branco','bege','marrom']
contador = 0

for x in camisas:
    for y in calcas:
        print(f"camisa {x} com calça {y}")
        contador +=1

print(f"Forem um total de {contador} combinações!")