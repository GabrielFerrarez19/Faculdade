nome = input("digite nome:")
opcao = input("deseja informar idade? (S - sim N-nao):")

if opcao.upper() == 'S':
    idade = int(input(f"{nome}, digite a idade: "))
    print(f"{nome} tem {idade} anos")
else:
    print(f"ok,tudo bem {nome}")

print(f"{nome} tem {idade} anos")
