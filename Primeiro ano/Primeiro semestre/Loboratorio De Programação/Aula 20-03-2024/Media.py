#entrada de dados referente as duas provas
prova1 = float(input("Digite a nota da primeira prova:"))
prova2 = float(input("Digite a nota da segunda prova:"))

#realiza a operação que da peso para a nota das provas
provas = (3*prova1+3*prova2)

#entrada de dados referente a trabalho
trabalhos = float(input("Digite a nota de trabalho:"))

#entrada de dados referente a participação
participação = float(input("Digite a nota de participação:"))

#realiza o calculo da media
media = (provas+3*trabalhos+participação)/10

#imprime o resultado da media calculada
input(f"A media final desse aluno foi {media}")