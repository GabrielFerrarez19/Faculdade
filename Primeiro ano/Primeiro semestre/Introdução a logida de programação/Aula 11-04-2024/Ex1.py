# EX.1 Faça a contagem de combinações desta lisa
comidas = ['bacon','lasanha','churrasco','ervilha','mingau','hamburguer']
frutas = ['pera','uva','maça','melancia','goiaba']
contador=0

print("VAMOS VER AS COMBINAÇÕES:")
for x in comidas:
    for y in frutas:
        print(f"{x} com {y}")
        contador +=1

print(f"Forem um total de {contador} combinações!")