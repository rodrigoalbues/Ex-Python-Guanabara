# Faça um prog que leia 3 números e mostre qual é o maior e qual é o menor.

n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
n3 = input("Digite o terceiro número: ")

if n1 and n2 and n3:
    numeros = [int(n1), int(n2), int(n3)]
    maior = int(n1)
    menor = int(n1)
    for i, n in enumerate(numeros):
        if numeros[i] > maior:
            maior = numeros[i]
    for i, n in enumerate(numeros):
        if numeros[i] < menor:
            menor = numeros[i]

    print("O maior número é: {}".format(maior))
    print("O menor número é: {}".format(menor))
else:
    print("Informação incorreta! Tente novamente.")
