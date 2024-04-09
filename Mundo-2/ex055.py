"""Faça um prog que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

digitado = 0
maior = float("-inf")
menor = float("inf")

for i in range(1, 6):
    peso = input("Digite o peso da {}ª pessoa: ".format(i))

    if peso:
        peso = float(peso)
        digitado += 1

        if peso < menor:
            menor = peso

        if peso > maior:
            maior = peso

if digitado <= 1:
    print("Digite pelo menos 2 pesos!")
else:
    print(
        "Dos {} pesos que você digitou o menor foi {} Kg e o maior foi {} Kg.".format(
            digitado, menor, maior
        )
    )
