def altera_nome():
    # variavel local
    global nome
    nome = "Feioso"
    print("----- Dentro da funcao ------")
    print(nome)

# variavel global
nome = "Lidovaldo"
altera_nome()
print("----- fora da funcao------")
print(nome)