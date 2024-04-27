"""Faça um prog que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele coquistou no final do jogo."""

from random import randint

cont = 0

print("*" * 60)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-" * 60)

while True:
    num_pc = randint(0, 10)
    num_user = input("Escolha um número de 0 a 10: ")
    op = input("Escolha par[P] ou ímpar[I]: ").strip().upper()[0]

    if op.isalpha() and num_user.isnumeric():
        if op == "P" or op == "I":
            num_user = int(num_user)
            soma = num_pc + num_user

            if soma % 2 == 0:
                comp = "P"
                res = "Par"
            else:
                comp = "I"
                res = "Ímpar"
            if op != comp:
                break
            else:
                cont += 1
                print(
                    f"""
{'VOCÊ GANHOU!!!'.center(60)}
                    
Você escolheu {num_user} e o Computador {num_pc}. A soma é {soma} que é {res}.

Vamos novamente...
"""
                )
                print("-" * 60)
        else:
            print("Informação inválida! Tente novamente.")
    else:
        print("Informação inválida! Tente novamente.")

print("-" * 60)
print(
    f"""
{'VOCÊ PERDEU!!!'.center (60)}
    
Você escolheu {num_user} e o Computador {num_pc}. A soma é {soma} que é {res}.
Você teve {cont} vitórias
"""
)
print("*" * 60)
