"""A confederação nacional de natação precisa de um prog  que leia o ano de nascimento de um atleta e mostre sua categoria , de acordo com a idade:
- Até 9 anos: MIRIM
- ATé 14 anos: INFANTIL
- até 19 anos: JUNIOR
-até 20 anos: SENIOR
- acima: MASTER"""

from datetime import date

a = input("Qual o ano de nascimento do atleta? ")

if a and a.isnumeric():
    i = int(a)
    atual = date.today().year
    idade = atual - i
    if idade <= 9:
        categoria = "mirim"
    elif idade > 9 and idade <= 14:
        categoria = "infantil"
    elif idade > 14 and idade <= 19:
        categoria = "junior"
    elif idade > 19 and idade <= 20:
        categoria = "senior"
    else:
        categoria = "master"
    print("Esse atleta tem {} anos e pertence a categoria {}.".format(idade, categoria))
else:
    print("Preencha as informações corretamente!")
