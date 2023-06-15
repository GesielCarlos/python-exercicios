cont = soma = 0

for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        cont += 1
        soma += n
print(f"A soma de todos os {cont} valores solicitados é {soma}")
