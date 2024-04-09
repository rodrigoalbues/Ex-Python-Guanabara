"""Desenvolva um prog que leia 6 nrs inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""

s = 0
cont = 0
for i in range(1, 7):

    n = input("Digite o {}º número inteiro: ".format(i))

    if n:

        n = int(n)

        if n % 2 == 0:
            s += n
            cont += 1
    else:

        s = s + 0

print("Você digitou {} números inteiros pares e a soma deles é: {}".format(cont, s))
