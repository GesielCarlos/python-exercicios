from datetime import date

ano_nasc = int(input("Digite o seu ano de nascimento: "))
ano_atual = date.today().year
ano_alist = date.today().year - ano_nasc

print(f"Quem nasceu em {ano_nasc} tem {date.today().year - ano_nasc} anos em {date.today().year}")

if ano_alist < 18:
    print(f"Ainda falta {18 - ano_alist} anos para seu alistamento")
    print(f"Seu alistamento será em {18 - ano_alist + ano_atual}")
elif ano_alist > 18:
    print(f"Você já deveria ter se alistado há {ano_alist - 18} anos")
    print(f"Seu alistamento foi em {ano_atual - (ano_alist - 18)}")
else:
    print(f"Esse é o seu ano de alistamento")
    print(f"Vá há um posto de alistamento e realize seu cadastro")
