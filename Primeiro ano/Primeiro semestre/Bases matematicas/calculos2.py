#Definindo a Função da Soma
def somar(valores):
    return sum(valores)

#Definir a Operação
def realizar_operacao():
    print ("Escolha a Operação:")
    print ("1 - Somar")
    print ("2 - Subtrair")
    print ("3 - Multiplicar")
    print ("4 - Dividir")
    
escolha = input("Digite o número corresponde a operação: ")

#Verificar se a opção é válida
if escolha not in ['1','2','3','4']:
    print('Opção Inválida. Por Favor digite um número entre 1 e 4: ')

#Solicita o numero de Valores para operação
num_valores = int(input("Digite o númeor de valores para a operação: "))

valores = []

#Solicita os valores para a operação
for i in range (num_valores):
    valor = float(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

#Executar a Operação Escolhida
if escolha =='1':
    resultado = somar(valores)
    print(f"Resultado da soma: {resultado}")

