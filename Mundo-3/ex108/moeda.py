"""Adapte o cod do ex107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado."""


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


def moeda(n, moeda="R$"):
    m = f"{moeda} {n:_.2f}".replace(".", ",").replace("_", ".")

    return m
