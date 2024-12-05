num_alunos = int(input("Informe a quantidade de alunos:"))
notas = [] #criar uma lista vazia

#ler as notas
for i in range(1,num_alunos+1):
    nota_aluno = float(input(f"Digite a nota do {i}° aluno: "))
    notas.append(nota_aluno)
    #soma += nota_aluno

#calcular a media
media = sum(notas)/len(notas)
print(f"A media da turma foi {media}")

for indece in range(len(notas)):
    nota = notas[indece]
    if nota > media:
        print(f"{indece}::{nota} - parabens")