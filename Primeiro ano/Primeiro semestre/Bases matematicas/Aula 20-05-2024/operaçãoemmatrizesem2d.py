import numpy as np
M1 = np.array([[1,2],[3,4]])
print(f"matriz 1: \n{M1}")
M2 = np.array([[1,2],[3,4]])
print(f'\nmatriz2: \n{M2}')

#SOMA
somaresultado = M1 + M2
print(f"m1 + m2 = \n{somaresultado}")

#Subtração
subtraçaoresultado = M1 - M2
print(f"m1 - m2 = \n{subtraçaoresultado}")

#divisão
divisaoresultado = M1 / M2
print(f"m1 / m2 = \n{divisaoresultado}")

#multiplicação
multiplicacaoresultado = M1.dot(M2)
print(f"m1 * m2 = \n{multiplicacaoresultado}")