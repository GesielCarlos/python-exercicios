posicoes = ['Primeira', 'Segunda', 'Terceira']
reta = list()

for posicao in posicoes:
    var = float(input(f"{posicao} reta: "))
    reta.append(var)
if reta[0] < reta[1] + reta[2] and reta[1] < reta[0] + reta[2] and reta[2] < reta[0] + reta[1]:
    if reta[0] == reta[1] == reta[2]:
        print("As retas podem formar um triângulo EQUILÁTERO!")
    elif reta[0] != reta[1] != reta[2] != reta[0]:
        print("As retas podem formar um triângulo ESCALENO")
    else:
        print("As retas podem formar um triângulo ISÓSCELES")
else:
    print("As retas não podem formar um triângulo")
