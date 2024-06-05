import moeda

p = input("Digite o preço: R$ ")

if p:
    p = float(p)
    print(f"A metade de R$ {p:.2f} é: R$ {moeda.metade(p):.2f}")
    print(f"O dobro de R$ {p:.2f} é: R$ {moeda.dobro(p):.2f}")
    print(f"Aumentando 10%, temos: R$ {moeda.aumentar(p, 10):.2f}")
    print(f"Reduzindo 13%, temos: R$ {moeda.diminuir(p, 13):.2f}")
