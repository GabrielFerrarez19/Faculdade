import numpy as np

# Criando uma matriz 10x10 de números de 1 a 100
matriz = np.arange(1, 101).reshape(10, 10)

# Loop para percorrer cada elemento da matriz e verificar se é primo ou não
for i in range(10):  # Percorre as linhas da matriz
    for j in range(10):  # Percorre as colunas da matriz
        numero = matriz[i, j]  # Obtém o número na posição (i, j)
        
        # Verificando se o número é primo
        if numero <= 1:  # Se o número for 1 ou menor, não é primo
            primo = False
        else:
            primo = True  # Supõe que o número é primo
            for k in range(2, int(numero**0.5) + 1):  # Loop para verificar se o número é divisível por algum número até a raiz quadrada do número
                if numero % k == 0:  # Se o número for divisível por outro número, não é primo
                    primo = False
                    break  # Sai do loop, pois já sabemos que o número não é primo
        
        # Imprimindo o resultado
        if primo:
            print(f"O número {numero} na posição ({i+1}, {j+1}) é primo.")  # Se o número for primo, imprime uma mensagem indicando isso
        else:
            print(f"O número {numero} na posição ({i+1}, {j+1}) não é primo.")  # Se o número não for primo, imprime uma mensagem indicando isso
