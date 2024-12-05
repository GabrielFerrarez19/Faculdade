
#funcao com parametros mas sem retorno
def calula_salario(horas_dia, dias_trabalhados,valor_hora = 88.5):
    #valor_hora = 88.5
    salario = horas_dia*valor_hora*dias_trabalhados
    print(f"R$ {salario:.2f}")


if (__name__ == "__main__"):
    print("A1")
    calula_salario(8,18)
    print("A2")
    calula_salario(3,10,100)
    print("A3")
