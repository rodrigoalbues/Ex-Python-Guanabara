"""Crie um prog que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta."""

linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]

print("=" * 80)
for i in range(0, 3):
    l1 = input(f"Digite um valor inteiro para [0, {i}]: ")
    if l1.isnumeric():
        l1 = int(l1)
        linha1[i].append(l1)
    else:
        print("Informação inválida!")
        linha1[i].append("")
for i in range(0, 3):
    l2 = input(f"Digite um valor inteiro para [1, {i}]: ")
    if l2.isnumeric():
        l2 = int(l2)
        linha2[i].append(l2)
    else:
        print("Informação inválida!")
        linha2[i].append("")
for i in range(0, 3):
    l3 = input(f"Digite um valor inteiro para [2, {i}]: ")
    if l3.isnumeric():
        l3 = int(l3)
        linha3[i].append(l3)
    else:
        print("Informação inválida!")
        linha3[i].append("")
print("-" * 80)
print(linha1[0], linha1[1], linha1[2])
print(linha2[0], linha2[1], linha2[2])
print(linha3[0], linha3[1], linha3[2])
print("=" * 80)
