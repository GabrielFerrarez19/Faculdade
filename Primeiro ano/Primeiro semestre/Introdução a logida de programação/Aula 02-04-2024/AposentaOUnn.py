idade = float(input("Digite sua idade:"))

contribuicao = int(input("Digite seus anos de contribuição:"))

if idade >= 65 and contribuicao >=30:
    print("aposetadoria aprovada")
else:
    print("aposentadoria reprovada")