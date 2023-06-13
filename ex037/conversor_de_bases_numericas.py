var = int(input("Digite um número: "))
print("Escolha uma das bases para conversão:")
print("[1] converter para BINÁRIO")
print("[2] converter para HEXADECIMAL")
print("[3] converter para OCTAL")
escolha = int(input("Sua escolha: "))

if escolha == 1:
    print(f"{var} convertido para BINÁRIO é {bin(var)[2:]}")
elif escolha == 2:
    print(f"{var} convertido para HEXADECIMAL é {hex(var)[2:]}")
else:
    print(f"{var} convertido para OCTAL é {oct(var)[2:]}")
