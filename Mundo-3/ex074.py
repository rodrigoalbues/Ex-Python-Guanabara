"""Crie um prog que vai gerar 5 nrs aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de nrs gerados e também indique o menor e o maior valor que estão na tupla."""

from random import random

n1 = int(random() * 10)
n2 = int(random() * 10)
n3 = int(random() * 10)
n4 = int(random() * 10)
n5 = int(random() * 10)
print("=" * 60)
numeros = (n1, n2, n3, n4, n5)

maior = float("-inf")
menor = float("inf")
print("Os números gerados foram:")
for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    print(f"{n}".center(20))
print(f"O maior número gerado foi {maior} e o menor foi {menor}.")
print("=" * 60)
