import moeda

print("=" * 60)
while True:
    p = input("Digite o preço: R$ ")

    if p:
        p = float(p)
        print(f"A metade de {moeda.moeda(p)} é: {moeda.moeda(moeda.metade(p))}")
        print(f"O dobro de {moeda.moeda(p)} é: {moeda.moeda(moeda.dobro(p))}")
        print(f"Aumentando 10%, temos: {moeda.moeda(moeda.aumentar(p, 10))}")
        print(f"Reduzindo 13%, temos: {moeda.moeda(moeda.diminuir(p, 13))}")
        break
    else:
        print("Valor inválido..")
        print("-" * 60)
print("=" * 60)
