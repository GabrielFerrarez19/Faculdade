def soma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + soma_digitos(n // 10)

numero = 12345
resultado = soma_digitos(numero)
print("Soma dos dígitos:", resultado)
