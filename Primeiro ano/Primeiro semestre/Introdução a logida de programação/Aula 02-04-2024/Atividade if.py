numero = int(input("Digite um numero inteiro:"))

if numero > 0 and numero%2 == 0:
    print(f"O nomero {numero} é positivo e par.")
elif numero > 0 and numero%2 != 0: 
    print(f"O nomero {numero} é positivo e impar.")
else:
    print(f"O numero {numero} nao e positivo.")