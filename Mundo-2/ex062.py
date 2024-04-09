"""Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O prog encerra quando ele disser que quer mostrar zero termos."""

termo = input("Digite o primeiro termo da Progressão Aritmética: ")
razao = input("Digite a razão da PA: ")

if termo.isnumeric() and razao.isnumeric():
    termo = int(termo)
    razao = int(razao)
    cont = 0
    total = 0
    print(
        "Os 10 primeiros termos da PA de acordo com o primeiro termo e a razão escolhida são: "
    )

    print("-" * 15)

    while cont < 10:
        print("      {}".format(termo))

        termo += razao

        cont += 1
        total += 1

    print("-" * 15)
    cont = 0

    rep = input("Gostaria de mostrar mais quantos termos? ")

    if rep.isnumeric():
        rep = int(rep)

        while rep > 0:

            print("-" * 15)
            while cont < rep:
                print("      {}".format(termo))

                termo += razao

                cont += 1
                total += 1

            print("-" * 15)

            rep -= 1

            rep = int(input("Gostaria de mostrar mais quantos termos? "))

            if rep == 0:
                print(
                    "Programa finalizado, com {} termos da PA escolhida mostrados!".format(
                        total
                    )
                )
            cont = 0

    else:
        print("Informação inválida!")
else:
    print("Digite todas as informações solicitadas!")
