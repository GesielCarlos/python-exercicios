from random import choice

posicoes = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']
alunos = list()
for posicao in posicoes:
    var = str(input(f"{posicao} aluno: "))
    alunos.append(var)
print(f"O aluno selecionado foi {choice(alunos)}")
