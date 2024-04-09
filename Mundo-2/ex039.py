"""Faça um prog que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- se ele ainda vai se alistar ao servico militar
- Se é a hora de se alistar
- se já passou do tempo do alistamento.
Seu prog também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

i = input("Informe o ano em que nasceu: ")
atual = date.today().year

if i:
    nasc = int(i)
    idade = atual - nasc
    if idade < 18:
        print("Você ainda vai se alistar ao servico militar.")
    elif idade > 18:
        print("Você já passou do tempo do alistamento.")
    else:
        print("Você está com {} anos. É a hora de você se alistar".format(idade))

    tempo = idade - 18

    if tempo > 0:
        print(
            "Você tem {} anos. Passou {} anos do ano do seu alistamento. Seu alistamento foi em {}.".format(
                idade, tempo, atual - tempo
            )
        )

    if tempo < 0:
        tempo = tempo * (-1)
        print(
            "Você tem {} anos. Faltam {} anos para o ano do seu alistamento. Seu alistamento será em {}.".format(
                idade, tempo, atual + tempo
            )
        )
else:
    print("Preencha as informações")
