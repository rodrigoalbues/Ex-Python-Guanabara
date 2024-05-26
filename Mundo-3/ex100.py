"""Faça um prog que tenha uma lista chamada números e 2 funções chamadas sorteio() e soma(). A 1ª função vai sortear 5 nrs e vai colocá-los dentro da lista e a 2ª função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint

nrs = []


def sorteio():
    for i in range(0, 5):
        nrs.append(randint(0, 10))


def soma():
    soma_pares = 0
    for n in nrs:
        if n % 2 == 0:
            soma_pares += n
    return soma_pares


sorteio()
soma_pares = soma()
print(nrs, soma_pares)
