peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))
imc = peso / (altura ** 2)

print(f"O seu IMC é de {imc:.1f}")
if imc <= 18.5:
    print("Você está abaixo do peso!")
elif 18.6 <= imc <= 24.9:
    print("Você está com o peso ideal!")
elif 25<= imc <= 29.99:
    print("Você está com sobrepeso!")
elif 30 <= imc <= 34.9:
    print("Você está com obesidade I!")
elif 35 <= imc <= 39.9:
    print("Você está com obesidade II!")
else:
    print("Você está com obesidade III!")
