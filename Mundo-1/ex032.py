# Faça um prog que leia um ano qualquer e mostre se é bissexto.
from datetime import date

a = input("Digite o ano, coloque zero para analisar o ano atual: ")

if a:
    ano = int(a)
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print("O ano {} é bissexto.".format(ano))
            else:
                print("O ano {} não é bissexto.".format(ano))
        else:
            print("O ano {} é bissexto.".format(ano))
    else:
        print("O ano {} não é bissexto.".format(ano))

else:
    print("Você não digitou o ano! Tente novamente.")
