def inverte_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + inverte_string(s[:-1])

texto = "recursao"
resultado = inverte_string(texto)
print("String invertida:", resultado)
