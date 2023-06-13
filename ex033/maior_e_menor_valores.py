num = list()
posicoes = ['Primeiro', 'Segundo', 'Terceiro']

print("Digite os números a serem analisados...")

for posicao in posicoes:
    var = int(input(f"{posicao} número: "))
    num.append(var)

print(f"O maior número digitado foi {max(num)}")
print(f"O menor número digitado foi {min(num)}")
