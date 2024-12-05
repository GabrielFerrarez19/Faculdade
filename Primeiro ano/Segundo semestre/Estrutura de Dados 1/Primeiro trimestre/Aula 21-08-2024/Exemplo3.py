import os 

def menu(ETM):
    os.system("cls")
    opcao = 0 
    print(f"(1) Soma\n(2) Subtrair\n(3) Multiplicar\n(4) Dividir\n(5) Limpar memoria\n(6) Sair do programa")
    print(f"Estado da memoria {ETM}")
    opcao = int(input("Digite a opção que deseja:"))
    valor = int(input("Digite o valor desejado: "))
    return opcao, valor

def Somar(ETM, num2):
    soma = ETM + num2
    return soma

def subtrair(ETM, num2):
    subtracao = ETM - num2
    return subtracao

def Multiplicar(ETM, num2):
    Mult = ETM * num2 
    return Mult

def dividir(ETM, num2):
    div = ETM / num2 
    return div 

def LimpaMemoria(memoria):
    memoria = 0
    return memoria

def calculadora():
    etm = 0 
    opcao = 0


    while opcao != 6:
        opcao, valoresco = menu(etm)
        
        if opcao == 1:
            etm = Somar(etm, valoresco)
        elif opcao == 2:
            etm = subtrair(etm, valoresco)
        elif opcao == 3:
            etm = Multiplicar(etm, valoresco)
        elif opcao == 4:
            etm = dividir(etm, valoresco)
        elif opcao == 5:
            etm = LimpaMemoria(etm)



calculadora()
print(f"Fim do programa")