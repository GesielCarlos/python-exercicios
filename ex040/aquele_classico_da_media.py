posicoes = ['Primeiro', 'Segundo']
notas = list()

for posicao in posicoes:
    var = float(input(f"{posicao} nota: "))
    notas.append(var)

media = (notas[0] + notas[1]) / 2
if media < 5:
    print(f"Sua média foi {media:.1f}. Você está REPROVADO!")
elif 5 >= media <= 6.9:
    print(f"Sua média foi {media:.1f}. Você está de RECUPERAÇÃO!")
else:
    print(f"Sua média foi {media:.1f}. Você foi APROVADO!")
