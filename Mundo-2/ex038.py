"""Escreva um prog que leia 2 nrs inteiros e compare-os, mostrando na tela uma msg:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os 2 são iguais"""

np = input("Digite um número inteiro: ")
ns = input("Digite outro número inteiro: ")

if np and ns:
    n1 = int(np)
    n2 = int(ns)
    if n1 > n2:
        print(
            "O primeiro valor é maior. Porque o número {} é maior que o número {}.".format(
                n1, n2
            )
        )
    elif n2 > n1:
        print(
            "O segundo valor é maior. Porque o número {} é maior que o número {}.".format(
                n2, n1
            )
        )
    else:
        print("Não existe valor maior, os 2 são iguais.")

else:
    print("Preencha todas as informações!")
