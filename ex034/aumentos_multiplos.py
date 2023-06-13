var = float(input("Digite o salário do funcionário: "))
if var <= 1250:
    print(f"Quem recebia R$ {var:.2f} passará a receber R$ {var + (var * (15 / 100)):.2f}")
else:
    print(f"Quem recebia R$ {var:.2f} passará a receber R$ {var + (var * (10 / 100)):.2f}")
