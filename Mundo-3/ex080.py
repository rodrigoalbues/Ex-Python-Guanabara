"""Crie um prog onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort(). No final, mostre a lista ordenada na tela."""

valores = []
print("=" * 80)
for i in range(0, 5):
    valor = input("Digite um valor: ")
    if valor.isnumeric():
        valor = int(valor)
        if i == 0 or valor > valores[-1]:
            valores.append(valor)
            print("Adicionado ao final da lista...")
        else:
            pos = 0
            while pos < len(valores):
                if valor <= valores[pos]:
                    valores.insert(pos, valor)
                    print(f"Adicionado na posição {pos} da lista...")
                    break
                pos += 1
    else:
        print("Informação inválida!")
print("-" * 80)
print(f"Os valores digitados em ordem foram {valores}")
print("=" * 80)
