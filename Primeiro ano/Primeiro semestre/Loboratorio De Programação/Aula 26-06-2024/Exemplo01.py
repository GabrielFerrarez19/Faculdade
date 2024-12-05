def le_inteiro(msg):
    numero = int(input(msg))
    print(f"Nuemro digitado = {numero}")
    return numero 

idade = le_inteiro("Digite idade: ")
quantidade = le_inteiro("Digite a quantidade de pessoas: ")

print (f"Idade: {idade}")
print (f"Quantidade: {quantidade}")