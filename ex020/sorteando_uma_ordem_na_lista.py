import random

posicoes = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']
alunos = []

for posicao in posicoes:
    var = str(input(f"{posicao} aluno: "))
    alunos.append(var)

print("A ordem de apresentação será:")
random.shuffle(alunos)
for aluno in alunos:
    print(aluno)