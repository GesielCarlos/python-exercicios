preco = float(input("Preço das compras R$: "))
print("FORMAS DE PAGAMENTO")
print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
opcao = int(input("Digite sua escolha: "))
if opcao == 1:
    print(f"Sua compra de R$ {preco:.2f} vai custar R$ {preco - (preco * (10 / 100)):.2f} no final, sem juros.")
elif opcao == 2:
    print(f"Sua compra de R$ {preco:.2f} vai custar R$ {preco - (preco * (5 / 100)):.2f} no final, sem juros.")
elif opcao == 3:
    print(f"Sua compra de R$ {preco:.2f} parcelada em 2x vai custar R$ {preco / 2:.2f} cada parcela sem juros.")
else:
    parcela = int(input("Digite o número de parcelas: "))
    total_parc = (preco + (preco * (20 / 100))) / parcela
    print(f"Sua compra de R$ {preco:.2f} parcelada em {parcela}x vai custar R$ {total_parc:.2f} cada parcela com juros de 20%.")
    print(f"O total da sua compra será de R$ {total_parc * parcela:.2f}.")
