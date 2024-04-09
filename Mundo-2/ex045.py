# Crie um prog que faça o computador jogar jokenpô com vc.
from random import randint

itens = ("Pedra", "Papel", "Tesoura")
comput = randint(0, 2)

print(
    """Suas opções:
      0 - PEDRA
      1 - PAPEL
      2 - TESOURA"""
)

jog = int(input("Qual a sua jogada? "))

if jog != 0 and jog != 1 and jog != 2:
    print("Opção inválida")

else:

    print("-=" * 13)

    print("Computador jogou {}".format(itens[comput]))
    print("Jogador jogou {}".format(itens[jog]))

    print("-=" * 13)

    if comput == 0:
        if jog == 0:
            print("EMPATOU")
        elif jog == 1:
            print("Jogador VENCEU!")
        elif jog == 2:
            print("Computador VENCEU!")

    elif comput == 1:
        if jog == 0:
            print("Computador VENCEU!")
        elif jog == 1:
            print("EMPATOU")
        elif jog == 2:
            print("Jogador VENCEU!")

    elif comput == 2:
        if jog == 0:
            print("Jogador VENCEU!")
        elif jog == 1:
            print("Computador VENCEU!")
        elif jog == 2:
            print("EMPATOU")
