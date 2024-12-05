notas = [3.5, 8.7,5, 6.9]
print(notas)
print(notas[2])
notas[3] = 10
print(notas)
#adicionar uma nota nota na lista
notas.append(9)
qtd = len(notas)
for i in range(qtd):
    valor = notas[i]
    print(f"{i} :: conteudo: {valor}")
    if valor >= 6:
        print(">>>>>>>>>>>>> PARABENS <<<<<<<<<<<<")
    