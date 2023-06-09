from time import sleep

nome = str(input("Digite o seu nome completo: "))

print("Analisando seu nome...")
sleep(0.5)

print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")
nome = nome.split()
print(f"Seu primeiro nome tem {len(nome[0])} letras")
