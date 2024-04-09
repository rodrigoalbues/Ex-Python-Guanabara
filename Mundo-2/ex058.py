"""Melhore o jodo do desafia 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
from time import sleep

nPc = randint(0, 10)

nUs = input("Tente acertar qual número inteiro entre 0 e 10 o computador escolheu: ")
palpite = 1
if nUs.isnumeric:
    nUs = int(nUs)

    sleep(1)

    while nPc != nUs:
        if nPc != nUs:
            print("Você errou!!!")
            nUs = input("Tente novamente: ")
            palpite += 1
            if nUs.isnumeric():
                nUs = int(nUs)

    print("Parabéns, você acertou!!!")
    print(
        "O número escolhido pelo computador foi {} você deu {} palpites para acertar.".format(
            nPc, palpite
        )
    )
