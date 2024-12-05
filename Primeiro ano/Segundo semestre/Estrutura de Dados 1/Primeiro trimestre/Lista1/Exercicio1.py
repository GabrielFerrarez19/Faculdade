def converte_temp():
    graus = float(input("Digite o valor em graus: "))
    fah = (graus * 1.8) + 32 
    print(f"O valor de Graus em Fahrenheit é {fah}")
    return fah 


converte_temp()