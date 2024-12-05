opcao = 's'
nome = input("Digite o nome completo: ")

while opcao == 's':
    print("-"*10)
    indice = int(input("Digite o posicao: "))
    print(nome)
    print(nome[indice])
    opcao = input("Deseja continuar?" )