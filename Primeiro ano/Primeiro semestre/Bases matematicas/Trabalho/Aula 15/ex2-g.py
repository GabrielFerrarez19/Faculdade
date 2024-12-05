import numpy as np

# Definindo a matriz K
K = np.array([[2, 1, 3],
              [1, 2, 1],
              [1, 1, 1]])

# Verificando se a matriz K é invertível (não singular)
if np.linalg.det(K) != 0:
    # Calculando a inversa de K
    R = np.linalg.inv(K)
    print("Matriz R (inversa de K):")
    print(R)
else:
    print("A matriz K é singular e não possui inversa.")
