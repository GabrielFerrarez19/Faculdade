import os
from word2number import w2n
from googletrans import Translator

def menu(ETM):
    os.system("cls")
    opcao = 0 
    print(f"(1) Soma\n(2) Subtrair\n(3) Multiplicar\n(4) Dividir\n(5) Limpar memória\n(6) Sair do programa")
    print(f"Estado da memória: {ETM}")
    opcao = int(input("Digite a opção que deseja: "))
    valor_extenso = input("Digite o valor desejado por extenso: ")
    valor_traduzido = traduzirParaIngles(valor_extenso)
    valor_numero = numeroPorExtenco(valor_traduzido)
    return opcao, valor_numero

def Somar(ETM, num2):
    return ETM + num2

def Subtrair(ETM, num2):
    return ETM - num2

def Multiplicar(ETM, num2):
    return ETM * num2

def Dividir(ETM, num2):
    return ETM / num2

def LimpaMemoria():
    return 0

def calculadora():
    etm = 0 
    opcao = 0

    while opcao != 6:
        opcao, valor = menu(etm)
        
        if opcao == 1:
            etm = Somar(etm, valor)
        elif opcao == 2:
            etm = Subtrair(etm, valor)
        elif opcao == 3:
            etm = Multiplicar(etm, valor)
        elif opcao == 4:
            etm = Dividir(etm, valor)
        elif opcao == 5:
            etm = LimpaMemoria()

    print(f"Fim do programa")

def numeroPorExtenco(numero):
    traducao = w2n.word_to_num(numero)
    return traducao

def traduzirParaIngles(extenso):
    translator = Translator()
    numero = translator.translate(extenso, src='pt', dest='en')
    return numero.text  

calculadora()

