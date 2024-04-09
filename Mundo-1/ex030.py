# Crie um prog que leia um número inteiro e mostre na tela se ele é par ou ímpar.
n = input("Digite um número inteiro: ")

if n:
    nInt = int(n)
    if nInt % 2 == 0:
        print("O número {} é par.".format(nInt))
    else:
        print("O número {} é ímpar.".format(nInt))
else:
    print("Você não digitou o número! Tente novamente.")
