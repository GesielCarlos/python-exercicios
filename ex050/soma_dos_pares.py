numeros = list()
posicoes = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto', 'Sexto']

for posicao in posicoes:
    var = int(input((f"{posicao} número: ")))
    numeros.append(var)

soma = cont = 0

for n in numeros:
    if n % 2 == 0:
        soma += n
        cont += 1

if cont == 1:
    print(f"Você informou {cont} número par e ele é o {soma}")
else:
    print(f"Você informou {cont} números pares e a soma deles é {soma}")
