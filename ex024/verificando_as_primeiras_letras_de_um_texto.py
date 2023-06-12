var = str(input("Digite o nome da cidade que você nasceu: "))
nome = var.lower().split()
if 'são' or 'santo' in nome:
    print(f"O nome da sua cidade começa com São!")
else:
    print(f"O nome da sua cidade não começa com São!")
