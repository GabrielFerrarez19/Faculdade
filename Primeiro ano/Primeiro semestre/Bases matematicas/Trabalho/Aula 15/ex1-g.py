import numpy as np

# Definindo a transposta da matriz G, G^T
G_transposta = np.array([[1, 0, 1], [0, 1, 2]])

# Imprimindo a transposta da matriz G, G^T
print("Transposta da matriz G, G^T:")
print(G_transposta)

# Verificando as dimensões da transposta da matriz G, G^T
num_linhas, num_colunas = G_transposta.shape

# Imprimindo manualmente as identificações da transposta da matriz G, G^T
print("\nIdentificações:")
print("( ) Matriz Inversa")
print("(X) Matriz Linha")
print("( ) Matriz Quadrada")
print("(X) Matriz Transposta")
print("(X) Matriz Coluna")
print("(X) Matriz Nula")
print("( ) Matriz Identidade")
print("( ) Matriz Oposta")
