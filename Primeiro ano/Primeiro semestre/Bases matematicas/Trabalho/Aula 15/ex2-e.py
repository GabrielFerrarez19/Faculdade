import numpy as np

# Definindo a matriz J
J = np.array([[1, -2, 0],
              [9, 5, -1],
              [7, 2, 4]])

# Substituir valores negativos por zero
J_non_negative = np.where(J >= 0, J, 0)

# Calculando a raiz quadrada de cada elemento da matriz J
P = np.sqrt(J_non_negative)

# Exibindo o resultado
print("Matriz P (sqrt(J)):")
print(P)
