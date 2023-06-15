from time import sleep
from random import choice

jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']

print("Suas opções: ")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")
opcao = int(input("Digite a sua escolha: "))

sleep(0.4)
print("JO")
sleep(0.4)
print("KEN")
sleep(0.4)
print("PO!!!")

if opcao == 0:
    jogador = 'PEDRA'
elif opcao == 1:
    jogador = 'PAPEL'
else:
    jogador = 'TESOURA'

computador = choice(jokenpo)

if jogador == computador:
    print("=-" * 15)
    print(f"O computador escolheu {computador}")
    print(f"O jogador escolheu {jogador}")
    print("=-" * 15)
    print("EMPATE")
elif jogador == 'PEDRA' and computador == 'TESOURA':
    print("=-" * 15)
    print(f"O computador escolheu {computador}")
    print(f"O jogador escolheu {jogador}")
    print("=-" * 15)
    print("JOGADOR VENCEU")
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print("=-" * 15)
    print(f"O computador escolheu {computador}")
    print(f"O jogador escolheu {jogador}")
    print("=-" * 15)
    print("JOGADOR VENCEU")
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print("=-" * 15)
    print(f"O computador escolheu {computador}")
    print(f"O jogador escolheu {jogador}")
    print("=-" * 15)
    print("JOGADOR VENCEU")
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print("=-" * 15)
    print(f"O computador escolheu {computador}")
    print(f"O jogador escolheu {jogador}")
    print("=-" * 15)
    print("COMPUTADOR VENCEU")
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print("=-" * 15)
    print(f"O computador escolheu {computador}")
    print(f"O jogador escolheu {jogador}")
    print("=-" * 15)
    print("COMPUTADOR VENCEU")
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print("=-" * 15)
    print(f"O computador escolheu {computador}")
    print(f"O jogador escolheu {jogador}")
    print("=-" * 15)
    print("COMPUTADOR VENCEU")
