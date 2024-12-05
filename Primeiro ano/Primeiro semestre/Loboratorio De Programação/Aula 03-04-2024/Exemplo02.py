valo1 = int(input("Digite valor1:"))

valor2 = int(input("Digite valor2:"))

igualdade = valo1 == valor2
print(f"A afirmação que {valo1} eh igual {valor2} eh {igualdade}")

if igualdade:
    print("Sao iguais")

if not igualdade:
    print("Sao diferentes")

print("Fim do programa")