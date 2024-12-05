erro = float(input("Digite o valor do erro aceitável: "))

pi_4 = 0
parcela = 1
denominador = 1
pi_4_anterior = 0

while True:
    pi_4_anterior = pi_4
    pi_4 += parcela
    
    # Próxima parcela: sinal alternado e incremento do denominador
    denominador += 2
    parcela = 1 / denominador if denominador % 4 == 1 else -1 / denominador
    
    # Verificar se a diferença entre iterações sucessivas é menor que o erro aceitável
    if abs(pi_4 - pi_4_anterior) < erro:
        break

pi = pi_4 * 4
print("O valor de Pi calculado é:", pi)
