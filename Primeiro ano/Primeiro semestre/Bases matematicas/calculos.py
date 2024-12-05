def calculadora():
    # Função para adicionar dois números
    def adicionar(numeros):
        return sum(numeros)

    # Função para subtrair dois números
    def subtrair(numeros):
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado -= num
        return resultado

    # Função para multiplicar dois números
    def multiplicar(numeros):
        resultado = 1
        for num in numeros:
            resultado *= num
        return resultado

    # Função para dividir dois números
    def dividir(numeros):
        resultado = numeros[0]
        for num in numeros[1:]:
            if num == 0:
                print("Erro: Divisão por zero!")
                return None
            resultado /= num
        return resultado

 
# Menu de seleção de operações
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    escolha = input("Digite sua escolha (1/2/3/4): ")


 # Capturando os números de entrada
    numeros = []
    while True:
        numero = input("Digite um número (ou 'q' para parar): ")
        if numero.lower() == 'q':
            break
        try:

            numeros.append(float(numero))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")


            # Realizando a operação selecionada
    if escolha == '1':
        resultado = adicionar(numeros)
    elif escolha == '2':
        resultado = subtrair(numeros)
    elif escolha == '3':
        resultado = multiplicar(numeros)
    elif escolha == '4':
        resultado = dividir(numeros)
    else:
        print("Opção inválida!")
        return

    # Exibindo o resultado
    if resultado is not None:
        print("O resultado é:", resultado)

# Chamando a função calculadora
calculadora()