# Escreva um prog que faça o computador 'pensar' em um nr inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O prog deverá  escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

nPc = randint(0, 5)

nUs = input("Tente acertar qual número inteiro entre 0 e 5 o computador escolheu: ")

sleep(3)  # O computador fica esperando por 3 segundos

if nUs:
    nUser = int(nUs)
    if nPc == nUser:
        print("Você venceu!!!")
    else:
        print("Você perdeu!!!")

    print("O número escolhido pelo computador foi {}".format(nPc))
else:
    print("Informação inválida! Tente novamente.")
