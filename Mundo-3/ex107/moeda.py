"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro(), metade().
Faça tbm um prog que importe esse módulo e use algumas dessas funções."""


def aumentar(n, tx):
    res = n * (1 + (tx / 100))
    return res


def diminuir(n, tx):
    res = n - (n * tx / 100)
    return res


def dobro(n):
    res = n * 2
    return res


def metade(n):
    res = n / 2
    return res
