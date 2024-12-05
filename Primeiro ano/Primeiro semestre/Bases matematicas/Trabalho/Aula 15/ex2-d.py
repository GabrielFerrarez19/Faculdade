import numpy as np

# Definindo a matriz K
K = np.array([[0.5, 2, -4],
              [3, 5, 9],
              [0, 0, 1]])

# Calculando o produto de K por ela mesma
O = np.dot(K, K)

# Exibindo o resultado
print("Matriz O (K^2):")
print(O)
