var = int(input("Digite a velocidade atual do carro: "))
if var > 80:
    print("MULTADO! Você excedeu o limite de velocidade de 80km/h.")
    print(f"A multa a ser paga será de R$ {(var - 80) * 7 :.2f}")
print("Tenha um bom dia! Dirija com segurança.")