"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
soma_pares = 0

print("=" * 80)
for i in range(0, 3):
    l1 = input(f"Digite um valor inteiro para [0, {i}]: ")
    if l1.isnumeric():
        l1 = int(l1)
        if l1 % 2 == 0:
            soma_pares += l1
        linha1[i].append(l1)
    else:
        print("Informação inválida!")
        linha1[i].append("")
for i in range(0, 3):
    l2 = input(f"Digite um valor inteiro para [1, {i}]: ")
    if l2.isnumeric():
        l2 = int(l2)
        if l2 % 2 == 0:
            soma_pares += l2
        linha2[i].append(l2)
    else:
        print("Informação inválida!")
        linha2[i].append("")
for i in range(0, 3):
    l3 = input(f"Digite um valor inteiro para [2, {i}]: ")
    if l3.isnumeric():
        l3 = int(l3)
        if l3 % 2 == 0:
            soma_pares += l3
        linha3[i].append(l3)
    else:
        print("Informação inválida!")
        linha3[i].append("")
soma_coluna3 = linha1[2][0] + linha2[2][0] + linha3[2][0]
maior_l2 = max(linha2)
print("-" * 80)
print(
    f"""[{str(linha1[0][0]).center(5)}] [{str(linha1[1][0]).center(5)}] [{str(linha1[2][0]).center(5)}]
[{str(linha2[0][0]).center(5)}] [{str(linha2[1][0]).center(5)}] [{str(linha2[2][0]).center(5)}]
[{str(linha3[0][0]).center(5)}] [{str(linha3[1][0]).center(5)}] [{str(linha3[2][0]).center(5)}]"""
)
print("-" * 80)
print(f"A soma dos valores pares é: {soma_pares}.")
print(f"A soma dos valores da terceira coluna é: {soma_coluna3}.")
print(f"O maior valor da segunda linha é: {maior_l2}")
print("=" * 80)
