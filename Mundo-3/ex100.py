"""Faça um prog que tenha uma lista chamada números e 2 funções chamadas sorteio() e soma(). A 1ª função vai sortear 5 nrs e vai colocá-los dentro da lista e a 2ª função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint
from time import sleep


print("=" * 60)


def sorteio():
    nrs = []
    print(f"Sorteando 5 valores da lista: ", end=" ")
    for i in range(0, 5):
        n = randint(0, 10)
        nrs.append(n)
        print(n, end=" ", flush=True)
        sleep(0.3)
    print("PRONTO!")
    return nrs


def soma(*num):
    soma_pares = 0
    for n in nrs:
        if n % 2 == 0:
            soma_pares += n
    print(f"Somando os valores pares de {nrs}, temos {soma_pares}.")


nrs = sorteio()
soma_pares = soma(nrs)
print("=" * 60)
