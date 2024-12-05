import numpy as np

# Definindo a matriz J
J = np.array([[1, -2, 0],
              [9, 5, -1],
              [7, 2, 4]])

# Calculando a inversa de J
Q = np.linalg.inv(J)

# Exibindo o resultado
print("Matriz Q (inversa de J):")
print(Q)
