var = float(input("Qual o salário do funcionário? R$ "))
print(f"Com o aumento de 15% o salário do funcionário passará a ser R$ {var + (var * (15/100)):.2f}")