"""Crie um prog que leia o ano de nasc de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos já são maiores."""

from datetime import date

idades = 0
maior = 0
menor = 0
atual = date.today().year

for i in range(1, 8):
    ano = input("Digite o ano de nascimento da {}ª pessoa: ".format(i))

    if ano and ano.isnumeric():

        ano = int(ano)
        idades += 1

        idade = atual - ano

        if idade >= 18:
            maior += 1
        else:
            menor += 1

if idades == 0:
    print("Digite pelo menos uma idade!")
else:
    print(
        "Das {} pessoas que você digitou o ano de nascimento {} ainda não atingiram a maioridade e {} já são maiores de idade.".format(
            idades, menor, maior
        )
    )
