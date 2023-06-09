from math import sqrt

num1 = float(input("Digite o valor do cateto oposto: "))
num2 = float(input("Digite o valor do cateto adjacente: "))
h = sqrt((num1 ** 2) + (num2 ** 2))
print(f"A hipotenusa medi {h:.2f}")
