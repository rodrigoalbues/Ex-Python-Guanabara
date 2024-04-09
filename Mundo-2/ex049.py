"""Refaça o desafia 009, mostrando a tabuada de um nr que o usuário escolher, só que agora utilizando um laço for."""

n = input("Digite um número para ver sua tabuada: ")

if n:

    n = int(n)

    print("-" * 15)
    for i in range(1, 11):
        print("  {} x {:2} = {}".format(n, i, (n * i)))

    print("-" * 15)
else:
    print("Digite o número desejado.")
