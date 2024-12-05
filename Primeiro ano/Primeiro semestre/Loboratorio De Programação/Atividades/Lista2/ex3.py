numero = int(input("Digite um número inteiro entre 1 e 7: "))

if 1 <= numero <= 7:
    dias_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }
    print("O dia da semana correspondente ao número", numero, "é", dias_semana[numero])
else:
    print("Número inválido. Por favor, insira um número entre 1 e 7.")