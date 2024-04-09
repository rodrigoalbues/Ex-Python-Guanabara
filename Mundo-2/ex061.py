""" Refaça o desafio 051, lendo o 1º termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."""

termo = input("Digite o primeiro termo da Progressão Aritmética: ")
razao = input("Digite a razão da PA: ")

if termo.isnumeric() and razao.isnumeric():
    termo = int(termo)
    razao = int(razao)
    cont = 0
    print(
        "Os 10 primeiros termos da PA de acordo com o primeiro termo e a razão escolhida são: "
    )

    print("-" * 15)

    while cont < 10:
        print("      {}".format(termo))

        termo += razao

        cont += 1

    print("-" * 15)

else:
    print("Digite todas as informações solicitadas!")
