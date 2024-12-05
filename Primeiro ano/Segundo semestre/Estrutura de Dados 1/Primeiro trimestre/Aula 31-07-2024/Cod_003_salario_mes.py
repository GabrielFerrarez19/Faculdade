
#funcao com parametros mas com retorno
def calula_salario(horas_dia, dias_trabalhados,valor_hora = 88.5):
    #valor_hora = 88.5
    salario = horas_dia*valor_hora*dias_trabalhados
    return salario

#funcao sem parametros e sem retorno 
def boas_vindas():
    print("-"*28)
    print("-"*10,"inicio","-"*10)

def ler_horas_dia():
    hd = float(input("Digite a quantidade de horas trabalhadas por dia: "))
    return hd

if (__name__ == "__main__"):
    boas_vindas()
    horas = ler_horas_dia()
    print("A1")
    salario1 = calula_salario(horas,18)
    print("A2")
    salario2 = calula_salario(ler_horas_dia(),10,100)
    print("A3")

    print(f"R${salario1:.2f}")
    print(f"R${salario2:.2f}")
    print(f"O dobro de R${salario2:.2f} é R${salario2*2:.2f}")