#entrada de dados  altura
altura = float(input("Digite sua altura em metros:"))

#calcula o peso ideal
pesohomem = ( 72.7* altura) - 58
pesomulher = ( 62.1* altura) - 44.7


#imprime o peso ideal para aquela pessoa
print (f"O peso ideal para uma mulher é {pesomulher:.2f} e para o homem é {pesohomem:.2f}")