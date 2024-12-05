centavo1 = int(input("Digite quantas moedas de 1 centavo tem: "))

centavo5 = int(input("Digite a quantidade de moedas de 5 centavos: "))

centavo10 = int(input("Digite a quantidade de moedas de 10 centavos: "))

centavo25 = int(input("Digite a quantidade de moedas de 25 centavos: "))

centavo50 = int(input("Digite a quantidade de moedas de 50 centavos: "))

real1 = int(input("Digite a quantidade de moedas de 1 real: "))

real = (centavo1*0.01) + (centavo5*0.05) + (centavo10*0.10) + (centavo25*0.25) + (centavo50*0.50)

realTotal = real + real1

print(f"Voce tem {realTotal} reais")