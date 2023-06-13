var = int(input("Digite a distância do trajeto: "))
if var <= 200:
    print(f"Você está prestes a começar uma viagem de {var} km")
    print(f"E o preço da sua viagem será de R$ {var * 0.50 :.2f}")
else:
    print(f"Você está prestes a começar uma viagem de {var} km")
    print(f"E o preço da sua viagem será de R$ {var * 0.45 :.2f}")
