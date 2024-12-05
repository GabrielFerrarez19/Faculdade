#from Cod_003_salario_mes import ler_horas_dia, calula_salario

# * importa todas as funcoes do cod_003_salario_mes
from Cod_003_salario_mes import *

h = ler_horas_dia()
salario = calula_salario(h,15,50)

print(f"R$ {salario:.2f}")