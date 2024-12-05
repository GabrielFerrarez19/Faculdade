#horas_dia = 8 
#valor_hora = 88.5
#dias_trabalhados = 18

#def -> definir uma funcao
#def nome da funcao (<parametros>)

#funcao com parametros mas sem retorno
def calula_salario(horas_dia, dias_trabalhados):
    valor_hora = 88.5
    salario = horas_dia*valor_hora*dias_trabalhados
    print(f"R$ {salario:.2f}")


print(__name__)
if (__name__ == "__main__"):
    calula_salario(8,18)
    calula_salario(3,10)
