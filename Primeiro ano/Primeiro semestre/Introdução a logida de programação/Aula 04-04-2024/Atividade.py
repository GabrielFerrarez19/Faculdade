Nome = input("Digite o seu nome:")

num1 = int(input("Digite um numero inteiro:"))
num2 = int(input("Digite outro numero inteiro:"))

if num1 == 99 and num2 == 99:
    print(f"{Nome}, numeros interressantes voce escolheu.")

if num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print("Não existe um numero maior que o outro")

contagem = input("Quer fazer uma contagem ate 10 de 2 em 2?")

if contagem == "sim":
   for i in range(0, 12, 2):
    print(i)
else:
   print("Vamos proseguir")

compra = input("Vamos criar uma lista de compra?")


if compra == "sim":
    lista = []
    while True:
        produto = input("Digite os produtos para a lista (Digite '99' para parar): ")
        if produto == "99":
            break
        lista += [produto]  
    
    print("Lista de compra:")
    for item in lista:
        print(item)
else:
    print("Ok, finalizando agora")
