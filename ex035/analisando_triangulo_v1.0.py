retas = list()
posicoes = ['Primeiro', 'Segundo', 'Terceiro']

for posicao in posicoes:
    var = float(input(f"{posicao} segmento: "))
    retas.append(var)

if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]:
    print("Estas retas formam um triângulo")
else:
    print("Estas retas não formam um triângulo")
