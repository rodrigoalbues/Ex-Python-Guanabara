"""Desenvolva um prog que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progessão."""

termo = input("Digite o primeiro termo da Progressão Aritmética: ")
razao = input("Digite a razão da PA: ")

if termo and razao:
    termo = int(termo)
    razao = int(razao)

    print(
        "Os 10 primeiros termos da PA de acordo com o primeiro termo e a razão escolhida são: "
    )

    print("-" * 15)

    for i in range(1, 11):

        print("      {}".format(termo))

        termo += razao

    print("-" * 15)

else:
    print("Digite todas as informações solicitadas!")
