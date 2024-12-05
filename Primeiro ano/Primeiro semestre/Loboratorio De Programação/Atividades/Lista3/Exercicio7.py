n = int(input("Digite um número inteiro: "))

# Iniciar a verificação com o menor número inteiro positivo consecutivo, que é 1
consecutivo = 1

while True:
    # Calcular o produto dos 3 números inteiros consecutivos
    produto = consecutivo * (consecutivo + 1) * (consecutivo + 2)
    
    # Se o produto for igual ao número fornecido, então possui a propriedade
    if produto == n:
        print(f"{n} é igual ao produto de {consecutivo}, {consecutivo + 1} e {consecutivo + 2}.")
        break
    # Se o produto for maior que o número fornecido, então não possui a propriedade
    elif produto > n:
        print(f"{n} não possui a propriedade de ser o produto de 3 números inteiros consecutivos.")
        break
    else:
        # Se o produto for menor que o número fornecido, tentamos com o próximo conjunto de números consecutivos
        consecutivo += 1
