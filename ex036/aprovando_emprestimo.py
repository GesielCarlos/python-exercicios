casa = float(input("Valor da casa: "))
salario = float(input("Salário do comprador: "))
anos = float(input("Anos de financiamento: "))

prestacao = casa / (anos * 12)

print(f"Para pagar uma casa de R$ {casa:.2f} em {anos:.0f} anos a prestação será de R$ {prestacao:.2f}")

if prestacao < salario * (30 / 100):
    print("Empréstimo concedido")
else:
    print("Empréstimo negado")
