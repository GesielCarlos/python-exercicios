posicoes = ['Primeiro', 'Segundo']
numeros = list()

for posicao in posicoes:
    num = int(input(f"{posicao} número: "))
    numeros.append(num)
if numeros[0] > numeros[1]:
    print(f"O primeiro número é maior")
elif numeros[0] < numeros[1]:
    print(f"O segundo número é maior")
else:
    print(f"Os números são iguais")
