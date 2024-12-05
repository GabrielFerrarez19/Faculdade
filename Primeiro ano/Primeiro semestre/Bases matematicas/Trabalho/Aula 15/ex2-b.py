import numpy as np

# Definindo as matrizes J e K
J = np.array([[1, -2, 0],
              [9, 5, -1],
              [7, 2, 4]])

K = np.array([[0.5, 2, -4],
              [3, 5, 9],
              [0, 0, 1]])

# Calculando a subtração das matrizes K e J
M = K - J

# Exibindo o resultado
print("Matriz M (K - J):")
print(M)
