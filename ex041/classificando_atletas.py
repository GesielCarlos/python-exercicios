from datetime import date

ano_nasc = int(input("Digite o ano em que você nasceu: "))
ano_atual = date.today().year

if ano_atual - ano_nasc <= 9:
    print(f"O atleta tem {ano_atual - ano_nasc} anos")
    print(f"Classificação: MIRIM")
elif ano_atual - ano_nasc <= 14:
    print(f"O atleta tem {ano_atual - ano_nasc} anos")
    print(f"Classificação: INFATIL")
elif ano_atual - ano_nasc <= 19:
    print(f"O atleta tem {ano_atual - ano_nasc} anos")
    print(f"Classificação: JÚNIOR")
elif ano_atual - ano_nasc <= 25:
    print(f"O atleta tem {ano_atual - ano_nasc} anos")
    print(f"Classificação: SÊNIOR")
else:
    print(f"O atleta tem {ano_atual - ano_nasc} anos")
    print(f"Classificação: MASTER")