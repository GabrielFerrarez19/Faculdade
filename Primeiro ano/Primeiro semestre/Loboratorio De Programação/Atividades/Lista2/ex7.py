import random

acertos = 0

print("Responda às perguntas de soma abaixo:")

for i in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    resposta_correta = a + b
    pergunta = f"Qual é a soma de {a} + {b}?"
    print("\nPergunta", i+1, ":", pergunta)
    resposta_aluno = int(input("Sua resposta: "))
    if resposta_aluno == resposta_correta:
        print("Resposta correta!")
        acertos += 1
    else:
        print("Resposta incorreta. A resposta correta é:", resposta_correta)

print("\nVocê acertou", acertos, "perguntas de um total de 5.")