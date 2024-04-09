"""Crie um prog que mostre na tela todos os nrs pares que estão no intervalo entre 1 e 50."""

from time import sleep

print(
    "Escolha o intervalo de números inteiros que gostaria de saber os números pares. (o primeiro deve ser o menor número.)"
)
intInf = input("Digite o primeiro número: ")
intSup = input("Digite o segundo número: ")


if intInf and intSup:
    n1 = int(intInf)
    n2 = int(intSup)
    print("Os números pares entre {} e {} são:".format(n1, n2))
    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            print(i)
            sleep(0.5)
    print("Acabou!!!")
else:
    print("Digite todas as informações!")
