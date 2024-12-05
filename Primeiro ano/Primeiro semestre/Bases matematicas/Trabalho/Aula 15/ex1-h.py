import numpy as np

# Definindo a negação da matriz H, -H
H_neg = np.array([[-1, -3, 2, 0], [3, -4, 0, 1], [-5, -1, 4, -2]])

# Imprimindo a negação da matriz H, -H
print("Negação da matriz H, -H:")
print(H_neg)

# Verificando as dimensões da negação da matriz H, -H
num_linhas, num_colunas = H_neg.shape

# Imprimindo manualmente as identificações da negação da matriz H, -H
print("\nIdentificações:")
print("( ) Matriz Inversa")
print("(X) Matriz Linha")
print("( ) Matriz Quadrada")
print("( ) Matriz Transposta")
print("( ) Matriz Coluna")
print("(X) Matriz Nula")
print("( ) Matriz Identidade")
print("(X) Matriz Oposta")
