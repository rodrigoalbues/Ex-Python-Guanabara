"""Faça um prog que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""

pessoa = []
pessoas = []
mais_pesados = []
mais_leves = []
maior_peso = float("-inf")
menor_peso = float("inf")
print("=" * 80)
while True:
    nome = input("Digite o nome: ")
    peso = input("Digite o peso: ")
    if nome and peso:
        peso = float(peso)
        pessoa.append(nome)
        pessoa.append(peso)
        pessoas.append(pessoa[:])
        pessoa.clear()
        print("Cadastro realizado com sucesso...")
        print("-" * 80)
        continuar = input("Deseja continuar? [S/N] ").upper().strip()
        print()
        if continuar and continuar[0] == "N":
            break
    else:
        print("Informação inválida!")
qtd_pessoas = len(pessoas)
print(f"Foram cadastras {qtd_pessoas} pessoas.")

for p in pessoas:
    if p[1] > maior_peso:
        maior_peso = p[1]
for p in pessoas:
    if p[1] == maior_peso:
        mais_pesados.append(p[0])

for p in pessoas:
    if p[1] < menor_peso:
        menor_peso = p[1]
for p in pessoas:
    if p[1] == menor_peso:
        mais_leves.append(p[0])
print(f"O maior peso foi {maior_peso} Kg. E os mais pesados foram {mais_pesados}.")
print(f"O menor peso foi {menor_peso} Kg. E os mais leves foram {mais_leves}.")
print("=" * 80)
