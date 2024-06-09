"""Modifique as funções que foram criadas no ex107 para que elas aceitem um parâmetro a mais, informado se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no ex108."""


def aumentar(n, tx, formatado=False):
    res = n * (1 + (tx / 100))
    if formatado:
        return moeda(res)
    else:
        return res


def diminuir(n, tx, formatado=False):
    res = n - (n * tx / 100)
    if formatado:
        return moeda(res)
    else:
        return res


def dobro(n, formatado=False):
    res = n * 2
    if formatado:
        return moeda(res)
    else:
        return res


def metade(n, formatado=False):
    res = n / 2
    if formatado:
        return moeda(res)
    else:
        return res


def moeda(n, moeda="R$"):
    m = f"{moeda} {n:_.2f}".replace(".", ",").replace("_", ".")

    return m
