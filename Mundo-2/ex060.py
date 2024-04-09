"""Faça um prog que leia 1 nr qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

num = input("Escolha um número inteiro: ")
cont = num
fat = 1
if num.isnumeric():
    cont = int(cont)
    fat = int(fat)
    while cont > 0:
        fat = fat * cont
        cont -= 1

    print("O fatorial de {} é {}.".format(num, fat))

else:
    print("Digite um valor!")
