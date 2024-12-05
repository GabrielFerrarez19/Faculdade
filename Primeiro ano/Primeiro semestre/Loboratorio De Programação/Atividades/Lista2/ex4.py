# Exibir o menu de opções
print("Escolha a opção:")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")

opcao = int(input("Opção: "))

if opcao == 1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("A soma de", num1, "e", num2, "é:", resultado)
elif opcao == 2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = abs(num1 - num2)
    print("A diferença entre", num1, "e", num2, "é:", resultado)
elif opcao == 3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("O produto de", num1, "e", num2, "é:", resultado)
elif opcao == 4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número (o denominador não pode ser zero): "))
    if num2 != 0:
        resultado = num1 / num2
        print("A divisão de", num1, "por", num2, "é:", resultado)
    else:
        print("Erro: O denominador não pode ser zero.")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")