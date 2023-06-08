var = input("Digite algo: ")
if var.isnumeric():
    print(f"O tipo primitivo da variável é {type(int(var))}")
else:
    print(f"O tipo primitivo da variável é {type(var)}")

if var.isspace():
    print(f"Só tem espaços? Sim!")
else:
    print(f"Só tem espaços? Não!")

if var.isnumeric():
    print(f"É um número? Sim!")
else:
    print(f"É um número? Não!")

if var.isalpha():
    print(f"É alfabético? Sim!")
else:
    print(f"É alfabético? Não!")

if var.isalnum():
    print(f"É alfanumérico? Sim!")
else:
    print(f"É alfanumérico? Não!")

if var.isupper():
    print(f"É maiúscula? Sim!")
else:
    print(f"É maiúscula? Não!")

if var.islower():
    print(f"É minúscula? Sim!")
else:
    print(f"É minúscula? Não!")

if var.istitle():
    print(f"É capitalizada? Sim!")
else:
    print(f"É capitalizada? Não!")
