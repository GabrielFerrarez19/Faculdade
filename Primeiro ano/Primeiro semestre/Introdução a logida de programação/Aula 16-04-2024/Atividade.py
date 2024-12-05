i = 0
lista1 = []
item = input("Digite os itens da lista1 (digite '99' para parar): ")
while item != '99':
    lista1.append(item)
    i += 1
    item = input("Digite os itens da lista1 (digite '99' para parar): ")

x = 0
lista2 = []
item2 = input("Digite os itens da lista2 (digite '99' para parar): ")
while item2 != '99':
    lista2.append(item2)
    x += 1
    item2 = input("Digite os itens da lista2 (digite '99' para parar): ")

contador = 0
for item1 in lista1:  # Renomeando a variável de iteração para evitar confusão
    for item2 in lista2:  # Renomeando a variável de iteração para evitar confusão
        if item1 == 'tomate' and item2 == 'tomate':
            item1 = item1.upper()
            item2 = item2.upper()
        if item1 != item2:
            print(f"{item1} com {item2}")
            contador += 1

print(f"Forem um total de {contador} combinações!")


