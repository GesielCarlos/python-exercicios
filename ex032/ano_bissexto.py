from datetime import date

var = int(input("Digite o ano que quer analisar (Digite 0 para checar o ano atual): "))
if var == 0:
    var = date.today().year
if var % 4 == 0 and var % 100 !=0 or var % 400 == 0:
    print(f"O ano {var} é bissexto")
else:
    print(f"O ano {var} não é bissexto")
