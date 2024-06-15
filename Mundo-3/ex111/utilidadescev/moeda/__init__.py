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


def resumo(n, tx_aument=10, tx_dimin=5):
    p = float(n)
    print("-" * 60)
    print("RESUMO DO VALOR".center(60))
    print("-" * 60)
    print(f"{'Preço analisado: ':<45} {moeda(p)}")
    print(f"{'Dobro do preço: ':<45} {dobro(p, True)}")
    print(f"{'Metade do preço: ':<45} {metade(p, True)}")
    print(f"{f'Aumentando {tx_aument}%: ':<45} {aumentar(p, tx_aument, True)}")
    print(f"{f'Reduzindo {tx_dimin}%: ':<45} {diminuir(p, tx_dimin, True)}")
