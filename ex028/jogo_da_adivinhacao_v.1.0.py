import random
from time import sleep

print("-=" * 30)
print("Vou pensar em um número de 0 a 5. Tente advinhar...")
print("-=" * 30)

# list_num = ['0','1', '2', '3', '4', '5']  # essa é uma forma de fazer o computador escolher um 
# num_maq = random.choice(list_num)         # número. Caso use essa forma vai ser necessário 
                                            # transformar o valor de num_maq para inteiro no 
                                            # comando if dessa forma: int(num_maq), pois o 
                                            # resultado do choice vai ser uma str
                                            

num_maq = random.randint(0, 5)

var = int(input("Em qual número eu pensei? "))

print("PROCESSANDO...")
sleep(1)
if var == num_maq:
    print(f"GANHOU! O número que eu pensei foi {num_maq}")
else:
    print(f"PERDEU! O número que eu pensei foi {num_maq}")
