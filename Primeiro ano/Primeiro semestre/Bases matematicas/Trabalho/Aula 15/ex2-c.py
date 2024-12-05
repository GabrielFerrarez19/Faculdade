import numpy as np

# Definindo as matrizes J e K
J = np.array([[1, -2, 0],
              [9, 5, -1],
              [7, 2, 4]])

K = np.array([[0.5, 2, -4],
              [3, 5, 9],
              [0, 0, 1]])

# Calculando a multiplicação das matrizes J e K
N = np.dot(J, K)

# Exibindo o resultado
print("Matriz N (J * K):")
print(N)
