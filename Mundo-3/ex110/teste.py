import moeda

print("=" * 60)
while True:
    p = input("Digite o preço: R$ ")

    if p:
        moeda.resumo(p, 20, 12)
        break
    else:
        print("Valor inválido..")
        print("-" * 60)
print("=" * 60)
