ingredientes = ['tomate','agriao','bacon','pão de queijo','mel']
contador = 0

for x in ingredientes:
    for y in ingredientes:
        for z in  ingredientes:
            if (x != y) and (x != z) and (y != z):
                print(f"{x} com {y} com {z}")
                contador +=1

print(f"Forem um total de {contador} combinações!")