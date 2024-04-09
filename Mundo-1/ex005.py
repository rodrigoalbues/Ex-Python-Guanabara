# Faça um programa que leia um nr inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input("Digite um número inteiro: "))
a = n - 1
s = n + 1

print(
    "O número digitado foi {}, que tem como antecessor o número {} e o como sucessor o número {}.".format(
        n, a, s
    )
)