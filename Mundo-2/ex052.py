"""Faça um prog que leia um nr inteiro e diga se ele é ou não um nr primo."""

n = input("Digite um número inteiro: ")

if n:

    teste = n.isnumeric()
    if teste == True:
        n = int(n)
        multi = 0
        for i in range(1, n + 1):

            if n % i == 0:
                multi += 1
        if multi == 2:
            print("Esse número é primo.")
        else:
            print(
                "O número {} não é primo, ele foi divisível {} vezes.".format(n, multi)
            )
    else:
        print("Somente números são aceitos!")
else:
    print("Favor digitar o número desejado!")
