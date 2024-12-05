import numpy as np
#Matriz 1D com 5 elementos
matriz1 = np.arange(6,11)
#matriz 1D com 5 elementos
matriz2 = np.array([1,2,3,4,5])
print(f"Matriz1 : {matriz1}")
print(f"Matriz2 : {matriz2}")
print()
#soma entre os elementos das matrizes: matriz1 + matriz2 
matriz3 = matriz1 + matriz2
print(f"matriz1 + matriz2: {matriz3} ")
#subtração entre os elementos das matrizes: matriz1 - matriz2
matriz4 = matriz1 - matriz2
print(f"matriz1 = matriz2: {matriz4}")
#multiplicação entre os elementos das matrizes: matriz1 * matriz 2
matriz5 = matriz1 * matriz2
print(f"matriz1 * matriz2: {matriz5}")
#divisão entres os elementos das matrizes: matriz1 / matriz2
matriz6 = matriz1 / matriz2
print(f"matriz1 / matriz2: {matriz6}")
