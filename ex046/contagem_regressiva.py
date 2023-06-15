from time import sleep

var = int(input("Digite um número: "))
for n in range(0, 11):
    sleep(0.6)
    print(f"{var}")
    var -= 1
sleep(0.4)
print("BUM! BUM! POOOW!")
